from app.database.config.Base import Base

from sqlalchemy.orm import Mapped, mapped_column, relationship

class Status(Base):
    
    __tablename__ = "tipo_status"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    cod_status: Mapped[int] = mapped_column(unique=True)
    nome: Mapped[str]
    
    correspondencia_interna = relationship("CorrespondenciaInterna", back_populates="tipo_status")