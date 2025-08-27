## Fluxos de Usuário

**Fluxo 1: Cadastro de Produtos**

O usuário acessa o menu principal, seleciona a opção "Cadastro de Produtos", escolhe entre adicionar, editar ou remover um produto.  Se adicionar, preenche os campos (ID, nome, categoria, quantidade, preço), valida os dados, e o sistema salva as informações. Se editar, busca o produto pelo ID, altera os campos desejados, valida e salva. Se remover, busca o produto pelo ID e confirma a remoção.

**Fluxo 2: Controle de Estoque**

O usuário acessa o menu principal, seleciona "Controle de Estoque", escolhe entre registrar entrada ou saída de produtos.  Informa o ID do produto e a quantidade. O sistema valida os dados, atualiza a quantidade em estoque e emite alertas se a quantidade ficar abaixo do mínimo.

**Fluxo 3: Consulta de Produtos**

O usuário acessa o menu principal, seleciona "Consulta de Produtos", escolhe o critério de busca (nome, categoria ou ID). Informa o valor de busca e o sistema exibe as informações detalhadas do(s) produto(s) encontrado(s).

**Fluxo 4: Relatórios**

O usuário acessa o menu principal, seleciona "Relatórios", e escolhe entre "Produtos em Estoque" ou "Produtos com Baixo Estoque". O sistema gera o relatório na tela (poderia ser aprimorado para gerar arquivo).


## Navegação

1. **Menu Principal:**  Opções: Cadastro de Produtos, Controle de Estoque, Consulta de Produtos, Relatórios, Sair.
2. **Cadastro de Produtos:** Submenu: Adicionar, Editar, Remover.  Retorno ao Menu Principal após cada ação.
3. **Controle de Estoque:** Submenu: Entrada, Saída. Retorno ao Menu Principal após cada ação.
4. **Consulta de Produtos:** Tela de busca com campos para nome, categoria ou ID. Exibição dos resultados. Retorno ao Menu Principal.
5. **Relatórios:** Submenu: Produtos em Estoque, Produtos com Baixo Estoque. Retorno ao Menu Principal.


## Interações

**Menu Principal:**

* **Usuário:** Seleciona uma opção do menu (1 a 5).
* **Sistema:** Exibe o submenu correspondente ou finaliza a aplicação (opção 5).

**Cadastro de Produtos (Adicionar):**

* **Usuário:** Preenche os campos (ID, nome, categoria, quantidade, preço).
* **Sistema:** Valida os dados. Se válidos, salva o produto e retorna ao menu de Cadastro. Se inválidos, exibe mensagem de erro.

**Cadastro de Produtos (Editar/Remover):**

* **Usuário:** Informa o ID do produto.
* **Sistema:** Busca o produto. Se encontrado, permite edição (ou confirmação de remoção). Se não encontrado, exibe mensagem de erro.

**Controle de Estoque (Entrada/Saída):**

* **Usuário:** Informa o ID do produto e a quantidade.
* **Sistema:** Valida os dados, atualiza o estoque e exibe a nova quantidade. Emite alerta se abaixo do mínimo.

**Consulta de Produtos:**

* **Usuário:** Seleciona o critério de busca e informa o valor.
* **Sistema:** Busca e exibe os resultados.

**Relatórios:**

* **Usuário:** Seleciona o tipo de relatório.
* **Sistema:** Gera e exibe o relatório.

<br>
<hr>
<br>

### 🧠 Instruções para o Agente de Desenvolvimento

**📝 Prompt Complementar:**
Este documento define os fluxos de usuário e a navegação para um MVP de sistema de gestão de estoque. A próxima fase do desenvolvimento deve focar na implementação de uma API RESTful que permita a realização desses fluxos, priorizando endpoints simples e diretos para cada ação do usuário, sem implementar funcionalidades adicionais ou complexas não contempladas neste documento. O foco deve estar em entregar valor rapidamente e validar as funcionalidades essenciais do MVP.


**👍 Instruções Positivas:**
Foque em endpoints RESTful que reflitam diretamente as ações descritas nos fluxos de usuário.  Priorize a simplicidade e a clareza do código.  Implemente validações mínimas, focadas na integridade dos dados (tipos e restrições básicas). Utilize uma base de dados leve e simples (ex: SQLite para desenvolvimento).  Os endpoints devem retornar apenas o essencial para cada ação (ex: ID do produto criado, status da operação, etc.).  Lembre-se que este é um MVP, então a escalabilidade e a complexidade devem ser mantidas ao mínimo.  Priorize o teste unitário para garantir a funcionalidade básica de cada endpoint.

**👎 Instruções Negativas:**
Evite implementar recursos avançados de autenticação, autorização ou gerenciamento de usuários nesta fase.  Não implemente mecanismos de cache, logging sofisticado, ou outras funcionalidades não-essenciais para o MVP.  Não utilize frameworks ou bibliotecas complexas desnecessárias.  Não crie relatórios em formato de arquivo (PDF, CSV, etc.) nesta fase; a exibição na tela é suficiente.  Não implemente funcionalidades de busca complexa com paginação ou filtros avançados; uma busca simples por ID, nome ou categoria é suficiente. Evite a criação de uma camada de abstração de dados complexa para o banco de dados, utilize acesso direto se possível.
