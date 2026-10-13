# language: pt

Funcionalidade: Receber alerta de arquivos não vinculados no espaço de trabalho

Cenário: Alertar sobre arquivos não vinculados existentes no espaço de trabalho
Dado que existem arquivos não vinculados no espaço de trabalho do pesquisador
Quando o sistema verifica o espaço de trabalho do pesquisador
Então o sistema exibe um alerta ao pesquisador sobre os arquivos não vinculados