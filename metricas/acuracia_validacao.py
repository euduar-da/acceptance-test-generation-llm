"""
Cálculo da Acurácia de Validação dos arquivos Gherkin.

A métrica verifica se o conteúdo de cada arquivo .feature
é aceito sintaticamente pelo parser oficial do Gherkin.

Acurácia de Validação =
    arquivos válidos / total de arquivos
"""

from gherkin import Parser


def preparar_gherkin_portugues(
    conteudo: str
) -> str:
    """
    Garante que o parser utilize o dialeto português.

    O cabeçalho # language: pt é adicionado somente
    quando não estiver presente.
    """

    conteudo = str(
        conteudo
    ).strip()

    if not conteudo.startswith(
        "# language:"
    ):
        conteudo = (
            "# language: pt\n"
            + conteudo
        )

    return conteudo


def validar_sintaxe_gherkin(
    conteudo: str
):
    """
    Valida um arquivo Gherkin utilizando
    o parser oficial do Cucumber.

    Retorna:
        valido: bool
        erro: str | None
    """

    conteudo = preparar_gherkin_portugues(
        conteudo
    )

    try:

        Parser().parse(
            conteudo
        )

        return (
            True,
            None
        )

    except Exception as erro:

        return (
            False,
            str(erro)
        )


def calcular_acuracia_validacao(
    conteudos: list[str]
):
    """
    Calcula:

        arquivos sintaticamente válidos
        --------------------------------
        total de arquivos avaliados

    Retorna:
        acuracia,
        quantidade_validos,
        quantidade_invalidos,
        total
    """

    total = len(
        conteudos
    )

    if total == 0:
        return (
            0.0,
            0,
            0,
            0
        )

    quantidade_validos = 0

    for conteudo in conteudos:

        valido, _ = (
            validar_sintaxe_gherkin(
                conteudo
            )
        )

        if valido:
            quantidade_validos += 1

    quantidade_invalidos = (
        total
        - quantidade_validos
    )

    acuracia = (
        quantidade_validos
        / total
    )

    return (
        acuracia,
        quantidade_validos,
        quantidade_invalidos,
        total
    )