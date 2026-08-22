import csv
import os
import re
import subprocess
from pathlib import Path


PASTA_CENARIOS = Path("cenarios")
ARQUIVO_SAIDA = Path("resultados/resultados_gherkin_lint.csv")


ANSI_ESCAPE = re.compile(r"\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])")


def remover_ansi(texto):
    """Remove códigos ANSI presentes na saída do gherkin-lint."""
    return ANSI_ESCAPE.sub("", texto)


def extrair_regras_violadas(mensagem):
    """
    Extrai nomes de regras do gherkin-lint presentes no final das linhas.

    Exemplo:
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


def executar_gherkin_lint(arquivo):
    """
    Executa o gherkin-lint para um único arquivo .feature.
    """

    ambiente = os.environ.copy()
    ambiente["FORCE_COLOR"] = "0"
    ambiente["NO_COLOR"] = "1"

    comando_npx = "npx.cmd" if os.name == "nt" else "npx"

    resultado = subprocess.run(
        [
            comando_npx,
            "gherkin-lint",
            str(arquivo)
        ],
        capture_output=True,
        text=True,
        env=ambiente
    )

    # Remove os códigos ANSI
    stdout = remover_ansi(resultado.stdout.strip())
    stderr = remover_ansi(resultado.stderr.strip())

    partes_mensagem = []

    if stdout:
        partes_mensagem.append(stdout)

    if stderr:
        partes_mensagem.append(stderr)

    mensagem_lint = "\n".join(partes_mensagem)

    # Código 0 = aprovado
    aprovado = resultado.returncode == 0

    # Identifica as regras que causaram a reprovação
    regras_violadas = extrair_regras_violadas(mensagem_lint)

    return {
        "aprovado": aprovado,
        "codigo_saida": resultado.returncode,
        "regras_violadas": regras_violadas,
        "mensagem_lint": mensagem_lint
    }


def main():
    resultados = []

    # Busca todos os arquivos .feature dentro de cenarios/
    arquivos = sorted(PASTA_CENARIOS.rglob("*.feature"))

    if not arquivos:
        print("Nenhum arquivo .feature encontrado.")
        return

    print(f"\nArquivos encontrados: {len(arquivos)}\n")

    for indice, arquivo in enumerate(arquivos, start=1):

        resultado = executar_gherkin_lint(arquivo)

      
        modelo = arquivo.parent.name
        criterio_id = arquivo.stem

        resultados.append({
            "criterio_id": criterio_id,
            "modelo": modelo,
            "arquivo": str(arquivo),
            "aprovado": resultado["aprovado"],
            "codigo_saida": resultado["codigo_saida"],
            "regras_violadas": resultado["regras_violadas"],
            "mensagem_lint": resultado["mensagem_lint"]
        })

        status = (
            "APROVADO"
            if resultado["aprovado"]
            else "REPROVADO"
        )

        print(
            f"[{indice}/{len(arquivos)}] "
            f"{criterio_id} | {modelo} | {status}"
        )

        if not resultado["aprovado"]:
            if resultado["regras_violadas"]:
                print(
                    f"    Regras violadas: "
                    f"{resultado['regras_violadas']}"
                )

    ARQUIVO_SAIDA.parent.mkdir(
        parents=True,
        exist_ok=True
    )

    with open(
        ARQUIVO_SAIDA,
        "w",
        newline="",
        encoding="utf-8-sig"
    ) as csvfile:

        campos = [
            "criterio_id",
            "modelo",
            "arquivo",
            "aprovado",
            "codigo_saida",
            "regras_violadas",
            "mensagem_lint"
        ]

        writer = csv.DictWriter(
            csvfile,
            fieldnames=campos
        )

        writer.writeheader()
        writer.writerows(resultados)

    total = len(resultados)

    aprovados = sum(
        1
        for resultado in resultados
        if resultado["aprovado"]
    )

    reprovados = total - aprovados

    print("\n--- Resultado geral ---")
    print(f"Cenários avaliados: {total}")
    print(f"Aprovados: {aprovados}")
    print(f"Reprovados: {reprovados}")
    

    print(
        f"\nResultados salvos em: "
        f"{ARQUIVO_SAIDA}"
    )


if __name__ == "__main__":
    main()