# language: pt

Funcionalidade: Aceitar valores zero e em branco para registros de empréstimo na validação FABS

Cenário: Validar registro de empréstimo com valor zero ou em branco
Dado que o usuário da agência possui um registro de empréstimo com valor zero ou em branco
Quando o usuário da agência submete o registro para validação FABS
Então o sistema aceita o registro de empréstimo como válido