# language: pt

Funcionalidade: Enviar arquivos grandes com mais de 1GB de tamanho

Cenário: Enviar arquivo grande com mais de 1GB de tamanho
Dado que o usuário possui um arquivo com mais de 1GB de tamanho
Quando o usuário envia o arquivo com mais de 1GB de tamanho
Então o sistema realiza o envio do arquivo com sucesso