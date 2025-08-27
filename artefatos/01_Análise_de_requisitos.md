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


<br>
<hr>
<br>

### 🧠 Instruções para o Agente de Desenvolvimento

**📝 Prompt Complementar:**
Este documento define os requisitos para um MVP de um sistema de gerenciamento de estoque.  A próxima fase de desenvolvimento deve focar na construção de um protótipo funcional que valide a hipótese central:  que um sistema simples e intuitivo para controle de estoque, com funcionalidades básicas de cadastro, controle de entrada/saída e relatórios, atenderá às necessidades dos Gerentes de Estoque e Funcionários de Almoxarifado.  Priorize a entrega rápida de um sistema mínimo viável para testar a aceitação do usuário e iterar com base no feedback obtido.

**👍 Instruções Positivas:**
Descubra a hipótese principal a ser validada: a usabilidade e utilidade de um sistema de gerenciamento de estoque básico para os perfis de Gerente de Estoque e Funcionário de Almoxarifado. Reduza o escopo ao mínimo necessário para testar a aceitação, implementando apenas as funcionalidades essenciais de cadastro de produtos (com validação básica), controle de estoque (entradas e saídas, com alerta de estoque baixo), e consulta de produtos por ID.  Concentre-se em uma interface de usuário simples e intuitiva, usando Python e as estruturas de dados especificadas (listas, tuplas e dicionários).  Priorize a implementação de testes unitários para garantir a qualidade do código.  Implemente um mecanismo básico de persistência de dados (e.g., arquivos CSV) para manter a informação entre as sessões. Foque na entrega de um sistema funcional, mesmo que com limitações estéticas.

**👎 Instruções Negativas:**
Não tente implementar todas as funcionalidades descritas nos requisitos funcionais e não-funcionais de uma vez. Evite o uso de banco de dados complexos ou frameworks adicionais neste estágio.  Não implemente recursos de segurança avançados (autenticação, autorização) ou mecanismos de relatórios sofisticados.  Não se preocupe com a escalabilidade ou performance para um grande volume de dados neste momento. Não busque a perfeição no design da interface do usuário ou na elegância do código, focando na funcionalidade mínima necessária para o teste da hipótese.  Evite o uso de bibliotecas ou frameworks externos que adicionem complexidade desnecessária ao projeto nesta fase inicial.
