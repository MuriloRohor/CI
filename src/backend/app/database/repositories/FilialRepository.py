from sqlalchemy import delete, update
from sqlalchemy.orm import Session

from app.database.models.FilialModel import Filial
from app.database.schemas.FilialSchema import FilialPorIdSchema, FilialSchema
from app.database.schemas.FiltroPageSchema import FiltroSchema
class FilialRepository():
    
    def __init__(self, session: Session) -> None:
        self.session = session
        
    def Inserir(self, filial: FilialSchema):
        db_filial = Filial(
            nome=filial.nome,
            cod_filial=filial.cod_filial,
            cnpj=filial.cnpj,
            uf=filial.uf,
            cep=filial.cep,
            rua=filial.rua,
            bairro=filial.bairro,
            numero=filial.numero
        )
        
        self.session.add(db_filial)
        self.session.commit()
        
        return db_filial
    
    def ObterFilialPorID(self, filial: FilialPorIdSchema):
        db_filial = self.session.query(Filial)\
                    .filter(Filial.id == filial.id)\
                    .first()
                    
        return db_filial
        
    
    def ListarFiliaisPorPag(self, filtro: FiltroSchema):
        offset = (filtro.page -1) * filtro.itens_page
        
        db_filial = self.session.query(Filial)\
                                .limit(filtro.itens_page)\
                                .offset(offset)\
                                .all()
                                
        return db_filial
        
        
    def AlterarFilialPorID(self, filial: FilialSchema):
        db_filial = update(Filial)\
                    .where(Filial.id == filial.id)\
                    .values(
                        nome=filial.nome,
                        cod_filial=filial.cod_filial,
                        cnpj=filial.cnpj,
                        uf=filial.uf,
                        cep=filial.cep,
                        rua=filial.rua,
                        bairro=filial.bairro,
                        numero=filial.numero
                    )
        self.session.execute(db_filial)
        self.session.commit()
        
        db_filial_alterada = self.session.query(Filial)\
                                         .filter(Filial.cod_filial == filial.cod_filial)\
                                         .first()
        return db_filial_alterada                              
                    
    
    
    def RemoverFilialPorID(self, filial: FilialPorIdSchema):
        db_filial = delete(Filial)\
                    .where(Filial.id == filial.id)
   
        self.session.execute(db_filial)
        self.session.commit()
        
        return {"message": f"Filial Deletada Com Sucesso!"}
        
    
    
        
        