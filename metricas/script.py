from pathlib import Path
import csv
import re


# ============================================================
# CAMINHOS DO PROJETO
# ============================================================

ROOT_DIR = Path(__file__).resolve().parent.parent

REFERENCE_DIR = (
    ROOT_DIR
    / "dataset"
    / "reference_base_scenarios"
)

SCENARIOS_DIR = (
    ROOT_DIR
    / "cenarios"
)

OUTPUT_DIR = (
    ROOT_DIR
    / "metricas"
    / "csv_entrada"
)


# ============================================================
# MAPEAMENTOS
# ============================================================

MODELOS = {
    "CLAU": "claude",
    "GEM": "gemini",
    "GPT": "chatgpt",
}

PROMPTS = {
    "ZS": "zero-shot",
    "OS": "one-shot",
    "FS": "few-shot",
}


# ============================================================
# IDENTIFICAÇÃO DO CENÁRIO
# ============================================================

def extrair_id_cenario(nome_arquivo: str):
    """
    Extrai C01, C02, ..., C45.

    Exemplos:
    CLAU_FS_C01.feature -> C01
    GEM_OS_C15.feature  -> C15
    GPT_ZS_C45.feature  -> C45
    REF_C01.feature     -> C01
    """

    resultado = re.search(
        r"(?:^|[_-])C(\d+)",
        nome_arquivo,
        re.IGNORECASE,
    )

    if resultado is None:
        resultado = re.search(
            r"scenario[_-]?(\d+)",
            nome_arquivo,
            re.IGNORECASE,
        )

    if resultado is None:
        return None

    numero = int(resultado.group(1))

    return f"C{numero:02d}"


# ============================================================
# IDENTIFICAÇÃO DO MODELO E PROMPT
# ============================================================

def identificar_arquivo_gerado(nome_arquivo: str):
    """
    Identifica modelo, técnica e cenário pelo nome.

    Exemplo:

    CLAU_FS_C01.feature

    retorna:

    ("claude", "few-shot", "C01")
    """

    nome = Path(nome_arquivo).stem.upper()

    padrao = re.match(
        r"(CLAU|GEM|GPT)_(ZS|OS|FS)_C(\d+)$",
        nome,
    )

    if padrao is None:
        return None

    sigla_modelo = padrao.group(1)
    sigla_prompt = padrao.group(2)
    numero = int(padrao.group(3))

    modelo = MODELOS[sigla_modelo]
    prompt = PROMPTS[sigla_prompt]
    cenario = f"C{numero:02d}"

    return modelo, prompt, cenario


# ============================================================
# LEITURA
# ============================================================

def ler_feature(caminho: Path):
    return caminho.read_text(
        encoding="utf-8"
    ).strip()

def limpar_comentarios_gherkin(texto: str):
    """
    Remove linhas de comentário/metadados do Gherkin.

    Exemplos removidos:
    # language: pt
    # g03-loudoun
    # qualquer outro comentário
    """

    linhas = []

    for linha in texto.splitlines():

        if linha.strip().startswith("#"):
            continue

        linhas.append(linha)

    return "\n".join(linhas).strip()


# ============================================================
# REFERÊNCIAS
# ============================================================

def carregar_referencias():

    referencias = {}

    for arquivo in REFERENCE_DIR.rglob("*.feature"):

        id_cenario = extrair_id_cenario(
            arquivo.name
        )

        if id_cenario is None:
            print(
                f"[AVISO] Referência sem ID: "
                f"{arquivo.name}"
            )
            continue

        if id_cenario in referencias:
            raise ValueError(
                f"Referência duplicada para "
                f"{id_cenario}: {arquivo}"
            )

        referencias[id_cenario] = arquivo

    return referencias


# ============================================================
# CARREGAR TODOS OS CENÁRIOS GERADOS
# ============================================================

def carregar_cenarios_gerados():

    grupos = {}

    arquivos = list(
        SCENARIOS_DIR.rglob("*.feature")
    )

    print(
        f"{len(arquivos)} arquivos .feature "
        f"gerados encontrados."
    )

    for arquivo in arquivos:

        identificacao = identificar_arquivo_gerado(
            arquivo.name
        )

        if identificacao is None:
            print(
                f"[AVISO] Nome não reconhecido: "
                f"{arquivo.name}"
            )
            continue

        modelo, prompt, cenario = identificacao

        chave = (
            modelo,
            prompt,
        )

        if chave not in grupos:
            grupos[chave] = []

        grupos[chave].append(
            {
                "cenario": cenario,
                "arquivo": arquivo,
            }
        )

    return grupos


# ============================================================
# GERAÇÃO DO CSV
# ============================================================

def gerar_csv(
    modelo,
    prompt,
    cenarios,
    referencias,
):

    linhas = []

    for item in cenarios:

        id_cenario = item["cenario"]
        arquivo_gerado = item["arquivo"]

        arquivo_referencia = referencias.get(
            id_cenario
        )

        if arquivo_referencia is None:
            print(
                f"[ERRO] Referência não encontrada "
                f"para {id_cenario}"
            )
            continue

        linhas.append(
            {
                "cenario": id_cenario,
                "modelo": modelo,
                "prompt": prompt,
                "arquivo_referencia":
                    arquivo_referencia.name,
                "arquivo_gerado":
                    arquivo_gerado.name,
                "referencia":
                    limpar_comentarios_gherkin(
                        ler_feature(
                            arquivo_referencia
                        )
                    ),
                "gerado":
                    limpar_comentarios_gherkin(
                        ler_feature(
                            arquivo_gerado
                        )
                    ),
            }
        )

    linhas.sort(
        key=lambda x: int(
            x["cenario"][1:]
        )
    )

    OUTPUT_DIR.mkdir(
        parents=True,
        exist_ok=True,
    )

    nome_saida = (
        f"{modelo}_{prompt}.csv"
    )

    caminho_saida = (
        OUTPUT_DIR
        / nome_saida
    )

    campos = [
        "cenario",
        "modelo",
        "prompt",
        "arquivo_referencia",
        "arquivo_gerado",
        "referencia",
        "gerado",
    ]

    with caminho_saida.open(
        "w",
        encoding="utf-8-sig",
        newline="",
    ) as arquivo_csv:

        writer = csv.DictWriter(
            arquivo_csv,
            fieldnames=campos,
            quoting=csv.QUOTE_ALL,
        )

        writer.writeheader()

        writer.writerows(
            linhas
        )

    print(
        f"[OK] {nome_saida}: "
        f"{len(linhas)} cenários pareados."
    )


# ============================================================
# EXECUÇÃO
# ============================================================

def main():

    print(
        "Carregando cenários de referência..."
    )

    referencias = carregar_referencias()

    print(
        f"{len(referencias)} referências "
        f"encontradas."
    )

    print()

    print(
        "Procurando cenários gerados..."
    )

    grupos = carregar_cenarios_gerados()

    print()

    for (
        modelo,
        prompt,
    ), cenarios in sorted(
        grupos.items()
    ):

        gerar_csv(
            modelo,
            prompt,
            cenarios,
            referencias,
        )


if __name__ == "__main__":
    main()