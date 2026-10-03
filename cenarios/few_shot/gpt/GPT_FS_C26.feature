# language: pt

Funcionalidade: Consultar status de uma transação

Cenário: Consultar status da transação
Dado que o solicitante possui uma transação em processo de provisionamento do serviço
Quando o solicitante consulta o status da transação
Então o sistema apresenta o status do provisionamento do serviço, incluindo informações relacionadas a níveis de serviço, taxas, revisão do plano, autorização ou resultados de inspeção
