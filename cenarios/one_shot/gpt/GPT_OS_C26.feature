# language: pt

Funcionalidade: Consultar status de uma transação

Cenário: Consultar o status do provisionamento do serviço
Dado que o solicitante possui uma transação em processo de provisionamento do serviço
Quando o solicitante consulta o status da transação
Então o sistema apresenta informações sobre o andamento do provisionamento do serviço