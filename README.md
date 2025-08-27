# Sistema de Gerenciamento de Estoque (MVP)

Este projeto é um Sistema de Gerenciamento de Estoque simplificado, desenvolvido como um Produto Mínimo Viável (MVP) para demonstração e validação de conceitos. Ele oferece uma API RESTful para gerenciar produtos e uma interface de usuário web básica para interação.

## Funcionalidades Implementadas

Até o momento, as seguintes funcionalidades foram implementadas:

*   **Cadastro de Produtos:**
    *   Adicionar novos produtos com ID automático, nome, categoria, preço, quantidade e estoque mínimo.
*   **Controle de Estoque:**
    *   Registrar entrada de produtos.
    *   Registrar saída de produtos (com validação para não permitir estoque negativo).
    *   Atualização automática da quantidade em estoque.
    *   Emissão de alerta quando a quantidade de um produto está abaixo ou igual ao seu estoque mínimo.
*   **Consulta de Produtos:**
    *   Listar todos os produtos.
    *   Buscar produtos por nome (busca parcial e case-insensitive).
    *   Obter detalhes de um produto específico por ID.
*   **Persistência de Dados:**
    *   Os dados são persistidos em um arquivo `estoque.json`.
*   **Interface de Usuário (Dashboard):**
    *   Dashboard web interativo com formulário de cadastro e controle de estoque.
    *   Tabela de listagem de produtos com detalhes e alertas visuais.

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
    # git clone <URL_DO_REPOSITORIO>
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
    *   Serve a página HTML do dashboard.
*   **`GET /docs`**
    *   Documentação interativa da API (Swagger UI).
*   **`GET /produtos`**
    *   **Descrição:** Lista todos os produtos no estoque.
    *   **Parâmetros de Query:** `nome` (opcional, string) - Filtra produtos por nome (busca parcial, case-insensitive).
    *   **Retorno:** `List[Produto]`
*   **`GET /produtos/{produto_id}`**
    *   **Descrição:** Obtém os detalhes de um produto específico.
    *   **Parâmetros de Path:** `produto_id` (inteiro) - ID único do produto.
    *   **Retorno:** `Produto` (ou 404 se não encontrado).
*   **`POST /produtos`**
    *   **Descrição:** Cria um novo produto no estoque.
    *   **Corpo da Requisição:** `ProdutoCreate` (nome, categoria, preco, quantidade, estoque_minimo).
    *   **Retorno:** `Produto` (com ID gerado, status 201 Created).
*   **`POST /produtos/{produto_id}/entrada`**
    *   **Descrição:** Registra a entrada de uma quantidade de um produto no estoque.
    *   **Parâmetros de Path:** `produto_id` (inteiro).
    *   **Corpo da Requisição:** `EstoqueUpdate` (quantidade).
    *   **Retorno:** `Produto` (atualizado, com `alert_message` se estoque baixo).
*   **`POST /produtos/{produto_id}/saida`**
    *   **Descrição:** Registra a saída de uma quantidade de um produto do estoque.
    *   **Parâmetros de Path:** `produto_id` (inteiro).
    *   **Corpo da Requisição:** `EstoqueUpdate` (quantidade).
    *   **Retorno:** `Produto` (atualizado, com `alert_message` se estoque baixo, ou 400 se quantidade insuficiente).

## Próximos Passos (Funcionalidades Pendentes)

Para expandir este MVP, as próximas funcionalidades a serem consideradas incluem:

*   **Remover Produto:** Implementar endpoint `DELETE /produtos/{produto_id}` e integração no frontend.
*   **Editar Produto:** Implementar endpoint `PUT /produtos/{produto_id}` e integração no frontend.
*   **Buscar por Categoria:** Adicionar filtro por categoria no endpoint `GET /produtos`.
*   **Relatório de Produtos com Baixo Estoque:** Criar um endpoint específico para este relatório.
