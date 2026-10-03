# language: pt

Funcionalidade: Consultar status de uma transação

Cenário: Consultar status de uma transação
Dado que o requerente possui uma transação em andamento
Quando o requerente consulta o status da transação
Então o sistema apresenta o status da transação com as informações do processo de provisionamento do serviço
