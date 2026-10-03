# language: pt

Funcionalidade: Desativar o botão de publicação durante o processamento de derivações

Cenário: Desativar o botão de publicação após o clique durante as derivações
Dado que o usuário está realizando uma submissão no FABS
Quando o usuário clica no botão de publicação durante o processamento das derivações
Então o sistema desativa o botão de publicação para impedir múltiplos cliques na mesma submissão