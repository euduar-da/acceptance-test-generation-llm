# language: pt

Funcionalidade: Download do pacote de dados em um único arquivo

Cenário: Consumidor baixa o pacote de dados em um único arquivo
Dado que o consumidor possui um pacote de dados disponível com descritor e recursos
Quando o consumidor solicita o download do pacote de dados
Então o consumidor recebe um único arquivo contendo o descritor e todos os recursos do pacote de dados
