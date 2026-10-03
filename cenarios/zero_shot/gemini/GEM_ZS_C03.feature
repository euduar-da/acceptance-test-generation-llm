# language: pt

Funcionalidade: Desativação do botão publicar durante o processamento de derivações

Cenário: Desativar o botão publicar após o clique enquanto as derivações estão acontecendo
Dado que o usuário está no FABS com uma submissão pronta para publicação
Quando o usuário clica no botão publicar
Então o botão publicar no FABS é desativado enquanto as derivações estão acontecendo