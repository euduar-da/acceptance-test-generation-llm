
# language: pt

Funcionalidade: Validação de registros de empréstimo nas regras FABS

Cenário: Validar registro de empréstimo com valor zero ou em branco
Dado que o usuário da agência possui um registro de empréstimo com valor zero ou em branco
Quando as regras de validação FABS são executadas no registro de empréstimo
Então as regras de validação FABS aceitam o registro de empréstimo