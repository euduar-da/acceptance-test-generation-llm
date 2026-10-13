import csv
import os
import re
import subprocess
from pathlib import Path



BASE_DIR = Path(__file__).resolve().parent

RAIZ_PROJETO = BASE_DIR.parent

PASTA_CENARIOS = RAIZ_PROJETO / "cenarios"


CONFIG_GHERKIN = BASE_DIR / ".gherkin-lintrc"

ARQUIVO_SAIDA = (
    BASE_DIR
    / "resultados"
    / "resultados_gherkin_lint.csv"
)


ANSI_ESCAPE = re.compile(
    r"\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])"
)

def remover_ansi(texto):
    """Remove códigos ANSI presentes na saída do gherkin-lint."""
    return ANSI_ESCAPE.sub("", texto)


def extrair_regras_violadas(mensagem):
    """
    Extrai nomes de regras do gherkin-lint presentes
    no final das linhas.

    Exemplos:
    no-multiline-steps
    keywords-in-logical-order
    """
    regras = []

    for linha in mensagem.splitlines():
        linha = linha.strip()

        correspondencia = re.search(
            r"\b([a-z][a-z0-9]*(?:-[a-z0-9]+)+)\s*$",
            linha
        )

        if correspondencia:
            regra = correspondencia.group(1)

            if regra not in regras:
                regras.append(regra)

    return "; ".join(regras)


def validar_estrutura_prompt(arquivo):
    """
    Verifica se o arquivo possui exatamente:
    - 1 Dado
    - 1 Quando
    - 1 Então
    - 0 E
    - 0 Mas

    Essa verificação complementa o gherkin-lint e valida
    especificamente a estrutura exigida no prompt do experimento.
    """

    conteudo = arquivo.read_text(
        encoding="utf-8-sig"
    )

    quantidade_dado = len(
        re.findall(
            r"^\s*Dado\b",
            conteudo,
            flags=re.MULTILINE
        )
    )

    quantidade_quando = len(
        re.findall(
            r"^\s*Quando\b",
            conteudo,
            flags=re.MULTILINE
        )
    )

    quantidade_entao = len(
        re.findall(
            r"^\s*Então\b",
            conteudo,
            flags=re.MULTILINE
        )
    )

    quantidade_e = len(
        re.findall(
            r"^\s*E\b",
            conteudo,
            flags=re.MULTILINE
        )
    )

    quantidade_mas = len(
        re.findall(
            r"^\s*Mas\b",
            conteudo,
            flags=re.MULTILINE
        )
    )

    aprovado = (
        quantidade_dado == 1
        and quantidade_quando == 1
        and quantidade_entao == 1
        and quantidade_e == 0
        and quantidade_mas == 0
    )

    erros = []

    if quantidade_dado != 1:
        erros.append(
            f"Esperado 1 Dado; encontrado {quantidade_dado}"
        )

    if quantidade_quando != 1:
        erros.append(
            f"Esperado 1 Quando; encontrado {quantidade_quando}"
        )

    if quantidade_entao != 1:
        erros.append(
            f"Esperado 1 Então; encontrado {quantidade_entao}"
        )

    if quantidade_e != 0:
        erros.append(
            f"Esperado 0 E; encontrado {quantidade_e}"
        )

    if quantidade_mas != 0:
        erros.append(
            f"Esperado 0 Mas; encontrado {quantidade_mas}"
        )

    return {
        "estrutura_aprovada": aprovado,
        "quantidade_dado": quantidade_dado,
        "quantidade_quando": quantidade_quando,
        "quantidade_entao": quantidade_entao,
        "quantidade_e": quantidade_e,
        "quantidade_mas": quantidade_mas,
        "erros_estrutura": "; ".join(erros)
    }


def executar_gherkin_lint(arquivo):
    """
    Executa o gherkin-lint para um único arquivo .feature,
    usando explicitamente o arquivo .gherkin-lintrc localizado
    dentro da pasta metricas.
    """

    ambiente = os.environ.copy()
    ambiente["FORCE_COLOR"] = "0"
    ambiente["NO_COLOR"] = "1"

    comando_npx = (
        "npx.cmd"
        if os.name == "nt"
        else "npx"
    )

    try:
        resultado = subprocess.run(
            [
                comando_npx,
                "gherkin-lint",
                "-c",
                str(CONFIG_GHERKIN),
                str(arquivo)
            ],
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="replace",
            env=ambiente,
            cwd=BASE_DIR
        )

    except FileNotFoundError:
        return {
            "aprovado": False,
            "codigo_saida": -1,
            "regras_violadas": "",
            "mensagem_lint": (
                "Não foi possível encontrar o comando npx. "
                "Verifique se o Node.js e o npm estão instalados."
            )
        }

    stdout = remover_ansi(
        resultado.stdout.strip()
    )

    stderr = remover_ansi(
        resultado.stderr.strip()
    )

    partes_mensagem = []

    if stdout:
        partes_mensagem.append(stdout)

    if stderr:
        partes_mensagem.append(stderr)

    mensagem_lint = "\n".join(
        partes_mensagem
    )

    aprovado = (
        resultado.returncode == 0
    )

    regras_violadas = (
        extrair_regras_violadas(
            mensagem_lint
        )
    )

    return {
        "aprovado": aprovado,
        "codigo_saida": resultado.returncode,
        "regras_violadas": regras_violadas,
        "mensagem_lint": mensagem_lint
    }


# ============================================================
# EXECUÇÃO PRINCIPAL
# ============================================================

def main():
    resultados = []

    # Confere se a pasta de cenários existe.
    if not PASTA_CENARIOS.exists():
        print(
            "ERRO: a pasta de cenários não foi encontrada:"
        )
        print(PASTA_CENARIOS)
        return

    # Confere se o arquivo .gherkin-lintrc existe.
    if not CONFIG_GHERKIN.exists():
        print(
            "ERRO: o arquivo .gherkin-lintrc "
            "não foi encontrado:"
        )
        print(CONFIG_GHERKIN)
        return

    # Busca todos os arquivos .feature em cenarios/
    # e em todas as suas subpastas.
    arquivos = sorted(
        PASTA_CENARIOS.rglob("*.feature")
    )

    if not arquivos:
        print(
            "Nenhum arquivo .feature encontrado em:"
        )
        print(PASTA_CENARIOS)
        return

    print(
        f"\nArquivos encontrados: "
        f"{len(arquivos)}\n"
    )

    for indice, arquivo in enumerate(
        arquivos,
        start=1
    ):
        resultado = executar_gherkin_lint(
            arquivo
        )

        estrutura = validar_estrutura_prompt(
            arquivo
        )

        caminho_relativo = (
            arquivo.relative_to(
                PASTA_CENARIOS
            )
        )

        # Estrutura esperada:
        # cenarios/
        #   zero-shot/
        #       gpt/
        #           GPT_ZS_C01.feature
        #
        # parts[0] -> técnica
        # parts[1] -> modelo
        partes = caminho_relativo.parts

        tecnica_prompt = (
            partes[0]
            if len(partes) >= 2
            else ""
        )

        modelo = (
            partes[1]
            if len(partes) >= 3
            else arquivo.parent.name
        )

        criterio_id = arquivo.stem

        aprovado_geral = (
            resultado["aprovado"]
            and estrutura["estrutura_aprovada"]
        )

        resultados.append({
            "criterio_id": criterio_id,
            "tecnica_prompt": tecnica_prompt,
            "modelo": modelo,
            "arquivo": str(caminho_relativo),

            "gherkin_lint_aprovado": resultado["aprovado"],
            "codigo_saida": resultado["codigo_saida"],
            "regras_violadas": resultado["regras_violadas"],
            "mensagem_lint": resultado["mensagem_lint"],

            "estrutura_prompt_aprovada": estrutura["estrutura_aprovada"],
            "quantidade_dado": estrutura["quantidade_dado"],
            "quantidade_quando": estrutura["quantidade_quando"],
            "quantidade_entao": estrutura["quantidade_entao"],
            "quantidade_e": estrutura["quantidade_e"],
            "quantidade_mas": estrutura["quantidade_mas"],
            "erros_estrutura": estrutura["erros_estrutura"],

            "aprovado_geral": aprovado_geral
        })

        status_lint = (
            "APROVADO"
            if resultado["aprovado"]
            else "REPROVADO"
        )

        status_estrutura = (
            "APROVADO"
            if estrutura["estrutura_aprovada"]
            else "REPROVADO"
        )

        status_geral = (
            "APROVADO"
            if aprovado_geral
            else "REPROVADO"
        )

        print(
            f"[{indice}/{len(arquivos)}] "
            f"{criterio_id} | "
            f"{tecnica_prompt} | "
            f"{modelo} | "
            f"Lint: {status_lint} | "
            f"Estrutura: {status_estrutura} | "
            f"Geral: {status_geral}"
        )

        if not resultado["aprovado"]:
            if resultado["regras_violadas"]:
                print(
                    "    Regras violadas: "
                    f"{resultado['regras_violadas']}"
                )

            elif resultado["mensagem_lint"]:
                print(
                    "    Mensagem do linter: "
                    f"{resultado['mensagem_lint']}"
                )

        if not estrutura["estrutura_aprovada"]:
            print(
                "    Estrutura: "
                f"{estrutura['erros_estrutura']}"
            )

    # Cria a pasta resultados/ caso ainda não exista.
    ARQUIVO_SAIDA.parent.mkdir(
        parents=True,
        exist_ok=True
    )

    campos = [
        "criterio_id",
        "tecnica_prompt",
        "modelo",
        "arquivo",

        "gherkin_lint_aprovado",
        "codigo_saida",
        "regras_violadas",
        "mensagem_lint",

        "estrutura_prompt_aprovada",
        "quantidade_dado",
        "quantidade_quando",
        "quantidade_entao",
        "quantidade_e",
        "quantidade_mas",
        "erros_estrutura",

        "aprovado_geral"
    ]

    with open(
        ARQUIVO_SAIDA,
        "w",
        newline="",
        encoding="utf-8-sig"
    ) as csvfile:
        writer = csv.DictWriter(
            csvfile,
            fieldnames=campos
        )

        writer.writeheader()
        writer.writerows(resultados)

    total = len(resultados)

    aprovados_lint = sum(
        1
        for item in resultados
        if item["gherkin_lint_aprovado"]
    )

    reprovados_lint = (
        total - aprovados_lint
    )

    aprovados_estrutura = sum(
        1
        for item in resultados
        if item["estrutura_prompt_aprovada"]
    )

    reprovados_estrutura = (
        total - aprovados_estrutura
    )

    aprovados_geral = sum(
        1
        for item in resultados
        if item["aprovado_geral"]
    )

    reprovados_geral = (
        total - aprovados_geral
    )

    print("\n--- Resultado geral ---")

    print(
        f"Cenários avaliados: {total}"
    )

    print("\nGherkin Lint:")
    print(
        f"Aprovados: {aprovados_lint}"
    )
    print(
        f"Reprovados: {reprovados_lint}"
    )

    print("\nEstrutura do prompt:")
    print(
        f"Aprovados: {aprovados_estrutura}"
    )
    print(
        f"Reprovados: {reprovados_estrutura}"
    )

    print("\nResultado combinado:")
    print(
        f"Aprovados: {aprovados_geral}"
    )
    print(
        f"Reprovados: {reprovados_geral}"
    )

    print(
        "\nResultados salvos em:"
    )
    print(ARQUIVO_SAIDA)


if __name__ == "__main__":
    main()
