# language: pt

Funcionalidade: Remover usuário como proprietário

Cenário: Remover um usuário da condição de proprietário
Dado que o usuário é proprietário
Quando o proprietário remove o usuário como proprietário
Então o usuário passa a ser membro e deixa de ter controle total