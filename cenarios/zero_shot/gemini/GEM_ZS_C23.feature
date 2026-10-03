# language: pt

Funcionalidade: Remover a permissão de proprietário de um usuário

Cenário: Alterar a permissão de um usuário de proprietário para membro
Dado que um usuário possui o papel de proprietário
Quando o proprietário remove a permissão de proprietário desse usuário
Então o usuário torna-se um membro sem controle total