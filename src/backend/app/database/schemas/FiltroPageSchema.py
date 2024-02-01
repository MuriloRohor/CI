from pydantic import BaseModel
from typing import Optional

class FiltroSchema(BaseModel):
    page: int
    itens_page: Optional[int] = 10
    
    class Config:
        from_attributes = True