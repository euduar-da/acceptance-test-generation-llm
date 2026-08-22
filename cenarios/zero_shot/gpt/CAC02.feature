# language: pt

Funcionalidade: Exibir flexfields nos arquivos de aviso e erro

Cenário: Exibir flexfields quando faltar um elemento obrigatório
Dado que o arquivo de submissão possui flexfields e apenas um elemento obrigatório ausente
Quando o usuário submete o arquivo
Então os flexfields aparecem nos arquivos de aviso e erro
