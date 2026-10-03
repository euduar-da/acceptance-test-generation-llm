# language: pt

Funcionalidade: Consultar status de transação

Cenário: Consultar status de transação de provisionamento de serviço
Dado que o requerente possui uma transação de provisionamento de serviço em andamento
Quando o requerente consulta o status da transação
Então o sistema apresenta o status atual da transação