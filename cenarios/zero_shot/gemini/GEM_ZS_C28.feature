# language: pt

Funcionalidade: Enviar candidatura

Cenário: Envio com sucesso da candidatura para iniciar uma transação
Dado que o Requerente está na etapa de envio de candidatura
Quando o Requerente envia a candidatura com suas informações, planos ou documentos
Então a candidatura é enviada para iniciar a transação com o Município
