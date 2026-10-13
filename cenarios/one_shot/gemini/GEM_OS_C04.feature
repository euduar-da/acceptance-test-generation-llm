# language: pt

Funcionalidade: Validar registros de empréstimo nas regras do FABS
Cenário: Aceitar valor zero ou em branco para registros de empréstimo
Dado que o usuário da agência possui um registro de empréstimo com valor zero ou em branco
Quando o usuário da agência submete o registro de empréstimo para validação no FABS
Então as regras de validação do FABS aceitam o registro de empréstimo