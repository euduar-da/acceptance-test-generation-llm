# language: pt

Funcionalidade: Download de múltiplos arquivos a partir dos resultados de busca

Cenário: Baixar múltiplos arquivos dos resultados de busca de uma só vez
Dado que o usuário está na página de resultados de busca com múltiplos arquivos selecionados
Quando o usuário solicita o download dos arquivos selecionados
Então o sistema realiza o download de todos os arquivos selecionados de uma só vez