# language: pt

Funcionalidade: Filtrar arquivos dos resultados de busca por tipo

Cenário: Filtrar os resultados de busca pelo tipo de arquivo
Dado que o usuário possui resultados de uma busca por arquivos
Quando o usuário filtra os resultados pelo tipo do arquivo
Então o sistema exibe apenas os arquivos correspondentes ao tipo selecionado
