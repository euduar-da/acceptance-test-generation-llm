"""
Execução das métricas de avaliação dos cenários Gherkin.

Métricas:
- METEOR-PT + Open Multilingual WordNet (OMW)
- BERTScore + BERTimbau

CSV de entrada esperado:
criterio_id,modelo,referencia,gerado
"""

from pathlib import Path

import nltk
import pandas as pd

from metricas.meteor_pt import (
    calcular_meteor,
    construir_indice_sinonimos_omw,
    validar_integracao_omw,
)

from metricas.bertscore_pt import (
    calcular_bertscore,
    MODEL_TYPE,
    NUM_LAYERS,
    MAX_LENGTH,
)


# ============================================================
# CONFIGURAÇÃO DOS ARQUIVOS
# ============================================================

ARQUIVO_ENTRADA = Path("cenarios.csv")

PASTA_RESULTADOS = Path("resultados")

ARQUIVO_RESULTADOS = (
    PASTA_RESULTADOS
    / "resultados_avaliacao.csv"
)

ARQUIVO_RESUMO = (
    PASTA_RESULTADOS
    / "resultados_avaliacao_resumo.csv"
)


# ============================================================
# RECURSOS NLTK
# ============================================================

def garantir_recursos_nltk():
    """
    Garante que os recursos necessários para
    tokenização e OMW estejam disponíveis.
    """

    recursos = [
        "punkt",
        "punkt_tab",
        "wordnet",
        "omw-1.4",
    ]

    for recurso in recursos:

        try:

            nltk.download(
                recurso,
                quiet=True
            )

        except Exception as erro:

            print(
                f"[AVISO] Não foi possível baixar "
                f"o recurso '{recurso}': {erro}"
            )


# ============================================================
# VALIDAÇÃO DAS LINHAS
# ============================================================

def linha_valida(
    referencia,
    gerado
) -> bool:
    """
    Verifica se referência e cenário gerado
    possuem conteúdo válido.
    """

    if (
        pd.isna(referencia)
        or
        pd.isna(gerado)
    ):
        return False

    return (
        str(referencia).strip() != ""
        and
        str(gerado).strip() != ""
    )


# ============================================================
# CARREGAMENTO DO CSV
# ============================================================

def carregar_csv(
    caminho: Path
) -> pd.DataFrame:
    """
    Carrega e valida o arquivo CSV.
    """

    df = pd.read_csv(
        caminho,
        encoding="utf-8-sig",
        sep=None,
        engine="python"
    )

    colunas_esperadas = {
        "criterio_id",
        "modelo",
        "referencia",
        "gerado",
    }

    if not colunas_esperadas.issubset(
        df.columns
    ):

        raise ValueError(
            "O CSV precisa conter as colunas: "
            "criterio_id, modelo, referencia, gerado.\n"
            f"Colunas encontradas: {list(df.columns)}"
        )

    total_original = len(df)

    mascara_valida = df.apply(
        lambda linha: linha_valida(
            linha["referencia"],
            linha["gerado"]
        ),
        axis=1
    )

    df = (
        df[mascara_valida]
        .reset_index(drop=True)
    )

    removidos = (
        total_original
        - len(df)
    )

    if removidos > 0:

        print(
            f"[AVISO] {removidos} linha(s) "
            f"inválida(s) foram ignoradas."
        )

    if df.empty:

        raise ValueError(
            "Nenhum par válido de cenários foi encontrado."
        )

    return df


# ============================================================
# EXECUÇÃO DO METEOR
# ============================================================

def executar_meteor(
    df: pd.DataFrame
) -> pd.DataFrame:
    """
    Calcula METEOR-PT + OMW para cada par
    de referência e cenário gerado.
    """

    print(
        "\nCalculando METEOR-PT + OMW..."
    )

    meteor_scores = []

    matches_exatos = []

    matches_stem = []

    matches_omw = []

    pares_omw = []


    total = len(df)


    for indice, linha in df.iterrows():

        score, detalhes = calcular_meteor(
            referencia=str(
                linha["referencia"]
            ),
            gerado=str(
                linha["gerado"]
            )
        )

        meteor_scores.append(
            score
        )

        matches_exatos.append(
            detalhes[
                "qtd_matches_exatos"
            ]
        )

        matches_stem.append(
            detalhes[
                "qtd_matches_stem"
            ]
        )

        matches_omw.append(
            detalhes[
                "qtd_matches_omw"
            ]
        )

        pares = " | ".join(
            f"{gerado} <-> {referencia}"

            for gerado, referencia

            in detalhes[
                "pares_omw"
            ]
        )

        pares_omw.append(
            pares
        )

        print(
            f"[METEOR {indice + 1}/{total}] "
            f"{linha['criterio_id']} - "
            f"{linha['modelo']} "
            f"= {score:.4f}"
        )


    df["meteor"] = (
        meteor_scores
    )

    df[
        "meteor_matches_exatos"
    ] = matches_exatos

    df[
        "meteor_matches_stem"
    ] = matches_stem

    df[
        "meteor_matches_omw"
    ] = matches_omw

    df[
        "meteor_pares_omw"
    ] = pares_omw

    df[
        "meteor_usou_omw"
    ] = (
        df[
            "meteor_matches_omw"
        ]
        > 0
    )

    return df


# ============================================================
# EXECUÇÃO DO BERTSCORE
# ============================================================

def executar_bertscore(
    df: pd.DataFrame
) -> pd.DataFrame:
    """
    Calcula BERTScore em lote utilizando
    o BERTimbau Base.
    """

    print(
        "\nCalculando BERTScore..."
    )

    print(
        f"Modelo: {MODEL_TYPE}"
    )

    print(
        f"Camada: {NUM_LAYERS}"
    )

    print(
        f"Max length: {MAX_LENGTH}\n"
    )


    referencias = (
        df["referencia"]
        .astype(str)
        .tolist()
    )

    gerados = (
        df["gerado"]
        .astype(str)
        .tolist()
    )


    (
        precision,
        recall,
        f1,
        hash_config
    ) = calcular_bertscore(

        referencias=referencias,

        gerados=gerados

    )


    df[
        "bertscore_precision"
    ] = precision

    df[
        "bertscore_recall"
    ] = recall

    df[
        "bertscore_f1"
    ] = f1

    df[
        "bertscore_hash"
    ] = hash_config


    return df


# ============================================================
# METADADOS
# ============================================================

def adicionar_metadados(
    df: pd.DataFrame
) -> pd.DataFrame:
    """
    Adiciona informações das configurações
    utilizadas nas métricas.
    """

    df[
        "meteor_config"
    ] = (
        "METEOR-PT+OMW;"
        "SnowballStemmer(portuguese);"
        "OMW(lang=por);"
        "alpha=0.9;"
        "beta=3.0;"
        "gamma=0.5"
    )

    df[
        "bertscore_model"
    ] = MODEL_TYPE

    df[
        "bertscore_num_layers"
    ] = NUM_LAYERS

    df[
        "bertscore_max_length"
    ] = MAX_LENGTH

    df[
        "nltk_version"
    ] = nltk.__version__

    return df


# ============================================================
# RESUMO POR MODELO
# ============================================================

def gerar_resumo(
    df: pd.DataFrame
) -> pd.DataFrame:
    """
    Calcula médias e desvios padrão
    das métricas por modelo.
    """

    resumo = (
        df.groupby(
            "modelo"
        )
        .agg(

            # Quantidade
            qtd_cenarios=(
                "criterio_id",
                "size"
            ),

            # METEOR
            meteor_media=(
                "meteor",
                "mean"
            ),

            meteor_desvio_padrao=(
                "meteor",
                "std"
            ),

            meteor_cenarios_com_omw=(
                "meteor_usou_omw",
                "sum"
            ),

            meteor_total_matches_omw=(
                "meteor_matches_omw",
                "sum"
            ),

            # BERTScore
            bertscore_precision_media=(
                "bertscore_precision",
                "mean"
            ),

            bertscore_recall_media=(
                "bertscore_recall",
                "mean"
            ),

            bertscore_f1_media=(
                "bertscore_f1",
                "mean"
            ),

            bertscore_f1_desvio_padrao=(
                "bertscore_f1",
                "std"
            ),

        )
    )


    resumo[
        "meteor_percentual_cenarios_com_omw"
    ] = (

        resumo[
            "meteor_cenarios_com_omw"
        ]

        / resumo[
            "qtd_cenarios"
        ]

        * 100
    )


    return resumo.round(4)


# ============================================================
# PROGRAMA PRINCIPAL
# ============================================================

def main():

    print(
        "=" * 80
    )

    print(
        "AVALIAÇÃO DE CENÁRIOS GHERKIN"
    )

    print(
        "METEOR-PT + OMW | BERTScore + BERTimbau"
    )

    print(
        "=" * 80
    )


    # ========================================================
    # PREPARAÇÃO
    # ========================================================

    PASTA_RESULTADOS.mkdir(
        parents=True,
        exist_ok=True
    )

    garantir_recursos_nltk()


    # ========================================================
    # VALIDAÇÃO DO OMW
    # ========================================================

    construir_indice_sinonimos_omw()

    if validar_integracao_omw():

        print(
            "Validação OMW concluída: "
            "'exibir' <-> 'mostrar' "
            "reconhecido corretamente.\n"
        )


    # ========================================================
    # CARREGA CSV
    # ========================================================

    df = carregar_csv(
        ARQUIVO_ENTRADA
    )

    print(
        f"Carregados {len(df)} pares válidos "
        f"para avaliação."
    )


    # ========================================================
    # METEOR
    # ========================================================

    df = executar_meteor(
        df
    )


    # ========================================================
    # BERTSCORE
    # ========================================================

    df = executar_bertscore(
        df
    )


    # ========================================================
    # METADADOS
    # ========================================================

    df = adicionar_metadados(
        df
    )


    # ========================================================
    # SALVA RESULTADO DETALHADO
    # ========================================================

    df.to_csv(
        ARQUIVO_RESULTADOS,
        index=False,
        encoding="utf-8-sig"
    )


    # ========================================================
    # RESUMO
    # ========================================================

    resumo = gerar_resumo(
        df
    )


    resumo.to_csv(
        ARQUIVO_RESUMO,
        encoding="utf-8-sig"
    )


    # ========================================================
    # RESULTADO NO TERMINAL
    # ========================================================

    print(
        "\n"
        + "=" * 100
    )

    print(
        "RESUMO POR MODELO"
    )

    print(
        "=" * 100
    )

    print(
        resumo.to_string()
    )

    print(
        "=" * 100
    )


    print(
        f"\nResultados detalhados:\n"
        f"{ARQUIVO_RESULTADOS}"
    )

    print(
        f"\nResumo:\n"
        f"{ARQUIVO_RESUMO}"
    )

    print(
        "\nAvaliação concluída com sucesso."
    )


# ============================================================
# EXECUÇÃO
# ============================================================

if __name__ == "__main__":

    try:

        main()

    except FileNotFoundError:

        print(
            f"\n[ERRO] O arquivo "
            f"'{ARQUIVO_ENTRADA}' "
            f"não foi encontrado."
        )

    except Exception as erro:

        print(
            f"\n[ERRO] Ocorreu um erro "
            f"durante a avaliação:\n"
            f"{erro}"
        )