from pydantic import BaseModel
from typing import Optional, List
from model.produto import Produto

from schemas import ComentarioSchema


class ProdutoSchema(BaseModel):
    
    nome: str = "Hedera helix"
    quantidade: Optional[int] = 12
    valor: float = 12.50
    mgmL: float = 20.50


class ProdutoBuscaSchema(BaseModel):
    
    nome: str = "Teste"


class ListagemProdutosSchema(BaseModel):
    
    produtos:List[ProdutoSchema]


def apresenta_produtos(produtos: List[Produto]):
    
    result = []
    for produto in produtos:
        result.append({
            "nome": produto.nome,
            "quantidade": produto.quantidade,
            "valor": produto.valor,
            "mgmL": produto.mgmL
        })

    return {"produtos": result}


class ProdutoViewSchema(BaseModel):
    
    id: int = 1
    nome: str = "Hedera helix"
    quantidade: Optional[int] = 12
    valor: float = 12.50
    mgmL: float = 20.50
    total_cometarios: int = 1
    comentarios:List[ComentarioSchema]


class ProdutoDelSchema(BaseModel):
    
    mesage: str
    nome: str

def apresenta_produto(produto: Produto):
   
    return {
        "id": produto.id,
        "nome": produto.nome,
        "quantidade": produto.quantidade,
        "mgmL": produto.mgmL,
        "valor": produto.valor,
        "total_cometarios": len(produto.comentarios),
        "comentarios": [{"texto": c.texto} for c in produto.comentarios]
    }