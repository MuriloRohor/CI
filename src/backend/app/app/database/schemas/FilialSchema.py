from pydantic import BaseModel
from typing import Optional

class FilialSchema(BaseModel):
    id: Optional[int] = None
    nome: str
    cod_filial: int
    cnpj:int
    uf:str
    cep:int
    rua:str
    bairro:str
    numero:int
    
    class Config:
        from_attributes = True

class FilialPorIdSchema(BaseModel):
    id: int
      
    class Config:
        from_attributes = True
