# Sistema de Gerenciamento de Estoque (MVP)

Este projeto é um Sistema de Gerenciamento de Estoque simplificado, desenvolvido como um Produto Mínimo Viável (MVP) para demonstração e validação de conceitos. Ele oferece uma API RESTful para gerenciar produtos e uma interface de usuário web básica para interação.

## Funcionalidades Implementadas

*   **CRUD Completo de Produtos:**
    *   **Adicionar** novos produtos com ID automático, nome, categoria, preço, quantidade e estoque mínimo.
    *   **Editar** os dados de produtos existentes através de um formulário dinâmico.
    *   **Remover** produtos do estoque com diálogo de confirmação.
*   **Controle de Estoque:**
    *   Registrar **entrada** e **saída** de produtos de forma simples.
    *   Atualização automática da quantidade em estoque após cada movimentação.
    *   Emissão de **alerta visual** na interface quando a quantidade de um produto atinge o estoque mínimo.
*   **Consulta e Relatórios:**
    *   Listagem completa e paginada de todos os produtos.
    *   Busca dinâmica e em tempo real por **nome** e/ou **categoria**.
    *   Obtenção de detalhes de um produto específico.
    *   **Relatório** dedicado para produtos com baixo estoque.
*   **Persistência de Dados:**
    *   Os dados são salvos e carregados a partir de um arquivo `estoque.json`, garantindo a persistência entre as sessões.
*   **Interface de Usuário (Dashboard):**
    *   Dashboard web interativo e responsivo para gerenciar todo o sistema.
    *   Formulário único que alterna entre os modos de adição e edição.
    *   Tabela de produtos com filtros, alertas visuais e botões de ação (Editar, Detalhes, Remover).

## Tecnologias Utilizadas

*   **Backend:**
    *   Python 3.x
    *   FastAPI (Framework web)
    *   Pydantic (Validação de dados)
    *   Uvicorn (Servidor ASGI)
*   **Frontend:**
    *   HTML5
    *   CSS3
    *   JavaScript (Vanilla JS)

## Como Rodar o Projeto

Siga os passos abaixo para configurar e executar o projeto em sua máquina:

### Pré-requisitos

*   Python 3.8+ instalado.

### Configuração

1.  **Clone o repositório (se aplicável):**
    ```bash
    # Se este projeto estiver em um repositório Git
    # git clone <[URL_DO_REPOSITORIO](https://github.com/RogerioMatos75/Gerenciamento-de-Estoque.git)>
    # cd sistema-de-gerenciamento-de-estoque
    ```
    *(Se você recebeu os arquivos diretamente, pule esta etapa e certifique-se de estar no diretório raiz do projeto.)*

2.  **Crie e Ative o Ambiente Virtual:**
    É altamente recomendado usar um ambiente virtual para isolar as dependências do projeto.
    ```bash
    python -m venv .venv
    ```
    *   **No Windows:**
        ```bash
        .venv\Scripts\activate
        ```
    *   **No macOS/Linux:**
        ```bash
        source .venv/bin/activate
        ```

3.  **Instale as Dependências:**
    Com o ambiente virtual ativado, instale as bibliotecas necessárias:
    ```bash
    pip install -r requirements.txt
    ```

4.  **Inicie o Servidor:**
    Execute o servidor FastAPI. O flag `--reload` é útil para desenvolvimento, pois reinicia o servidor automaticamente a cada alteração no código.
    ```bash
    uvicorn main:app --reload
    ```

5.  **Acesse o Dashboard:**
    Com o servidor rodando, abra seu navegador e acesse:
    ```
    http://127.0.0.1:8000/
    ```
    Você também pode acessar a documentação interativa da API em:
    ```
    http://127.0.0.1:8000/docs
    ```

## Estrutura do Projeto

```
.
├── main.py                 # Aplicação FastAPI principal (backend)
├── estoque.json            # Arquivo JSON para persistência dos dados do estoque
├── requirements.txt        # Lista de dependências do Python
├── static/                 # Contém os arquivos do frontend
│   ├── index.html          # Estrutura HTML do dashboard
│   ├── style.css           # Estilos CSS do dashboard
│   └── script.js           # Lógica JavaScript do dashboard
└── .venv/                  # Ambiente virtual do Python (gerado automaticamente)
```

## Endpoints da API

Todos os endpoints retornam dados em formato JSON.

*   **`GET /`**
    *   Serve a página HTML principal do dashboard.
*   **`GET /docs`**
    *   Serve a documentação interativa da API (gerada automaticamente pelo FastAPI).
*   **`GET /produtos`**
    *   **Descrição:** Lista todos os produtos. Permite filtrar por nome e/ou categoria.
    *   **Parâmetros de Query:**
        *   `nome: str` (opcional) - Filtra produtos por nome (busca parcial, case-insensitive).
        *   `categoria: str` (opcional) - Filtra produtos por categoria (busca parcial, case-insensitive).
    *   **Retorno:** `List[Produto]`
*   **`POST /produtos`**
    *   **Descrição:** Cria um novo produto no estoque.
    *   **Corpo da Requisição:** `ProdutoCreate` (nome, categoria, preco, quantidade, estoque_minimo).
    *   **Retorno:** `Produto` (com ID gerado, status 201 Created).
*   **`GET /produtos/baixo-estoque`**
    *   **Descrição:** Retorna um relatório de produtos com quantidade igual ou inferior ao estoque mínimo.
    *   **Retorno:** `List[Produto]`
*   **`GET /produtos/{produto_id}`**
    *   **Descrição:** Obtém os detalhes de um produto específico.
    *   **Parâmetros de Path:** `produto_id: int`.
    *   **Retorno:** `Produto` (ou 404 se não encontrado).
*   **`PUT /produtos/{produto_id}`**
    *   **Descrição:** Atualiza os dados de um produto existente.
    *   **Parâmetros de Path:** `produto_id: int`.
    *   **Corpo da Requisição:** `ProdutoCreate`.
    *   **Retorno:** `Produto` (atualizado).
*   **`DELETE /produtos/{produto_id}`**
    *   **Descrição:** Remove um produto do estoque.
    *   **Parâmetros de Path:** `produto_id: int`.
    *   **Retorno:** `dict` (mensagem de sucesso).
*   **`POST /produtos/{produto_id}/entrada`**
    *   **Descrição:** Registra a entrada de uma quantidade de um produto.
    *   **Parâmetros de Path:** `produto_id: int`.
    *   **Corpo da Requisição:** `EstoqueUpdate` (quantidade).
    *   **Retorno:** `Produto` (atualizado).
*   **`POST /produtos/{produto_id}/saida`**
    *   **Descrição:** Registra a saída de uma quantidade de um produto.
    *   **Parâmetros de Path:** `produto_id: int`.
    *   **Corpo da Requisição:** `EstoqueUpdate` (quantidade).
    *   **Retorno:** `Produto` (atualizado).

## Checklist de Requisitos Cumpridos

Todos os requisitos do projeto foram implementados com sucesso.

**1. Cadastro de Produtos:**
- [x] Armazenamento de produtos com ID, nome, categoria, quantidade e preço.
- [x] Utilização de estrutura de dados baseada em dicionários (JSON/Pydantic).
- [x] Implementação das funcionalidades de Adicionar, Remover e Editar produtos.

**2. Controle de Estoque:**
- [x] Registro de entrada e saída de produtos.
- [x] Atualização automática da quantidade em estoque.
- [x] Emissão de alerta para produtos com estoque baixo.

**3. Consulta de Produtos:**
- [x] Busca de produtos por nome, categoria e ID.
- [x] Exibição de informações detalhadas dos produtos.

**4. Relatórios:**
- [x] Relatório geral de produtos em estoque (lista principal).
- [x] Relatório específico de produtos com baixo estoque.

**5. Interface e Usabilidade:**
- [x] Criação de um dashboard web interativo para acesso às funcionalidades.
- [x] Validação de entradas do usuário tanto no frontend quanto no backend.

## Checklist de Requisitos a Melhorias. Agora, temos as seguintes opções para finalizar o projeto:

   1. Implementar o botão "Atualizar Lista": Adicionar a funcionalidade que você sugeriu para atualizar a lista de produtos no
      dashboard.
   2. Atualizar o `requirements.txt`: Garantir que o arquivo de dependências contenha apenas o necessário e as versões exatas das
      bibliotecas.
   3. Considerar o projeto concluído: Se você estiver satisfeito com o estado atual do projeto.


  
  Mensagem de Commit Sugerida:

   1 feat: Implementação completa do sistema de gerenciamento de estoque
   2
   3 Este commit finaliza a implementação das funcionalidades principais do sistema de gerenciamento de estoque,
     incluindo:
   4 - Correção de inicialização do servidor.
   5 - Funcionalidade de exclusão de produtos.
   6 - Funcionalidade de edição de produtos.
   7 - Filtro de produtos por nome e categoria.
   8 - Relatório de produtos com baixo estoque.
   9 - Atualização completa da documentação no README.md (funcionalidades e endpoints da API).