# language: pt

Funcionalidade: Desativar o botão de publicação no FABS durante as derivações

Cenário: Impedir múltiplos cliques no botão de publicação para a mesma submissão
Dado que as derivações estão acontecendo após a submissão
Quando o usuário clica no botão de publicação
Então o botão de publicação fica desativado enquanto as derivações estão acontecendo