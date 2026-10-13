# language: pt

Funcionalidade: Enviar arquivos com mais de 1GB de tamanho
Cenário: Enviar arquivo com tamanho superior a 1GB
Dado que o usuário possui um arquivo com mais de 1GB de tamanho
Quando o usuário envia o arquivo
Então o sistema aceita o envio do arquivo do usuário