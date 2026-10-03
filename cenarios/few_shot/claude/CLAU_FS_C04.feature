# language: pt

Funcionalidade: Aceitar valores zero e em branco para registros de empréstimo na validação FABS

Cenário: Validar registro de empréstimo com valor zero ou em branco
Dado que o usuário da agência possui um registro de empréstimo com valor zero ou em branco
Quando o sistema aplica as regras de validação FABS sobre o registro
Então o sistema aceita o registro de empréstimo como válido