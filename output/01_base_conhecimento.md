## Regras de Negócio
* Cada produto deve possuir um ID único.
* A quantidade em estoque nunca pode ser negativa.
* O sistema deve registrar todas as entradas e saídas de produtos, mantendo um histórico audível.
* O sistema deve emitir alertas para produtos com estoque abaixo do mínimo definido.
* Preços dos produtos devem ser positivos.
* As categorias de produtos devem ser consistentes e bem definidas.


## Requisitos Funcionais
* Cadastro de produtos (inclusão, alteração e exclusão).
* Controle de estoque (registrar entradas e saídas, atualizar quantidade em estoque).
* Consulta de produtos por nome, categoria ou ID.
* Emissão de relatórios de produtos em estoque e produtos com baixo estoque.
* Interface de usuário interativa com menu de navegação.
* Validação de entradas de usuário.


## Requisitos Não Funcionais
* O sistema deve ser eficiente e responder rapidamente às solicitações do usuário.
* A interface deve ser intuitiva e fácil de usar, mesmo para usuários com pouca experiência em sistemas de gerenciamento de estoque.
* O sistema deve ser robusto e suportar um grande volume de dados.
* O sistema deve ser seguro, protegendo os dados contra acesso não autorizado.
* O código deve ser bem organizado, comentado e seguir boas práticas de programação.
* O sistema deve ser desenvolvido utilizando a linguagem Python e as estruturas de dados listadas no documento de contexto (listas, tuplas, dicionários).


## Personas de Usuário
* **Gerente de Estoque:** Responsável por monitorar os níveis de estoque, gerar relatórios e realizar ajustes.
* **Funcionário de Almoxarifado:** Responsável pelas entradas e saídas de produtos no estoque.


## Fluxos de Usuário
* **Cadastro de Produto:** O usuário acessa o menu, seleciona a opção de cadastro, insere os dados do produto (ID, nome, categoria, quantidade, preço) e confirma. O sistema valida os dados e salva as informações.
* **Controle de Estoque:** O usuário acessa o menu, seleciona a opção de controle de estoque, escolhe entre entrada ou saída, informa o ID do produto e a quantidade. O sistema atualiza o estoque e gera um alerta se a quantidade estiver abaixo do mínimo.
* **Consulta de Produto:** O usuário acessa o menu, seleciona a opção de consulta, informa o critério de busca (nome, categoria ou ID) e o sistema exibe as informações do produto.
* **Relatórios:** O usuário acessa o menu, seleciona a opção de relatórios e escolhe entre o relatório de estoque geral ou de produtos com baixo estoque. O sistema gera o relatório.

