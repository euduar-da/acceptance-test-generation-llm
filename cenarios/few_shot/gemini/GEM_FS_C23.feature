# language: pt

Funcionalidade: Remover usuário da função de proprietário

Cenário: Alterar função do usuário de proprietário para membro
Dado que o proprietário possui um usuário cadastrado como proprietário
Quando o proprietário remove o usuário da função de proprietário
Então o sistema define o usuário como membro sem controle total