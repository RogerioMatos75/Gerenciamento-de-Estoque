import json
import os
from typing import List, Optional

from fastapi import FastAPI, status, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from pydantic import BaseModel, Field

# --- Configuração da API ---
app = FastAPI(
    title="API de Gerenciamento de Estoque",
    description="API para gerenciar produtos e estoque.",
    version="0.1.0"
)

# --- Montar arquivos estáticos ---
app.mount("/static", StaticFiles(directory="static"), name="static")


# --- Modelos de Dados (Pydantic) ---
class ProdutoBase(BaseModel):
    nome: str = Field(..., min_length=1, description="Nome do produto")
    categoria: str = Field(..., min_length=1, description="Categoria do produto")
    preco: float = Field(..., gt=0, description="Preço do produto, deve ser maior que zero")
    quantidade: int = Field(..., ge=0, description="Quantidade em estoque, deve ser maior ou igual a zero")
    estoque_minimo: int = Field(..., ge=0, description="Estoque mínimo desejado, deve ser maior ou igual a zero")

class ProdutoCreate(ProdutoBase):
    pass

import json
import os
from typing import List, Optional

from fastapi import FastAPI, status, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from pydantic import BaseModel, Field

# --- Configuração da API ---
app = FastAPI(
    title="API de Gerenciamento de Estoque",
    description="API para gerenciar produtos e estoque.",
    version="0.1.0"
)

# --- Montar arquivos estáticos ---
app.mount("/static", StaticFiles(directory="static"), name="static")


# --- Modelos de Dados (Pydantic) ---
class ProdutoBase(BaseModel):
    nome: str = Field(..., min_length=1, description="Nome do produto")
    categoria: str = Field(..., min_length=1, description="Categoria do produto")
    preco: float = Field(..., gt=0, description="Preço do produto, deve ser maior que zero")
    quantidade: int = Field(..., ge=0, description="Quantidade em estoque, deve ser maior ou igual a zero")
    estoque_minimo: int = Field(..., ge=0, description="Estoque mínimo desejado, deve ser maior ou igual a zero")

class ProdutoCreate(ProdutoBase):
    pass

class Produto(ProdutoBase):
    id: int = Field(..., description="ID único do produto")
    alert_message: Optional[str] = None # Novo campo para mensagens de alerta

class EstoqueUpdate(BaseModel):
    quantidade: int = Field(..., gt=0, description="Quantidade a ser adicionada ou removida, deve ser maior que zero")


# --- Persistência de Dados ---
NOME_ARQUIVO_ESTOQUE = "estoque.json"

def carregar_estoque() -> List[Produto]:
    """Carrega o estoque do arquivo JSON."""
    if not os.path.exists(NOME_ARQUIVO_ESTOQUE):
        return []
    try:
        with open(NOME_ARQUIVO_ESTOQUE, 'r', encoding='utf-8') as f:
            content = f.read()
            if not content:
                return []
            dados_brutos = json.loads(content)
            # Garante que o campo alert_message seja inicializado para produtos existentes
            return [Produto(**p, alert_message=p.get('alert_message')) for p in dados_brutos]
    except (json.JSONDecodeError, IOError):
        return []

def salvar_estoque(estoque_data: List[Produto]):
    """Salva o estado atual do estoque no arquivo JSON."""
    with open(NOME_ARQUIVO_ESTOQUE, 'w', encoding='utf-8') as f:
        dados_serializados = [p.model_dump() for p in estoque_data]
        json.dump(dados_serializados, f, indent=4, ensure_ascii=False)

# Carrega os dados do estoque na inicialização da API
estoque: List[Produto] = carregar_estoque()

# --- Lógica de Negócio ---
def gerar_novo_id() -> int:
    """Gera um novo ID único para o produto."""
    if not estoque:
        return 1
    return max(produto.id for produto in estoque) + 1

def encontrar_produto_por_id(produto_id: int) -> Optional[Produto]:
    """Encontra um produto na lista de estoque pelo seu ID."""
    for produto in estoque:
        if produto.id == produto_id:
            return produto
    return None

# --- Endpoints ---

@app.get("/", response_class=HTMLResponse)
async def get_dashboard():
    """Serve a página principal do dashboard."""
    try:
        with open("static/index.html", "r", encoding="utf-8") as f:
            return HTMLResponse(content=f.read(), status_code=200)
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail="index.html não encontrado")

@app.post("/produtos", response_model=Produto, status_code=status.HTTP_201_CREATED, tags=["Produtos"])
def criar_produto(produto_data: ProdutoCreate) -> Produto:
    """Cria um novo produto no estoque."""
    novo_id = gerar_novo_id()
    produto_novo = Produto(id=novo_id, **produto_data.model_dump())
    estoque.append(produto_novo)
    salvar_estoque(estoque)
    return produto_novo

@app.get("/produtos", response_model=List[Produto], tags=["Produtos"])
def listar_produtos(nome: Optional[str] = None) -> List[Produto]:
    """Lista todos os produtos no estoque."""
    if nome:
        return [p for p in estoque if nome.lower() in p.nome.lower()]
    return estoque

@app.get("/produtos/{produto_id}", response_model=Produto, tags=["Produtos"])
def obter_produto_por_id(produto_id: int):
    """Obtém os detalhes de um produto específico pelo seu ID."""
    produto = encontrar_produto_por_id(produto_id)
    if not produto:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Produto não encontrado")
    return produto

@app.post("/produtos/{produto_id}/entrada", response_model=Produto, tags=["Estoque"])
def registrar_entrada(produto_id: int, update_data: EstoqueUpdate):
    """Registra a entrada de uma quantidade no estoque de um produto."""
    produto = encontrar_produto_por_id(produto_id)
    if not produto:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Produto não encontrado")
    
    produto.quantidade += update_data.quantidade
    
    # Verifica alerta de estoque baixo
    if produto.quantidade <= produto.estoque_minimo:
        produto.alert_message = f"ATENÇÃO: Estoque de {produto.nome} ({produto.quantidade}) está abaixo ou igual ao mínimo ({produto.estoque_minimo})!"
    else:
        produto.alert_message = None # Limpa a mensagem se o estoque subiu acima do mínimo
        
    salvar_estoque(estoque)
    return produto

@app.post("/produtos/{produto_id}/saida", response_model=Produto, tags=["Estoque"])
def registrar_saida(produto_id: int, update_data: EstoqueUpdate):
    """Registra a saída de uma quantidade no estoque de um produto."""
    produto = encontrar_produto_por_id(produto_id)
    if not produto:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Produto não encontrado")
    
    if produto.quantidade < update_data.quantidade:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Quantidade em estoque insuficiente para a saída.")
        
    produto.quantidade -= update_data.quantidade
    
    # Verifica alerta de estoque baixo
    if produto.quantidade <= produto.estoque_minimo:
        produto.alert_message = f"ATENÇÃO: Estoque de {produto.nome} ({produto.quantidade}) está abaixo ou igual ao mínimo ({produto.estoque_minimo})!"
    else:
        produto.alert_message = None # Limpa a mensagem se o estoque subiu acima do mínimo
        
    salvar_estoque(estoque)
    return produto


class EstoqueUpdate(BaseModel):
    quantidade: int = Field(..., gt=0, description="Quantidade a ser adicionada ou removida, deve ser maior que zero")


# --- Persistência de Dados ---
NOME_ARQUIVO_ESTOQUE = "estoque.json"

def carregar_estoque() -> List[Produto]:
    """Carrega o estoque do arquivo JSON."""
    if not os.path.exists(NOME_ARQUIVO_ESTOQUE):
        return []
    try:
        with open(NOME_ARQUIVO_ESTOQUE, 'r', encoding='utf-8') as f:
            content = f.read()
            if not content:
                return []
            dados_brutos = json.loads(content)
            return [Produto(**p) for p in dados_brutos]
    except (json.JSONDecodeError, IOError):
        return []

def salvar_estoque(estoque_data: List[Produto]):
    """Salva o estado atual do estoque no arquivo JSON."""
    with open(NOME_ARQUIVO_ESTOQUE, 'w', encoding='utf-8') as f:
        dados_serializados = [p.model_dump() for p in estoque_data]
        json.dump(dados_serializados, f, indent=4, ensure_ascii=False)

# Carrega os dados do estoque na inicialização da API
estoque: List[Produto] = carregar_estoque()

# --- Lógica de Negócio ---
def gerar_novo_id() -> int:
    """Gera um novo ID único para o produto."""
    if not estoque:
        return 1
    return max(produto.id for produto in estoque) + 1

def encontrar_produto_por_id(produto_id: int) -> Optional[Produto]:
    """Encontra um produto na lista de estoque pelo seu ID."""
    for produto in estoque:
        if produto.id == produto_id:
            return produto
    return None

# --- Endpoints ---

@app.get("/", response_class=HTMLResponse)
async def get_dashboard():
    """Serve a página principal do dashboard."""
    try:
        with open("static/index.html", "r", encoding="utf-8") as f:
            return HTMLResponse(content=f.read(), status_code=200)
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail="index.html não encontrado")

@app.post("/produtos", response_model=Produto, status_code=status.HTTP_201_CREATED, tags=["Produtos"])
def criar_produto(produto_data: ProdutoCreate) -> Produto:
    """Cria um novo produto no estoque."""
    novo_id = gerar_novo_id()
    produto_novo = Produto(id=novo_id, **produto_data.model_dump())
    estoque.append(produto_novo)
    salvar_estoque(estoque)
    return produto_novo

@app.get("/produtos", response_model=List[Produto], tags=["Produtos"])
def listar_produtos(nome: Optional[str] = None) -> List[Produto]:
    """Lista todos os produtos no estoque."""
    if nome:
        return [p for p in estoque if nome.lower() in p.nome.lower()]
    return estoque

@app.get("/produtos/{produto_id}", response_model=Produto, tags=["Produtos"])
def obter_produto_por_id(produto_id: int):
    """Obtém os detalhes de um produto específico pelo seu ID."""
    produto = encontrar_produto_por_id(produto_id)
    if not produto:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Produto não encontrado")
    return produto

@app.post("/produtos/{produto_id}/entrada", response_model=Produto, tags=["Estoque"])
def registrar_entrada(produto_id: int, update_data: EstoqueUpdate):
    """Registra a entrada de uma quantidade no estoque de um produto."""
    produto = encontrar_produto_por_id(produto_id)
    if not produto:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Produto não encontrado")
    
    produto.quantidade += update_data.quantidade
    salvar_estoque(estoque)
    return produto

@app.post("/produtos/{produto_id}/saida", response_model=Produto, tags=["Estoque"])
def registrar_saida(produto_id: int, update_data: EstoqueUpdate):
    """Registra a saída de uma quantidade no estoque de um produto."""
    produto = encontrar_produto_por_id(produto_id)
    if not produto:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Produto não encontrado")
    
    if produto.quantidade < update_data.quantidade:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Quantidade em estoque insuficiente para a saída.")
        
    produto.quantidade -= update_data.quantidade
    salvar_estoque(estoque)
    return produto
