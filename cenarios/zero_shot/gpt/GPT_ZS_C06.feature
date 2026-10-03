# language: pt

Funcionalidade: Receber um erro mais útil no nível do arquivo ao enviar um arquivo com extensão incorreta

Cenário: Receber um erro mais útil ao enviar um arquivo com extensão incorreta
Dado que o usuário da Agência possui um arquivo com extensão incorreta
Quando ele envia o arquivo
Então ele recebe um erro mais útil no nível do arquivo
