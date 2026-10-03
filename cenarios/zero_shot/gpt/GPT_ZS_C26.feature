# language: pt

Funcionalidade: Consultar o status de uma transação

Cenário: Consultar o status da transação para acompanhar o provisionamento do serviço
Dado que o Applicant possui uma transação de provisionamento de serviço
Quando o Applicant consulta o status da transação
Então o status da transação apresenta informações sobre o andamento do provisionamento do serviço