# language: pt

Funcionalidade: Receber erro ao enviar arquivo com extensão incorreta
Cenário: Enviar arquivo com extensão incorreta
Dado que o usuário da agência envia um arquivo com a extensão incorreta
Quando o usuário da agência faz o envio do arquivo
Então o sistema exibe uma mensagem de erro útil referente ao arquivo enviado