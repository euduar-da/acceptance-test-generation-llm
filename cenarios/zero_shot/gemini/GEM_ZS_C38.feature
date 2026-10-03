# language: pt

Funcionalidade: Envio de arquivos grandes

Cenário: Enviar um arquivo com tamanho superior a 1GB com sucesso
Dado que o usuário está pronto para enviar um arquivo
Quando o usuário envia um arquivo com tamanho superior a 1GB
Então o arquivo com tamanho superior a 1GB é enviado com sucesso
