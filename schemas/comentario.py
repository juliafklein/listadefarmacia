from pydantic import BaseModel


class ComentarioSchema(BaseModel):
    
    produto_id: int = 1
    texto: str = "Só comprar se o preço realmente estiver bom!"