import unicodedata
import nltk

from nltk.corpus import wordnet as wn
from nltk.stem import SnowballStemmer


METEOR_ALPHA = 0.9
METEOR_BETA = 3.0
METEOR_GAMMA = 0.5

STEMMER_PT = SnowballStemmer("portuguese")

INDICE_SINONIMOS_OMW = None


def normalizar_texto(texto: str) -> str:
    return unicodedata.normalize(
        "NFC",
        str(texto)
    ).lower().strip()


def tokenizar_portugues(texto: str) -> list[str]:
    return nltk.word_tokenize(
        normalizar_texto(texto),
        language="portuguese"
    )


def obter_stem(palavra: str) -> str:
    return STEMMER_PT.stem(
        normalizar_texto(palavra)
    )


def construir_indice_sinonimos_omw():
    global INDICE_SINONIMOS_OMW

    if INDICE_SINONIMOS_OMW is not None:
        return

    print(
        "Carregando Open Multilingual WordNet "
        "para português..."
    )

    wn.synsets(
        "exibir",
        lang="por"
    )

    indice = {}

    total_synsets = 0

    for synset in wn.all_synsets(
        lang="por"
    ):
        total_synsets += 1

        lemas = {
            normalizar_texto(lema)

            for lema in synset.lemma_names(
                lang="por"
            )

            if lema
            and "_" not in lema
        }

        stems = {
            obter_stem(lema)

            for lema in lemas

            if lema
        }

        if len(stems) < 2:
            continue

        for stem_origem in stems:

            indice.setdefault(
                stem_origem,
                set()
            )

            indice[
                stem_origem
            ].update(
                stems - {stem_origem}
            )

    INDICE_SINONIMOS_OMW = indice

    print(
        f"Índice OMW construído: "
        f"{len(indice)} stems possuem "
        f"relações de sinonímia."
    )

    print(
        f"Synsets portugueses percorridos: "
        f"{total_synsets}.\n"
    )


def alinhar_exatos(
    hipoteses,
    referencias
):
    hipoteses = hipoteses.copy()
    referencias = referencias.copy()

    matches = []

    for i in range(
        len(hipoteses) - 1,
        -1,
        -1
    ):
        for j in range(
            len(referencias) - 1,
            -1,
            -1
        ):
            if (
                hipoteses[i][1]
                ==
                referencias[j][1]
            ):
                matches.append(
                    (
                        hipoteses[i][0],
                        referencias[j][0]
                    )
                )

                hipoteses.pop(i)
                referencias.pop(j)

                break

    return (
        matches,
        hipoteses,
        referencias
    )


def alinhar_stems(
    hipoteses,
    referencias
):
    hipoteses = hipoteses.copy()
    referencias = referencias.copy()

    matches = []

    for i in range(
        len(hipoteses) - 1,
        -1,
        -1
    ):

        stem_hipotese = obter_stem(
            hipoteses[i][1]
        )

        for j in range(
            len(referencias) - 1,
            -1,
            -1
        ):

            stem_referencia = obter_stem(
                referencias[j][1]
            )

            if (
                stem_hipotese
                ==
                stem_referencia
            ):
                matches.append(
                    (
                        hipoteses[i][0],
                        referencias[j][0]
                    )
                )

                hipoteses.pop(i)
                referencias.pop(j)

                break

    return (
        matches,
        hipoteses,
        referencias
    )


def alinhar_sinonimos_omw(
    hipoteses,
    referencias
):
    construir_indice_sinonimos_omw()

    hipoteses = hipoteses.copy()
    referencias = referencias.copy()

    matches = []
    pares_omw = []

    for i in range(
        len(hipoteses) - 1,
        -1,
        -1
    ):

        palavra_hipotese = (
            hipoteses[i][1]
        )

        stem_hipotese = obter_stem(
            palavra_hipotese
        )

        sinonimos = (
            INDICE_SINONIMOS_OMW.get(
                stem_hipotese,
                set()
            )
        )

        if not sinonimos:
            continue

        for j in range(
            len(referencias) - 1,
            -1,
            -1
        ):

            palavra_referencia = (
                referencias[j][1]
            )

            stem_referencia = obter_stem(
                palavra_referencia
            )

            if (
                stem_referencia
                in sinonimos
            ):

                matches.append(
                    (
                        hipoteses[i][0],
                        referencias[j][0]
                    )
                )

                pares_omw.append(
                    (
                        palavra_hipotese,
                        palavra_referencia
                    )
                )

                hipoteses.pop(i)
                referencias.pop(j)

                break

    return (
        matches,
        hipoteses,
        referencias,
        pares_omw
    )


def alinhar_palavras_meteor(
    referencia_tokens,
    gerado_tokens
):
    hipoteses = list(
        enumerate(
            gerado_tokens
        )
    )

    referencias = list(
        enumerate(
            referencia_tokens
        )
    )

    (
        matches_exatos,
        hipoteses,
        referencias
    ) = alinhar_exatos(
        hipoteses,
        referencias
    )

    (
        matches_stem,
        hipoteses,
        referencias
    ) = alinhar_stems(
        hipoteses,
        referencias
    )

    (
        matches_omw,
        hipoteses,
        referencias,
        pares_omw
    ) = alinhar_sinonimos_omw(
        hipoteses,
        referencias
    )

    matches = sorted(
        (
            matches_exatos
            + matches_stem
            + matches_omw
        ),
        key=lambda par: par[0]
    )

    detalhes = {
        "qtd_matches_exatos":
            len(matches_exatos),

        "qtd_matches_stem":
            len(matches_stem),

        "qtd_matches_omw":
            len(matches_omw),

        "pares_omw":
            pares_omw,
    }

    return (
        matches,
        detalhes
    )


def contar_chunks(matches) -> int:

    if not matches:
        return 0

    chunks = 1

    for i in range(
        len(matches) - 1
    ):

        atual = matches[i]
        seguinte = matches[i + 1]

        consecutivos = (
            seguinte[0]
            == atual[0] + 1

            and

            seguinte[1]
            == atual[1] + 1
        )

        if not consecutivos:
            chunks += 1

    return chunks


def calcular_meteor(
    referencia: str,
    gerado: str
):
    """
    METEOR-PT:
    exact match + stemming português + OMW.
    """

    referencia_tokens = tokenizar_portugues(
        referencia
    )

    gerado_tokens = tokenizar_portugues(
        gerado
    )

    tamanho_referencia = len(
        referencia_tokens
    )

    tamanho_gerado = len(
        gerado_tokens
    )

    detalhes_vazios = {
        "qtd_matches_exatos": 0,
        "qtd_matches_stem": 0,
        "qtd_matches_omw": 0,
        "pares_omw": [],
    }

    if (
        tamanho_referencia == 0
        or
        tamanho_gerado == 0
    ):
        return (
            0.0,
            detalhes_vazios
        )

    matches, detalhes = (
        alinhar_palavras_meteor(
            referencia_tokens,
            gerado_tokens
        )
    )

    quantidade_matches = len(
        matches
    )

    if quantidade_matches == 0:
        return (
            0.0,
            detalhes
        )

    precisao = (
        quantidade_matches
        / tamanho_gerado
    )

    recall = (
        quantidade_matches
        / tamanho_referencia
    )

    denominador = (
        METEOR_ALPHA
        * precisao
        +
        (1 - METEOR_ALPHA)
        * recall
    )

    fmean = (
        precisao
        * recall
        / denominador
    )

    quantidade_chunks = contar_chunks(
        matches
    )

    fracao_fragmentacao = (
        quantidade_chunks
        / quantidade_matches
    )

    penalidade = (
        METEOR_GAMMA
        *
        (
            fracao_fragmentacao
            ** METEOR_BETA
        )
    )

    score = (
        (1 - penalidade)
        * fmean
    )

    return (
        score,
        detalhes
    )


def validar_integracao_omw():

    score, detalhes = calcular_meteor(
        "exibir",
        "mostrar"
    )

    if (
        detalhes[
            "qtd_matches_omw"
        ]
        == 0
    ):
        raise RuntimeError(
            "Falha na integração OMW."
        )

    return True