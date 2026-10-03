# language: pt

Funcionalidade: Aplicar bloqueio

Cenário: Aplicar bloqueio para impedir progressão no fluxo de trabalho
Dado que o funcionário identifica uma questão pendente de resolução
Quando o funcionário aplica um bloqueio
Então o sistema impede a progressão no fluxo de trabalho até que a questão seja resolvida