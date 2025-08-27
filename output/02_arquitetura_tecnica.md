## Arquitetura

O sistema será um monolito, desenvolvido em Python, utilizando estruturas de dados como listas, tuplas e dicionários para armazenar e manipular informações sobre produtos e estoque.  A interface com o usuário será via terminal (CLI).

## Tecnologias

* **Linguagem:** Python
* **Banco de Dados:**  Um arquivo de dados (ex: JSON ou Pickle) será usado para persistir os dados, para simplicidade e atender aos requisitos do projeto.  Para um sistema real, um banco de dados relacional (ex: PostgreSQL, MySQL) ou NoSQL (ex: MongoDB) seria recomendado.
* **Interface:** Interface de linha de comando (CLI) em Python.


## Integrações

Não há integrações com serviços de terceiros neste projeto.


## Fluxos Principais

1. **Cadastro de Produtos:** O usuário interage com o menu CLI para adicionar novos produtos, fornecendo nome, categoria, quantidade e preço. O sistema valida as entradas e armazena as informações em um dicionário.  Funcionalidades de edição e remoção de produtos seguem um fluxo similar.

2. **Controle de Estoque:**  O sistema registra entradas e saídas de produtos, atualizando a quantidade em estoque no dicionário.  Um alerta é exibido se a quantidade de um produto cair abaixo de um mínimo definido (este mínimo deverá ser configurado pelo usuário).

3. **Consulta de Produtos:**  O usuário pode buscar produtos por nome, categoria ou ID via menu CLI. O sistema pesquisa no dicionário e exibe as informações do produto encontrado.

4. **Relatórios:** O sistema gera relatórios de produtos em estoque e produtos com baixo estoque, exibindo os dados formatados na CLI.  A geração dos relatórios irá iterar sobre o dicionário de produtos.
