# language: pt

Funcionalidade: Criar conta de usuário no Portal do Cliente

Cenário: Criar uma conta de usuário no Portal do Cliente com sucesso
Dado que o Cliente não possui uma conta de usuário no Portal do Cliente
Quando o Cliente cria uma conta de usuário no Portal do Cliente
Então o Cliente pode se autenticar no Portal do Cliente para realizar transações que exigem autenticação
