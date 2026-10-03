# language: pt

Funcionalidade: Aceitação de zero e vazio nas regras de validação FABS para registros de empréstimo

Cenário: Regras de validação FABS aceitam zero e vazio para registros de empréstimo
Dado que o usuário de agência possui registros de empréstimo com valor zero ou vazio
Quando o usuário de agência realiza a validação FABS dos registros de empréstimo
Então as regras de validação FABS aceitam os registros de empréstimo com valor zero ou vazio