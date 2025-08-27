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

<br>
<hr>
<br>

### 🧠 Instruções para o Agente de Desenvolvimento

**📝 Prompt Complementar:**
Este documento de prototipação define a arquitetura MVP de um sistema de gerenciamento de estoque.  A próxima fase de desenvolvimento deve focar na implementação funcional das funcionalidades essenciais descritas nos fluxos principais, utilizando Python e um arquivo de dados persistente (JSON ou Pickle).  O objetivo é validar a viabilidade e o fluxo de trabalho do core do sistema antes de investir em recursos mais avançados.

**👍 Instruções Positivas:**
Crie fluxos diretos e mockups funcionais que validem a funcionalidade base de cadastro, edição e remoção de produtos; controle de estoque com alertas de níveis mínimos; consulta de produtos por nome, categoria ou ID; e geração de relatórios simples de estoque, tudo isso utilizando a CLI. Priorize a clareza e a rapidez na implementação, focando na entrega das funcionalidades essenciais definidas neste documento.  Implemente testes unitários para garantir a corretude das funcionalidades. Utilize estruturas de dados Python (listas, tuplas e dicionários) de forma eficiente para representar os dados de produtos e estoque.  Documente o código com clareza, utilizando docstrings para explicar as funções e classes.

**👎 Instruções Negativas:**
Não perca tempo refinando a interface da CLI além do essencial para o funcionamento das funcionalidades.  Evite implementações complexas de validação de dados ou tratamento de exceções além do estritamente necessário para o MVP.  Não implemente recursos adicionais não descritos neste documento, como integrações com serviços externos ou funcionalidades de relatórios sofisticados.  Não utilize frameworks web ou bancos de dados relacionais/NoSQL nesta fase.  Evite a utilização de bibliotecas externas desnecessárias.  Não se preocupe com a otimização de performance ou escalabilidade neste momento.
