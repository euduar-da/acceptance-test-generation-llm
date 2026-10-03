# language: pt

Funcionalidade: Aceitação de valores zero e em branco nas regras de validação FABS para registros de empréstimo

Cenário: Registro de empréstimo com valor zero ou em branco é aceito pela validação
Dado que o usuário da agência possui um registro de empréstimo com valor zero ou em branco
Quando o registro de empréstimo é submetido às regras de validação FABS
Então o registro de empréstimo é aceito sem erro de validação