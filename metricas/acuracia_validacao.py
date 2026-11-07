
"""
Cálculo da Acurácia de Validação dos arquivos Gherkin.

A métrica utiliza os resultados previamente obtidos
pelo Gherkin Lint.
"""

import csv
from pathlib import Path


# Diretório onde está este script
BASE_DIR = Path(__file__).resolve().parent


# CSV de entrada com os resultados do Gherkin Lint
ARQUIVO_RESULTADOS_LINT = (
    BASE_DIR
    / "resultados"
    / "resultados_gherkin_lint.csv"
)


# CSV de saída com a Acurácia de Validação
ARQUIVO_SAIDA_ACURACIA = (
    BASE_DIR
    / "resultados"
    / "resultados_acuracia_validacao.csv"
)


def converter_booleano(valor):
    """
    Converte o valor True/False armazenado
    no CSV para booleano do Python.
    """

    return (
        str(valor)
        .strip()
        .lower()
        == "true"
    )


def calcular_acuracia_validacao():
    """
    Calcula a Acurácia de Validação com base
    nos resultados do Gherkin Lint.

    Acurácia de Validação =
        número de arquivos aprovados pelo Gherkin Lint
        ------------------------------------------------
        número total de arquivos .feature avaliados

    Retorna:
        acuracia,
        quantidade_aprovados,
        quantidade_reprovados,
        total
    """

    if not ARQUIVO_RESULTADOS_LINT.exists():
        raise FileNotFoundError(
            "Arquivo de resultados do Gherkin Lint "
            f"não encontrado: {ARQUIVO_RESULTADOS_LINT}"
        )

    with open(
        ARQUIVO_RESULTADOS_LINT,
        "r",
        encoding="utf-8-sig",
        newline=""
    ) as arquivo:

        leitor = csv.DictReader(
            arquivo
        )

        resultados = list(
            leitor
        )

    total = len(
        resultados
    )

    if total == 0:
        return (
            0.0,
            0,
            0,
            0
        )

    quantidade_aprovados = sum(
        1
        for resultado in resultados
        if converter_booleano(
            resultado[
                "aprovado_geral"
            ]
        )
    )

    quantidade_reprovados = (
        total
        - quantidade_aprovados
    )

    acuracia = (
        quantidade_aprovados
        / total
    )

    return (
        acuracia,
        quantidade_aprovados,
        quantidade_reprovados,
        total
    )


def salvar_resultados_csv():
    """
    Gera um CSV com a Acurácia de Validação
    por modelo e técnica de prompting,
    incluindo o resultado geral.
    """

    with open(
        ARQUIVO_RESULTADOS_LINT,
        "r",
        encoding="utf-8-sig",
        newline=""
    ) as arquivo:
        resultados = list(csv.DictReader(arquivo))

    grupos = {}

    for resultado in resultados:

        modelo = resultado["modelo"]
        tecnica = resultado["tecnica_prompt"]

        chave = (modelo, tecnica)

        if chave not in grupos:
            grupos[chave] = {
                "total": 0,
                "aprovados": 0
            }

        grupos[chave]["total"] += 1

        if converter_booleano(
            resultado["aprovado_geral"]
        ):
            grupos[chave]["aprovados"] += 1

    campos = [
        "modelo",
        "tecnica_prompt",
        "total",
        "aprovados",
        "reprovados",
        "acuracia",
        "acuracia_percentual"
    ]

    ARQUIVO_SAIDA_ACURACIA.parent.mkdir(
        parents=True,
        exist_ok=True
    )

    total_geral = 0
    aprovados_geral = 0

    with open(
        ARQUIVO_SAIDA_ACURACIA,
        "w",
        encoding="utf-8-sig",
        newline=""
    ) as arquivo:

        writer = csv.DictWriter(
            arquivo,
            fieldnames=campos
        )

        writer.writeheader()

        for (modelo, tecnica), dados in sorted(
            grupos.items()
        ):

            total = dados["total"]
            aprovados = dados["aprovados"]
            reprovados = total - aprovados

            acuracia = (
                aprovados / total
                if total > 0 else 0.0
            )

            writer.writerow({
                "modelo": modelo,
                "tecnica_prompt": tecnica,
                "total": total,
                "aprovados": aprovados,
                "reprovados": reprovados,
                "acuracia": f"{acuracia:.6f}",
                "acuracia_percentual": f"{acuracia * 100:.2f}"
            })

            total_geral += total
            aprovados_geral += aprovados

        reprovados_geral = (
            total_geral - aprovados_geral
        )

        acuracia_geral = (
            aprovados_geral / total_geral
            if total_geral > 0 else 0.0
        )

        writer.writerow({
            "modelo": "TOTAL_GERAL",
            "tecnica_prompt": "todas",
            "total": total_geral,
            "aprovados": aprovados_geral,
            "reprovados": reprovados_geral,
            "acuracia": f"{acuracia_geral:.6f}",
            "acuracia_percentual": f"{acuracia_geral * 100:.2f}"
        })

    print(
        f"\nResultados da Acurácia de Validação salvos em:"
        f"\n{ARQUIVO_SAIDA_ACURACIA}"
    )


def main():

    (
        acuracia,
        aprovados,
        reprovados,
        total
    ) = calcular_acuracia_validacao()

    print("\n--- Acurácia de Validação ---")

    print(f"Total de arquivos avaliados: {total}")
    print(f"Arquivos aprovados: {aprovados}")
    print(f"Arquivos reprovados: {reprovados}")
    print(f"Acurácia: {acuracia:.4f}")
    print(f"Acurácia (%): {acuracia * 100:.2f}%")

    salvar_resultados_csv()


if __name__ == "__main__":
    main()