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
