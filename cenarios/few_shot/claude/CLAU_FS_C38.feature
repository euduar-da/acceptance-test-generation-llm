# language: pt

Funcionalidade: Enviar arquivos de grande porte

Cenário: Enviar arquivo com tamanho superior a 1GB
Dado que o usuário possui um arquivo com tamanho superior a 1GB
Quando o usuário envia o arquivo
Então o sistema armazena o arquivo enviado