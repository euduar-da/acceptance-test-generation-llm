# language: pt

Funcionalidade: Receber erro no nível de arquivo ao enviar arquivo com extensão incorreta

Cenário: Enviar arquivo com extensão incorreta
Dado que o usuário da agência possui um arquivo com extensão incorreta para envio
Quando o usuário da agência envia o arquivo com a extensão incorreta
Então o sistema apresenta uma mensagem de erro no nível de arquivo mais útil