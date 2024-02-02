from pydantic import BaseModel
from typing import Optional

class CorrespondenciaInternaSchema(BaseModel):
    id: Optional[int] = None
    cod_ci: int
    user_id_remetente: int
    user_id_destinatario: int
    cod_filial_origem: int
    cod_filial_destino: int
    descricao: str
    status: int
    