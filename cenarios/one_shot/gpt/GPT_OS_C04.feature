# language: pt

Funcionalidade: Aceitar zero e em branco nas regras de validação FABS para registros de empréstimo

Cenário: Aceitar zero e em branco nas regras de validação FABS
Dado que o usuário da agência possui registros de empréstimo
Quando o usuário da agência aplica as regras de validação FABS aos registros de empréstimo com zero e em branco
Então as regras de validação FABS aceitam zero e em branco nos registros de empréstimo