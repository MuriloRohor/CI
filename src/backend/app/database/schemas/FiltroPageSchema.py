from pydantic import BaseModel
from typing import Optional

class FiltroSchema():
    page: int
    itens_page: Optional[int] = 10