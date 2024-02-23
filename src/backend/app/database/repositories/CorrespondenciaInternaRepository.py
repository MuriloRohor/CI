from datetime import datetime
from sqlalchemy import delete, update
from sqlalchemy.orm import Session

from app.database.models.StatusModel import Status
from app.database.schemas.CorrespondenciaInternaSchema import CorrespondenciaInternaCodCiSchema, CorrespondenciaInternaSchema
from app.database.schemas.FiltroSchema import FiltroSchema
from app.database.schemas.UserSchema import UserPorIdSchema, UserSchema

from database.models.CiModel import CorrespondenciaInterna


class CorrespondenciaInternaRepository:
    
    def __init__(self, session: Session) -> None:
        self.session = session
        
    def Inserir(self, ci: CorrespondenciaInternaSchema):
        db_ci = CorrespondenciaInterna(
            user_id_remetente=ci.user_id_remetente,
            user_id_destinatario=ci.user_id_destinatario,
            cod_filial_origem=ci.cod_filial_origem,
            cod_filial_destino=ci.cod_filial_destino,
            descricao=ci.descricao,
            status=1
        )
        self.session.add(db_ci)
        self.session.commit()
    
    def AlterarStatusParaEntregue(self, ci: CorrespondenciaInternaCodCiSchema):
        date_now = datetime.now()
        db_ci =  update(CorrespondenciaInterna)\
                 .where(CorrespondenciaInterna.cod_ci == ci.cod_ci)\
                 .values(
                        status=2,
                        data_entrega=date_now
                        )
        self.session.execute(db_ci)
        self.session.commit()
    
    def ListarCiEnviados(self, user: UserPorIdSchema, filtro: FiltroSchema):
        offset = (filtro.page -1) * filtro.itens_page
        
        db_ci = self.session.query(CorrespondenciaInterna)\
                            .filter(CorrespondenciaInterna.user_id_remetente == user.id)\
                            .limit(filtro.itens_page)\
                            .offset(offset)\
                            .all()
        return db_ci
                            
    
    def InserirStatusPadrao(self):
        db_status_enviado = Status(
            cod_status=1,
            nome="Enviado"
        )
        
        db_status_recebido = Status(
            cod_status=2,
            nome="Recebido"
        )
        
        self.session.add(db_status_enviado)
        self.session.add(db_status_recebido)
        self.session.commit()
        
        
    