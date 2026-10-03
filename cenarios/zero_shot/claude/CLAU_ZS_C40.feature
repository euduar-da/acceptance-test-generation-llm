# language: pt

Funcionalidade: Filtragem de arquivos por tipo nos resultados de busca

Cenário: Usuário filtra os resultados de busca por tipo de arquivo
Dado que o usuário possui resultados de busca contendo arquivos de diferentes tipos
Quando o usuário aplica um filtro por tipo de arquivo
Então o sistema exibe apenas os arquivos do tipo selecionado