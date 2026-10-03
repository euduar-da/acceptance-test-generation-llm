# language: pt

Funcionalidade: Receber erro detalhado ao enviar arquivo com extensão incorreta

Cenário: Notificar envio de arquivo com extensão incorreta
Dado que o usuário da agência está na página de envio de arquivo
Quando ele envia um arquivo com a extensão incorreta
Então ele recebe uma mensagem de erro mais detalhada no nível do arquivo