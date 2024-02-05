from datetime import datetime

from database.config.Base import Base
from sqlalchemy import Integer, Sequence, func
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

cod_ci_seq = Sequence('cod_ci_seq', start=1, increment=1)


class CorrespondenciaInterna(Base):
    
    __tablename__ = "correspondencia_interna"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    cod_ci: Mapped[int] = mapped_column(Integer, cod_ci_seq, server_default=cod_ci_seq.next_value(), unique=True)
    user_id_remetente: Mapped[int] = mapped_column(ForeignKey("user.id"))
    user_id_destinatario: Mapped[int] = mapped_column(ForeignKey("user.id"))
    cod_filial_origem: Mapped[int] = mapped_column(ForeignKey("filial.cod_filial"))
    cod_filial_destino: Mapped[int] = mapped_column(ForeignKey("filial.cod_filial"))
    data_criacao: Mapped[datetime] = mapped_column(insert_default=func.now())
    data_entrega: Mapped[datetime]
    descricao: Mapped[str]
    status: Mapped[int] = mapped_column(ForeignKey("tipo_status.cod_status"))
    
    user_remetente = relationship("User", foreign_keys="[CorrespondenciaInterna.user_id_remetente]", back_populates="correspondencia_interna_remetente", uselist=False)
    user_destinatario = relationship("User", foreign_keys="[CorrespondenciaInterna.user_id_destinatario]", back_populates="correspondencia_interna_destinatario", uselist=False)
    
    filial_origem = relationship("Filial", foreign_keys="[CorrespondenciaInterna.cod_filial_origem]", back_populates="correspondencia_interna_cod_filial_origem", uselist=False)
    filial_destino = relationship("Filial", foreign_keys="[CorrespondenciaInterna.cod_filial_destino]", back_populates="correspondencia_interna_cod_filial_destino", uselist=False)
    
    tipo_status = relationship("Status", back_populates="correspondencia_interna", uselist=False)