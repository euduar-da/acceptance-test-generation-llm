# language: pt

Funcionalidade: Verificação do status de uma transação

Cenário: Consultar o status do provisionamento do serviço
Dado que o Solicitante possui uma transação em andamento
Quando o Solicitante consulta o status da transação
Então o sistema exibe as informações relativas ao processo de provisionamento do serviço
