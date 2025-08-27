## Regras de Negócio

* **Cadastro de Produtos:** O sistema deve permitir o cadastro de produtos com os seguintes atributos: ID (único), nome, categoria, quantidade em estoque e preço.  A validação de entrada é obrigatória, assegurando que todos os campos sejam preenchidos corretamente (nome e categoria não podem ser vazios, quantidade e preço devem ser numéricos e positivos).  O ID será gerado automaticamente pelo sistema, garantindo unicidade.  O uso de dicionários para armazenar as informações dos produtos é mandatário.

* **Controle de Estoque:** O sistema deve registrar entradas e saídas de produtos, atualizando a quantidade em estoque automaticamente.  A quantidade em estoque nunca poderá ser negativa.  Deve existir um campo para definir a quantidade mínima em estoque para cada produto. Quando a quantidade em estoque de um produto atingir ou ficar abaixo da quantidade mínima, o sistema deve emitir um alerta.

* **Consulta de Produtos:** O sistema deve permitir a busca de produtos por nome, categoria ou ID. A busca deve ser case-insensitive (não sensível a maiúsculas/minúsculas).  O sistema deve exibir todas as informações do produto encontrado. Caso nenhum produto seja encontrado, deve ser exibida uma mensagem informativa.

* **Relatórios:** O sistema deve gerar relatórios de produtos em estoque, listando todos os produtos com suas informações completas e um relatório de produtos com baixo estoque (abaixo da quantidade mínima).

* **Interface e Usabilidade:** O sistema deve possuir uma interface de menu interativo para acesso às funcionalidades, utilizando estruturas de repetição e seleção para navegação. A validação de entradas do usuário é obrigatória para evitar erros e garantir a integridade dos dados.


## Restrições

* O sistema será desenvolvido utilizando a linguagem Python.
* A utilização de dicionários para armazenar informações de produtos é obrigatória.
* A quantidade mínima em estoque deve ser definida para cada produto.
* Não há suporte para múltiplos usuários simultâneos.
* O sistema será baseado em uma interface de linha de comando (CLI).


## Exceções

* **Entrada inválida:**  O sistema deve tratar entradas inválidas do usuário (ex: letras em campos numéricos, campos obrigatórios vazios) exibindo mensagens de erro claras e solicitando a reentrada dos dados.
* **Quantidade negativa:** Tentativas de registrar uma saída de produto que resulte em quantidade em estoque negativa devem ser impedidas, exibindo uma mensagem de erro.
* **Produto não encontrado:**  Se um produto não for encontrado durante uma consulta ou remoção, uma mensagem informativa apropriada deve ser exibida.
* **Arquivo de dados:** Caso haja falha na leitura ou escrita do arquivo de dados (persistência dos dados), uma mensagem de erro apropriada deve ser apresentada ao usuário.


## Decisões

* Utilizar dicionários para representar os produtos, por sua flexibilidade e facilidade de acesso aos dados.
* Implementar um sistema de alertas para produtos com estoque baixo.
* Gerar relatórios em formato de texto na tela.
* Criar um menu de navegação intuitivo e amigável para o usuário.
* Implementar validações robustas para evitar erros de entrada de dados.
* A persistência dos dados (salvando e carregando os produtos) será feita em um arquivo externo (exemplo: arquivo .json ou .txt).  A escolha do formato de arquivo ficará a cargo da implementação.


<br>
<hr>
<br>

### 🧠 Instruções para o Agente de Desenvolvimento

**📝 Prompt Complementar:**
Este documento define as regras de negócio, restrições e exceções para o desenvolvimento de um MVP de um sistema de gerenciamento de estoque. A próxima fase de desenvolvimento deve focar na implementação de um protótipo funcional que atenda às funcionalidades essenciais descritas, utilizando uma arquitetura simples e eficiente, priorizando a entrega rápida e a validação das funcionalidades principais com o usuário.

**👍 Instruções Positivas:**
Use uma arquitetura monolítica simples e direta, utilizando dicionários Python para o armazenamento de dados como especificado.  Priorize a clareza e manutenibilidade do código, utilizando boas práticas de programação como funções bem definidas e nomes de variáveis descritivas.  Implemente as funcionalidades de cadastro, controle de estoque, consulta e geração de relatórios de forma incremental, testando cada módulo individualmente antes de integrar.  Foque na construção de uma interface CLI intuitiva e fácil de usar, garantindo que a validação de entrada seja robusta e que mensagens de erro sejam informativas.  Facilite a adição de novas funcionalidades no futuro, mantendo o código modular e bem estruturado.

**👎 Instruções Negativas:**
Não implemente recursos complexos de escalabilidade, como bancos de dados relacionais ou sistemas de gerenciamento de usuários sofisticados.  Evite o uso de frameworks ou bibliotecas desnecessárias, a menos que sejam essenciais para o funcionamento de funcionalidades básicas.  Não implemente funcionalidades não essenciais listadas no documento original, como por exemplo, interface gráfica ou suporte a múltiplos usuários.  Não se preocupe em otimizar o desempenho para um grande volume de dados neste MVP.  Não perca tempo implementando soluções de persistência de dados extremamente robustas ou complexas.  Um arquivo simples (JSON ou TXT) é suficiente para este protótipo.
