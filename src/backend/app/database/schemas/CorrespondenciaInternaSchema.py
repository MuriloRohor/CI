from datetime import datetime
from pydantic import BaseModel
from typing import Optional

class CorrespondenciaInternaSchema(BaseModel):
    id: Optional[int] = None
    cod_ci: Optional[int] = None
    user_id_remetente: int
    user_id_destinatario: int
    cod_filial_origem: int
    cod_filial_destino: int
    data_criacao: Optional[datetime] = None
    data_entrega: Optional[datetime] = None
    descricao: str
    status: Optional[int] = None
    
    class Config:
        from_attributes = True

class CorrespondenciaInternaCodCiSchema(BaseModel):
    cod_ci: int
    
    class Config:
        from_attributes = True
    