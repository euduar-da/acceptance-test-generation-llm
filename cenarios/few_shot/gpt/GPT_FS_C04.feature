# language: pt

Funcionalidade: Aceitar zero e branco nas regras de validação FABS para registros de empréstimo

Cenário: Aceitar zero e branco nas regras de validação FABS para registros de empréstimo
Dado que o usuário da agência possui registros de empréstimo
Quando o usuário da agência realiza a validação FABS dos registros de empréstimo com zero e branco
Então as regras de validação FABS aceitam zero e branco nos registros de empréstimo