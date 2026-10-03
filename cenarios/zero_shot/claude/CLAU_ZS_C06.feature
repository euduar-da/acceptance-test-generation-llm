# language: pt

Funcionalidade: Exibição de mensagem de erro detalhada ao enviar arquivo com extensão inválida

Cenário: Usuário da Agência recebe mensagem de erro detalhada ao enviar arquivo com extensão não suportada
Dado que o usuário da Agência está na tela de envio de arquivo
Quando ele envia um arquivo com uma extensão não suportada
Então o sistema exibe uma mensagem de erro detalhada informando o problema no arquivo