## Funcionalidades (Épicos e User Stories)

**Épico 1: Cadastro de Produtos**

* US1: Como usuário, quero cadastrar um novo produto com ID, nome, categoria, quantidade em estoque e preço, para que eu possa gerenciar meu estoque.
* US2: Como usuário, quero remover um produto existente do sistema, para que eu possa atualizar meu estoque.
* US3: Como usuário, quero editar as informações de um produto existente (nome, categoria, quantidade em estoque, preço), para que eu possa corrigir informações incorretas ou atualizar dados.

**Épico 2: Controle de Estoque**

* US4: Como usuário, quero registrar a entrada de produtos no estoque, para que eu possa atualizar a quantidade disponível.
* US5: Como usuário, quero registrar a saída de produtos do estoque, para que eu possa controlar as vendas e o consumo.
* US6: Como usuário, quero receber um alerta quando a quantidade de um produto estiver abaixo do mínimo estipulado, para que eu possa realizar um novo pedido.

**Épico 3: Consulta de Produtos**

* US7: Como usuário, quero buscar produtos por nome, para que eu possa encontrar rapidamente um produto específico.
* US8: Como usuário, quero buscar produtos por categoria, para que eu possa visualizar todos os produtos de uma mesma categoria.
* US9: Como usuário, quero buscar produtos por ID, para que eu possa acessar informações precisas de um produto específico.
* US10: Como usuário, quero visualizar as informações detalhadas de um produto, incluindo ID, nome, categoria, quantidade em estoque e preço, para que eu possa tomar decisões informadas.

**Épico 4: Relatórios**

* US11: Como usuário, quero gerar um relatório de todos os produtos em estoque, para que eu possa ter uma visão geral do meu estoque.
* US12: Como usuário, quero gerar um relatório de produtos com baixo estoque, para que eu possa identificar produtos que precisam ser repostos.

**Épico 5: Interface e Usabilidade**

* US13: Como usuário, quero interagir com o sistema através de um menu intuitivo e fácil de usar, para que eu possa acessar todas as funcionalidades de forma simples e eficiente.
* US14: Como usuário, quero que o sistema valide as entradas para evitar erros, assegurando a integridade dos dados.


## Critérios de Aceitação

* US1: O sistema deve permitir o cadastro de novos produtos com os campos: ID (único), nome, categoria, quantidade em estoque e preço. Os dados devem ser armazenados em um dicionário.
* US2: O sistema deve permitir a remoção de produtos através do ID, atualizando o dicionário de produtos.
* US3: O sistema deve permitir a edição de informações de produtos existentes através do ID, atualizando o dicionário de produtos.
* US4: O sistema deve permitir o registro da entrada de produtos, atualizando automaticamente a quantidade em estoque.
* US5: O sistema deve permitir o registro da saída de produtos, atualizando automaticamente a quantidade em estoque.
* US6: O sistema deve emitir um alerta (mensagem na tela) quando a quantidade de um produto atingir ou ficar abaixo do estoque mínimo.  O estoque mínimo deve ser um parâmetro configurável.
* US7, US8, US9: O sistema deve permitir a busca de produtos por nome, categoria e ID, retornando os resultados correspondentes.
* US10: O sistema deve exibir as informações completas do produto consultado.
* US11: O sistema deve gerar um relatório mostrando todos os produtos e suas informações.
* US12: O sistema deve gerar um relatório mostrando apenas os produtos com quantidade em estoque abaixo do estoque mínimo.
* US13: O sistema deve apresentar um menu de navegação claro e conciso, permitindo o acesso a todas as funcionalidades.
* US14: O sistema deve validar todas as entradas do usuário, tratando erros de formato e tipo de dados.


## Priorização (MoSCoW)

**Must have (Essencial):**

* US1: Cadastrar um novo produto
* US4: Registrar entrada de produtos
* US5: Registrar saída de produtos
* US7: Buscar produtos por nome
* US10: Visualizar informações detalhadas de um produto
* US13: Menu de navegação

**Should have (Importante):**

* US2: Remover um produto
* US3: Editar informações de um produto
* US8: Buscar produtos por categoria
* US11: Relatório de todos os produtos em estoque
* US14: Validação de entradas

**Could have (Desejável):**

* US6: Alerta de baixo estoque
* US9: Buscar produtos por ID
* US12: Relatório de produtos com baixo estoque

**Won't have (Não será feito neste MVP):**

* Nenhuma funcionalidade definida para esta categoria neste MVP.
