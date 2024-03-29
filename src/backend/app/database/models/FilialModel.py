from database.config.Base import Base

from sqlalchemy.orm import Mapped, mapped_column, relationship

class Filial(Base):
    
    __tablename__ = "filial"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    nome: Mapped[str]
    cod_filial: Mapped[int] = mapped_column(unique=True)
    cnpj: Mapped[int]
    uf: Mapped[str]
    cep: Mapped[int]
    rua: Mapped[str]
    bairro: Mapped[str]
    numero: Mapped[int]
    
    user = relationship("User", back_populates="filial")
    
    correspondencia_interna_cod_filial_origem = relationship("CorrespondenciaInterna", foreign_keys="[CorrespondenciaInterna.cod_filial_origem]", back_populates="filial_origem")
    correspondencia_interna_cod_filial_destino = relationship("CorrespondenciaInterna", foreign_keys="[CorrespondenciaInterna.cod_filial_destino]", back_populates="filial_destino")