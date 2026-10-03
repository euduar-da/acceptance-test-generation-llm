# language: pt

Funcionalidade: Restauração de arquivos excluídos

Cenário: Restaurar um arquivo excluído acidentalmente
Dado que um usuário possui um arquivo na lixeira
Quando o usuário solicita a restauração do arquivo
Então o sistema restaura o arquivo para o seu estado original