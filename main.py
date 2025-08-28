import json
import os
from typing import List, Optional

from fastapi import FastAPI, HTTPException, status
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel, Field

# --- Configuração da API ---
app = FastAPI(
    title="API de Gerenciamento de Estoque",
    description="API para gerenciar produtos e estoque.",
    version="0.1.0",
)

# --- Montar arquivos estáticos ---
app.mount("/static", StaticFiles(directory="static"), name="static")


# --- Modelos de Dados (Pydantic) ---
class ProdutoBase(BaseModel):
    nome: str = Field(..., min_length=1, description="Nome do produto")
    categoria: str = Field(..., min_length=1, description="Categoria do produto")
    preco: float = Field(..., gt=0, description="Preço do produto, deve ser maior que zero")
    quantidade: int = Field(..., ge=0, description="Quantidade em estoque")
    estoque_minimo: int = Field(..., ge=0, description="Estoque mínimo desejado")


class ProdutoCreate(ProdutoBase):
    pass


class Produto(ProdutoBase):
    id: int = Field(..., description="ID único do produto")
    alert_message: Optional[str] = Field(None, description="Mensagem de alerta para estoque baixo")


class EstoqueUpdate(BaseModel):
    quantidade: int = Field(..., gt=0, description="Quantidade a ser movimentada")


# --- Persistência de Dados ---
NOME_ARQUIVO_ESTOQUE = "estoque.json"


def carregar_estoque() -> List[Produto]:
    """Carrega o estoque do arquivo JSON."""
    if not os.path.exists(NOME_ARQUIVO_ESTOQUE):
        return []
    try:
        with open(NOME_ARQUIVO_ESTOQUE, "r", encoding="utf-8") as f:
            content = f.read()
            if not content:
                return []
            dados_brutos = json.loads(content)
            return [Produto(**p) for p in dados_brutos]
    except (json.JSONDecodeError, IOError):
        return []


def salvar_estoque(estoque_data: List[Produto]):
    """Salva o estado atual do estoque no arquivo JSON."""
    with open(NOME_ARQUIVO_ESTOQUE, "w", encoding="utf-8") as f:
        dados_serializados = [p.model_dump() for p in estoque_data]
        json.dump(dados_serializados, f, indent=4, ensure_ascii=False)


# Carrega os dados do estoque na inicialização
estoque: List[Produto] = carregar_estoque()


# --- Lógica de Negócio ---
def gerar_novo_id() -> int:
    """Gera um novo ID único para o produto."""
    return max(p.id for p in estoque) + 1 if estoque else 1


def encontrar_produto_por_id(produto_id: int) -> Optional[Produto]:
    """Encontra um produto na lista de estoque pelo seu ID."""
    for produto in estoque:
        if produto.id == produto_id:
            return produto
    return None


def verificar_alerta_estoque(produto: Produto):
    """Verifica se o estoque está baixo e atualiza a mensagem de alerta."""
    if produto.quantidade <= produto.estoque_minimo:
        produto.alert_message = f"Alerta: Estoque baixo! A quantidade atual ({produto.quantidade}) é menor ou igual ao mínimo ({produto.estoque_minimo})."
    else:
        produto.alert_message = None


# --- Endpoints da API ---
@app.get("/", response_class=HTMLResponse, include_in_schema=False)
async def get_dashboard():
    """Serve a página principal do dashboard."""
    try:
        with open("static/index.html", "r", encoding="utf-8") as f:
            return HTMLResponse(content=f.read(), status_code=status.HTTP_200_OK)
    except FileNotFoundError:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Arquivo index.html não encontrado.")


@app.get("/produtos", response_model=List[Produto], tags=["Produtos"])
def listar_produtos(nome: Optional[str] = None, categoria: Optional[str] = None) -> List[Produto]:
    """
    Lista todos os produtos no estoque.
    Permite filtrar por nome e/ou categoria (busca parcial, case-insensitive).
    """
    # Atualiza as mensagens de alerta para todos os produtos
    for p in estoque:
        verificar_alerta_estoque(p)

    resultados = estoque
    
    if nome:
        resultados = [p for p in resultados if nome.lower() in p.nome.lower()]
    
    if categoria:
        resultados = [p for p in resultados if categoria.lower() in p.categoria.lower()]
        
    return resultados


@app.get("/produtos/baixo-estoque", response_model=List[Produto], tags=["Relatórios"])
def relatorio_baixo_estoque() -> List[Produto]:
    """Retorna uma lista de produtos com quantidade igual ou inferior ao estoque mínimo."""
    produtos_baixo_estoque = [
        p for p in estoque if p.quantidade <= p.estoque_minimo
    ]
    # Garante que a mensagem de alerta esteja atualizada para os itens retornados
    for p in produtos_baixo_estoque:
        verificar_alerta_estoque(p)
    return produtos_baixo_estoque


@app.get("/produtos/{produto_id}", response_model=Produto, tags=["Produtos"])
def obter_produto(produto_id: int) -> Produto:
    """Obtém os detalhes de um produto específico."""
    produto = encontrar_produto_por_id(produto_id)
    if not produto:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Produto não encontrado")
    
    verificar_alerta_estoque(produto)
    return produto


@app.post("/produtos", response_model=Produto, status_code=status.HTTP_201_CREATED, tags=["Produtos"])
def criar_produto(produto_data: ProdutoCreate) -> Produto:
    """Cria um novo produto no estoque."""
    novo_produto = Produto(id=gerar_novo_id(), **produto_data.model_dump())
    verificar_alerta_estoque(novo_produto)
    estoque.append(novo_produto)
    salvar_estoque(estoque)
    return novo_produto


@app.post("/produtos/{produto_id}/entrada", response_model=Produto, tags=["Estoque"])
def registrar_entrada(produto_id: int, update_data: EstoqueUpdate) -> Produto:
    """Registra a entrada de uma quantidade no estoque de um produto."""
    produto = encontrar_produto_por_id(produto_id)
    if not produto:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Produto não encontrado")

    produto.quantidade += update_data.quantidade
    verificar_alerta_estoque(produto)
    salvar_estoque(estoque)
    return produto


@app.post("/produtos/{produto_id}/saida", response_model=Produto, tags=["Estoque"])
def registrar_saida(produto_id: int, update_data: EstoqueUpdate) -> Produto:
    """Registra a saída de uma quantidade do estoque de um produto."""
    produto = encontrar_produto_por_id(produto_id)
    if not produto:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Produto não encontrado")

    if produto.quantidade < update_data.quantidade:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Quantidade em estoque insuficiente para a saída.",
        )

    produto.quantidade -= update_data.quantidade
    verificar_alerta_estoque(produto)
    salvar_estoque(estoque)
    return produto


@app.delete("/produtos/{produto_id}", response_model=dict, tags=["Produtos"])
def remover_produto(produto_id: int) -> dict:
    """Remove um produto do estoque."""
    produto = encontrar_produto_por_id(produto_id)
    if not produto:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Produto não encontrado")

    estoque.remove(produto)
    salvar_estoque(estoque)
    return {"mensagem": "Produto removido com sucesso", "produto_id": produto_id}


@app.put("/produtos/{produto_id}", response_model=Produto, tags=["Produtos"])
def atualizar_produto(produto_id: int, produto_data: ProdutoCreate) -> Produto:
    """Atualiza os dados de um produto existente."""
    produto = encontrar_produto_por_id(produto_id)
    if not produto:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Produto não encontrado")

    # Atualiza os campos do produto com os dados recebidos
    produto_update_data = produto_data.model_dump(exclude_unset=True)
    for key, value in produto_update_data.items():
        setattr(produto, key, value)

    verificar_alerta_estoque(produto)
    salvar_estoque(estoque)
    return produto