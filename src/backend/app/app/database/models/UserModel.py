from app.database.config.Base import Base

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship


class User(Base):
    
    __tablename__ = "user"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    cod_matricula: Mapped[int] = mapped_column(unique=True)
    nome: Mapped[str]
    email: Mapped[str]
    senha: Mapped[str]
    token: Mapped[str]
    image_url: Mapped[str]
    filial_id: Mapped[int] = mapped_column(ForeignKey("filial.id"))
    
    filial = relationship("Filial", back_populates="user")
    correspondencia_interna_remetente = relationship("CorrespondenciaInterna", foreign_keys="[CorrespondenciaInterna.user_id_remetente]", back_populates="user_remetente")
    correspondencia_interna_destinatario = relationship("CorrespondenciaInterna", foreign_keys="[CorrespondenciaInterna.user_id_destinatario]", back_populates="user_destinatario")