# language: pt

Funcionalidade: Aceitar valor zero e em branco para registros de empréstimo nas regras de validação FABS

Cenário: Validar registro de empréstimo com valor zero ou em branco
Dado que o usuário da agência possui um registro de empréstimo com valor zero ou em branco
Quando as regras de validação FABS processam o registro de empréstimo
Então as regras de validação FABS aceitam o registro de empréstimo