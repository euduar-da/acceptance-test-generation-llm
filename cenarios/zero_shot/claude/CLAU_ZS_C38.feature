# language: pt

Funcionalidade: Upload de arquivos grandes

Cenário: Usuário realiza upload de um arquivo com mais de 1GB
Dado que o usuário possui um arquivo com tamanho superior a 1GB
Quando o usuário realiza o upload do arquivo
Então o arquivo é carregado com sucesso