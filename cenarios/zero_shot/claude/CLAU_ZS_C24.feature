# language: pt

Funcionalidade: Aplicar retenção para impedir a progressão no fluxo de trabalho

Cenário: Membro da equipe aplica uma retenção para impedir ações no sistema
Dado que o membro da equipe está visualizando um item com uma questão não resolvida
Quando ele aplica uma retenção sobre esse item
Então a progressão pelo fluxo de trabalho e outras ações sobre o item ficam impedidas até que a questão seja resolvida