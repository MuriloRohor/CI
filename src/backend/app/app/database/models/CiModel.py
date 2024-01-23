from app.database.config.Base import Base

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship


class CorrespondenciaInterna(Base):
    
    __tablename__ = "correspondencia_interna"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    cod_ci: Mapped[int] = mapped_column(unique=True)
    user_id_remetente: Mapped[int] = mapped_column(ForeignKey("user.id"))
    user_id_destinatario: Mapped[int] = mapped_column(ForeignKey("user.id"))
    descricao: Mapped[str]
    status: Mapped[int] = mapped_column(ForeignKey("tipo_status.cod_status"))
    
    user_remetente = relationship("User", foreign_keys="[CorrespondenciaInterna.user_id_remetente]", back_populates="correspondencia_interna_remetente", uselist=False)
    user_destinatario = relationship("User", foreign_keys="[CorrespondenciaInterna.user_id_destinatario]", back_populates="correspondencia_interna_destinatario", uselist=False)
    
    tipo_status = relationship("Status", back_populates="correspondencia_interna", uselist=False)