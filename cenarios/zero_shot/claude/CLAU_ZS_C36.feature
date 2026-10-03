# language: pt

Funcionalidade: Alerta de arquivos não anexados no workspace

Cenário: Pesquisador recebe alerta ao existir arquivo não anexado no workspace
Dado que o pesquisador possui um arquivo não anexado em seu workspace
Quando o sistema verifica os arquivos do workspace
Então o pesquisador recebe um alerta sobre o arquivo não anexado