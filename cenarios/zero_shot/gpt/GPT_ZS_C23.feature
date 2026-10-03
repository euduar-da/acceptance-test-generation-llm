# language: pt

Funcionalidade: Remover um usuário como proprietário

Cenário: Usuário proprietário é removido como proprietário
Dado que o usuário é um proprietário
Quando o proprietário remove o usuário como proprietário
Então o usuário passa a ser apenas membro e não possui mais controle total