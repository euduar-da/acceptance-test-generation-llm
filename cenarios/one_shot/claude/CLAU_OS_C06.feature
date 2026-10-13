# language: pt

Funcionalidade: Exibir erro detalhado ao enviar arquivo com extensão inválida

Cenário: Enviar arquivo com extensão não suportada
Dado que o usuário da agência seleciona um arquivo com extensão inválida para envio
Quando o usuário da agência envia o arquivo
Então o sistema exibe um erro detalhado informando que a extensão do arquivo não é válida