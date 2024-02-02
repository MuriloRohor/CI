from sqlalchemy import delete, update
from sqlalchemy.orm import Session

from database.models.CiModel import CorrespondenciaInterna


class CorrespondenciaInternaRepository:
    
    def __init__(self, session: Session) -> None:
        self.session = session
        
    