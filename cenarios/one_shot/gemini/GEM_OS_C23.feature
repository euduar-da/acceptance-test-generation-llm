# language: pt

Funcionalidade: Remover usuário como proprietário
Cenário: Alterar permissão de um proprietário para membro
Dado que o proprietário possui um usuário cadastrado como proprietário
Quando o proprietário remove a permissão de proprietário do usuário
Então o sistema define o usuário como membro sem controle total