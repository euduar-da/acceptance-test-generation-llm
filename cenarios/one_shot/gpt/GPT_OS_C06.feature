# language: pt

Funcionalidade: Receber erro mais útil ao enviar arquivo com extensão incorreta

Cenário: Receber erro mais útil ao enviar arquivo com extensão incorreta
Dado que o usuário da agência possui um arquivo com extensão incorreta
Quando o usuário da agência envia o arquivo
Então o sistema apresenta um erro mais útil relacionado à extensão do arquivo