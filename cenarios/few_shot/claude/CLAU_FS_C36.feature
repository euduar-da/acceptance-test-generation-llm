# language: pt

Funcionalidade: Receber alerta de arquivos não anexados

Cenário: Receber alerta de arquivos não anexados no espaço de trabalho
Dado que o pesquisador possui arquivos não anexados em seu espaço de trabalho
Quando o sistema verifica o espaço de trabalho do pesquisador
Então o sistema envia ao pesquisador um alerta sobre os arquivos não anexados