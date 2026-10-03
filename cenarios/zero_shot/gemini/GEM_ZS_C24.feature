# language: pt

Funcionalidade: Aplicar uma retenção no sistema

Cenário: Aplicar retenção para impedir o avanço no fluxo de trabalho
Dado que um membro da equipe precisa prevenir ações no sistema devido a uma pendência
Quando o membro da equipe aplica uma retenção
Então o sistema impede o avanço no fluxo de trabalho e a realização de outras ações até que a pendência seja resolvida
