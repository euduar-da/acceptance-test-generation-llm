"""
Cálculo da Acurácia de Validação dos arquivos Gherkin.

A métrica utiliza os resultados previamente obtidos
pelo Gherkin Lint.

Acurácia de Validação =
    arquivos aprovados pelo Gherkin Lint
    ------------------------------------
    total de arquivos .feature avaliados
"""

import csv
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent

ARQUIVO_RESULTADOS_LINT = (
    BASE_DIR
    / "resultados"
    / "resultados_gherkin_lint.csv"
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
                "gherkin_lint_aprovado"
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


def main():

    (
        acuracia,
        aprovados,
        reprovados,
        total
    ) = calcular_acuracia_validacao()

    print(
        "\n--- Acurácia de Validação ---"
    )

    print(
        f"Total de arquivos avaliados: "
        f"{total}"
    )

    print(
        f"Arquivos aprovados pelo "
        f"Gherkin Lint: {aprovados}"
    )

    print(
        f"Arquivos reprovados pelo "
        f"Gherkin Lint: {reprovados}"
    )

    print(
        f"Acurácia: "
        f"{acuracia:.4f}"
    )

    print(
        f"Acurácia (%): "
        f"{acuracia * 100:.2f}%"
    )


if __name__ == "__main__":
    main()