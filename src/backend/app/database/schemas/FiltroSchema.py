from pydantic import BaseModel
from typing import Optional

class FiltroSchema(BaseModel):
    page: int
    itens_page: Optional[int] = 10
    
    class Config:
        from_attributes = True
        
class FiltroPorFilialSchema(BaseModel):
    page: int
    itens_page: int = 10
    cod_filial: int
    nome_usuario: Optional[str] = None
    
    class Config:
        from_attributes = True