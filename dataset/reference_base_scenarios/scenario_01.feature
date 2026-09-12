@g02-federalspending

# As a Website user, I want to access published FABS files, so that I can see the new files as they come in.
Cenário: Visualizar arquivos FABS publicados
Dado que o usuário acessa o sistema
Quando acessar a seção de arquivos FABS publicados
Então deve visualizar os arquivos FABS já publicados
E deve visualizar novos arquivos à medida que eles forem publicados

# As a website user, I want to see updated financial assistance data daily.
Cenário: Visualizar dados de assistência financeira atualizados diariamente
Dado que o usuário acessa o sistema
Quando acessar os dados de assistência financeira
Então deve visualizar os dados atualizados diariamente

# As a user, I want the publish button in FABS to deactivate after I click it while the derivations are happening, so that I cannot click it multiple times for the same submission.
Cenário: Desativar botão de publicar arquivos FABS durante o processamento
Dado que o usuário acessa o sistema
Quando clicar no botão de publicar arquivos FABS
Então o botão de publicar deve ser desativado enquanto o processamento ocorre
E não deve ser permitido realizar múltiplos cliques no mesmo envio

# As an agency user, I want the FABS validation rules to accept zero and blank for loan records.
Cenário: Aceitar valores zero e em branco para registros de empréstimos
Dado que o usuário da agência acessa o sistema
Quando enviar registros de empréstimos com valores zero ou em branco
Então o sistema deve aceitar esses registros sem erros de validação

# As an Agency user, I want the header information box to show updated date AND time, so that I know when it was updated.
Cenário: Mostrar data e hora de atualização na caixa de informações do cabeçalho
Dado que o usuário da agência acessa o sistema
Quando visualizar a caixa de informações do cabeçalho
Então o sistema deve exibir a data e hora de atualização corretamente

# As an Agency user, I want to receive a more helpful file-level error when I upload a file with the wrong extension.
Cenário: Exibir mensagem de erro ao enviar um arquivo com extensão incorreta
Dado que o usuário da agência acessa o sistema
Quando realizar o upload de um arquivo com extensão incorreta
Então o sistema deve exibir uma mensagem de erro relacionada à extensão do arquivo

# As an Agency user, I want to accurately see who created a submission, so that I'm not confused about who last updated a submission.
Cenário: Exibir informações precisas sobre o criador da submissão
Dado que o usuário da agência acessa o sistema
Quando visualizar uma submissão
Então o sistema deve exibir corretamente o nome do usuário que criou a submissão

# As an agency user, I want a landing page to navigate to either FABS or DABS pages, so that I can access both sides of the site.
Cenário: Navegar para páginas FABS ou DABS a partir da página inicial
Dado que o usuário da agência acessa a página inicial
Quando realizar a navegação para FABS ou DABS
Então o sistema deve redirecionar o usuário para a página da área correspondente 

# As an agency user, I want to know when the submission periods start and end, so that I know when the submission starts and ends.
Cenário: Exibir informações sobre o período de submissão
Dado que o usuário da agência acessa o sistema
Quando visualizar as informações de submissão
Então o sistema deve exibir as datas de início e término do período de submissão

# As a user, I want more information about how many rows will be published prior to deciding whether to publish.
Cenário: Exibir informações sobre o número de linhas a serem publicadas
Dado que o usuário acessa o sistema
E está na página de submissão
Quando visualizar as informações de submissão
Então o sistema deve exibir claramente o número de linhas que serão publicadas

@g14-datahub

# As a Publisher, I want to sign up for an account, so that that I can publish my data package to the registry and to have a publisher account to publish my data package under.
Cenário: Realizar cadastro de conta de editor
Dado que o usuário acessa o sistema
E o usuário deseja possuir uma conta de editor
Quando realizar o cadastro
Então deve possuir uma conta de editor para publicar seus pacotes de dados

# As a Publisher, I want to import my data package into the registry, so that my data has a permanent online home to access. 
Cenário: Importar pacote de dados para o registro
Dado que o editor acessa o sistema
E que possui pacotes de dados para importação
Quando importar um pacote de dados para o registro
Então o pacote de dados deve permanecer disponível online para acesso futuro

# As a Publisher, I want to unpublish a data package, so that it is no longer visible to anyone.
Cenário: Despublicar pacotes de dados
Dado que o editor acessa o sistema
E que possui pacotes de dados publicados
Quando despublicar um pacote de dados
Então o pacote de dados não deve mais ser visível para os demais usuários

# As a Publisher, I want to create a data package in the UI so that it is available and published.
Cenário: Criar pacote de dados pela interface
Dado que o editor acessa o sistema
Quando criar um pacote de dados pela interface
Então o pacote de dados deve ficar disponível e publicado

# As a Publisher, I want to undelete the deleted data packages, so that that the deleted data packages is now visible again.
Cenário: Restaurar pacotes de dados excluídos
Dado que o editor acessa o sistema
E que possui pacotes de dados excluídos
Quando restaurar um pacote de dados excluído
Então o pacote de dados deve se tornar visível novamente para os demais usuários

# As a Consumer, I want to search data packages, so that that I can find the ones I want.
Cenário: Pesquisar pacotes de dados
Dado que o usuário acessa o sistema  
Quando realizar uma pesquisa por pacotes de dados
Então o sistema deve exibir os pacotes de dados correspondentes aos critérios da pesquisa

# As a Consumer, I want to download the data package in one file, so that that I don't have to download descriptor and each resource by hand.
Cenário: Baixar pacote de dados em um único arquivo
Dado que o usuário possui um pacote de dados disponível
Quando realizar o download de um pacote de dados
Então o sistema deve fornecer o pacote de dados completo em um único arquivo para download

# As an Owner, I want to edit my profile, so that that it is updated with new information.
Cenário: Editar perfil do proprietário
Dado que o proprietário acessa o sistema
Quando realizar alterações em seu perfil
Então o sistema deve atualizar as informações do perfil com os novos dados fornecidos

# As an Owner, I want to invite an existing user, so that the user can become a member of my publisher.
Cenário: Convidar usuário existente para se tornar membro de uma editora
Dado que o proprietário acessa o sistema
Quando convidar um usuário existente para se tornar membro de sua editora
Então o usuário deve poder se tornar membro da editora

# As an owner, I want to remove someone from membership in my publisher, so that they no longer have ability to publish or modify my data packages.
Cenário: Remover membro de uma editora
Dado que o proprietário acessa o sistema
Quando remover um membro de sua editora
Então o membro não deve mais ter a capacidade de publicar ou modificar os pacotes de dados da editora

# As an owner, I want to make a user an owner, so that they have full control.
Cenário: Tornar um usuário proprietário
Dado que o proprietário acessa o sistema
Quando tornar um usuário proprietário
Então o usuário deve ter controle total sobre a editora e seus pacotes de dados

# As an owner, I want to remove a user as an owner, so that they are just a member and no longer have full control.
Cenário: Remover um usuário como proprietário
Dado que o proprietário acessa o sistema
Quando remover um usuário como proprietário
Então o usuário deve se tornar apenas um membro e não ter mais controle total sobre a editora e seus pacotes de dados

@g03-loudoun


# As a Staff member, I want to Apply a Hold, so that I can prevent progression through the workflow or other actions in the system until the issue is resolved.
Cenário: Aplicar uma restrição 
Dado que um membro da equipe acessa o sistema
Quando aplicar uma restrição
Então o sistema deve impedir a progressão através do workflow ou outras ações no sistema até que o problema seja resolvido

# As a Staff member, I want to Remove a Hold, so that I can allow progression through the workflow or other actions in the system now that the issue has been resolved.
Cenário: Remover uma restrição
Dado que um membro da equipe acessa o sistema
Quando remover uma restrição
Então o sistema deve permitir a progressão através do workflow ou outras ações no sistema agora que o problema foi resolvido

# As an Applicant, I want to Check the Status of a transaction, so that I can understand where the provisioning of my service is in the process, such as information related to service levels, fees, plan review, permit, or inspection results.
Cenário: Consultar status de uma transação 
Dado que um solicitante acessa o sistema
Quando verificar o status da transação
Então deve visualizar a etapa do processo em que se encontra o provisionamento do serviço

# As a Customer, I want to Create a Customer Portal User Account, so that I can log on to the Customer Portal and perform transactions that first require user authentication.
Cenário: Criar conta de usuário do Portal do Cliente
Dado que o usuário acessa o Portal do cliente
Quando realizar o cadastro
Então deve poder realizar login 
E deve poder acessar transações que necessitam de autenticação

# As an Applicant, I want to Submit Application, so that I can provide my information, plans and/or documents to initiate a transaction with the County.
Cenário: Realizar envio de solicitação
Dado que o solicitante acessa o sistema
Quando enviar uma solicitação com suas informações, planos e/ou documentos
Então a solicitação deve ser enviada para iniciar uma transação com o Condado

# As an Applicant, I want to Submit Supporting Documentation, so that I can satisfy documentation requirements for my application.
Cenário: Enviar documentação de suporte
Dado que o solicitante possui uma solicitação
Quando enviar a documentação de suporte da solicitação
Então a documentação deve ser enviada para atender aos requisitos documentais da solicitação

# As a Staff member, I need to be notified when Geospatial attributes change, so that I can ensure that I am reviewing the permit/application to the most current data and appropriate standards.
Cenário: Notificar alteração de atributos geoespaciais
Dado que o membro da equipe está revisando uma solicitação ou permissão
Quando os atributos geoespaciais forem alterados
Então o membro da equipe deve ser notificado sobre a alteração

# As an Inspection Staff member, I want to Create an Inspection, so that I can schedule and assign the inspection.
Cenário: Criar uma inspeção
Dado que o membro da equipe de inspeção acessa o sistema
Quando criar uma inspeção
Então a inspeção deve ser criada e estar disponível para agendamento e atribuição

# As a Plan Review Staff Member, I want to Review the Code Modifications submitted by the Applicant, so that I can review the request and if approved, associate it with the appropriate project.
Cenário: Revisar modificações de código submetidas pelo solicitante
Dado que o membro da equipe de análise de projetos acessa uma solicitação com modificações de código submetidas pelo solicitante
Quando revisar as modificações de código
Então deve poder revisar a solicitação
E se aprovada, deve poder associá-la ao projeto apropriado

# As a Plan Review Staff Supervisor, I want to Manage Plan Reviewer Workload, so that I can monitor and effectively adjust workload as necessary and ensure service levels are met
Cenário: Gerenciar carga de trabalho dos analistas de projetos
Dado que o supervisor da equipe de análise de projetos acessa o sistema
Quando gerenciar a carga de trabalho dos analistas de projetos
Então deve poder monitorar e ajustar a carga de trabalho conforme necessário para garantir os níveis de serviço

# g18-neurohub

# As a researcher, I want to upload files prior to having them attached to a log book page using the web interface.
Cenário: Fazer upload de arquivos para anexá-los a uma página
Dado que o pesquisador acessa o sistema pela interface web
Quando realizar o upload de arquivos
Então os arquivos devem ficar disponíveis para serem anexados posteriormente a uma página do livro de registros

# As a researcher, I want to attach currently non-attached files to a log book page.
Cenário: Anexar arquivos não associados a uma página
Dado que o pesquisador possui arquivos que não estão anexados a uma página do livro de registros
Quando anexar os arquivos a uma página do livro de registros
Então os arquivos devem ficar anexados à página do livro de registros

# As a researcher, I want to receive an alert of any unattached files that are in my workspace.
Cenário: Alertar sobre arquivos não anexados
Dado que o pesquisador possui arquivos em seu espaço de trabalho
Quando houverem arquivos não estão anexados no espaço de trabalho
Então o pesquisador deve receber um alerta sobre os arquivos não anexados

# As a researcher, I want to download files attached to an experiment using my Web browser.
Cenário: Baixar arquivos anexados a um experimento pelo navegador
Dado que o pesquisador possui arquivos anexados a um experimento
Quando realizar o download dos arquivos pelo navegador
Então os arquivos devem ser disponibilizados para download

# As a user, I want to upload large files of over 1GB in size.
Cenário: Realizar upload de arquivos com mais de 1GB
Dado que o usuário acessa o sistema
Quando realizar o upload de arquivos
Então deve ser possível anexar para upload aqueles com mais de 1 GB de tamanho

# As a user, I want to assign tags to files that I have uploaded.
Cenário: Atribuir tags a arquivos enviados
Dado que o usuário possui arquivos enviados
Quando atribuir tags aos arquivos
Então os arquivos devem ficar associados às tags atribuídas

# As a user, I want to filter the files I get from search results based on their  type.
Cenário: Filtrar arquivos com base no tipo
Dado que o usuário realizou uma pesquisa por arquivos
Quando filtrar os resultados pelo tipo de arquivo
Então o sistema deve exibir apenas os arquivos correspondentes ao tipo selecionado

# As a user, I want to have files I might accidentally delete to be restorable.
Cenário: Restaurar arquivos deletados
Dado que o usuário possui arquivos que foram deletados
Quando restaurar um arquivo 
Então o arquivo deve ser restaurado e ficar novamente disponível para o usuário

# As a user, I want to search specifically for files rather than log book pages.
Cenário: Pesquisar especificamente por arquivosa
Dado que o usuário realiza uma pesquisa
Quando pesquisar especificamente por arquivos
Então o sistema deve exibir resultados referentes aos arquivos, sem incluir páginas do livro de registros

# As a user, I want to download files directly from the search results page.
Cenário: Realizar download de arqivos buscados
Dado que o usuário realizou uma busca
Quando visualizar os resultados
Então deve ser possível realizar o download de arquivos direto da listagem de resultados da busca

# As a user, I want to attach multiple files at once to a log book page.
Cenário: Anexar múltiplos arquivos a uma página do livro de registros
Dado que o usuário acessa uma página do livro de registros
Quando anexar múltiplos arquivos à página
Então os arquivos devem ser anexados à página do livro de registros

# As a user, I want to download multiple files from the search results in one go.
Cenário: Baixar múltiplos arquivos dos resultados da pesquisa
Dado que o usuário possui múltiplos arquivos nos resultados da pesquisa
Quando realizar o download dos arquivos
Então o sistema deve permitir baixar os múltiplos arquivos de uma só vez

# As a user, I want to either keep a logbook entry private or share it with individuals rather than groups.
Cenário: Definir o compartilhamento de uma entrada do livro de registros
Dado que o usuário possui uma entrada no livro de registros
Quando definir as opções de compartilhamento da entrada
Então deve poder mantê-la privada
E deve poder compartilhá-la com indivíduos em vez de grupos
