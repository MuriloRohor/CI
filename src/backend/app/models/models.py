from sqlalchemy import ForeignKey
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


class Base(DeclarativeBase):
    pass


class Filial(Base):
    
    __tablename__ = "filial"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    nome: Mapped[str]
    cod_filial: Mapped[str] = mapped_column(unique=True)
    cnpj: Mapped[int]
    uf: Mapped[str]
    cep: Mapped[int]
    rua: Mapped[str]
    bairro: Mapped[str]
    numero: Mapped[str]
    
    user = relationship("User", back_populates="filial")
    
    
class Status(Base):
    
    __tablename__ = "tipo_status"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    cod_status: Mapped[int] = mapped_column(unique=True)
    nome: Mapped[str]
    
    correspondencia_interna = relationship("CorrespondenciaInterna", back_populates="tipo_status")
    
    
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
    
    filial = relationship("Filial", back_populates="user", uselist=False)
    correspondencia_interna_remetente = relationship("CorrespondenciaInterna", back_populates="user_remetente")
    correspondencia_interna_destinatario = relationship("CorrespondenciaInterna", back_populates="user_destinatario")
    
    
class CorrespondenciaInterna(Base):
    
    __tablename__ = "correspondencia_interna"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    cod_ci: Mapped[int] = mapped_column(unique=True)
    user_id_remetente: Mapped[int] = mapped_column(ForeignKey("user.id"))
    user_id_destinatario: Mapped[int] = mapped_column(ForeignKey("user.id"))
    descricao: Mapped[str]
    status: Mapped[int] = mapped_column(ForeignKey("tipo_status.cod_status"))
    
    user_remetente = relationship("User", back_populates="correspondencia_interna_remetente", uselist=False)
    user_destinatario = relationship("User", back_populates="correspondencia_interna_destinatario", uselist=False)
    
    tipo_status = relationship("Status", back_populates="correspondencia_interna", uselist=False)
    
    


    
