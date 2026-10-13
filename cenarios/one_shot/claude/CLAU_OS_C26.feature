# language: pt

Funcionalidade: Consultar status de uma transação

Cenário: Consultar status de uma transação de provisionamento de serviço
Dado que o solicitante possui uma transação de provisionamento de serviço em andamento
Quando o solicitante consulta o status da transação
Então o sistema apresenta o status atual da transação ao solicitante