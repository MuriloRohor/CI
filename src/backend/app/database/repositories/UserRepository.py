from sqlalchemy import delete, func, update
from sqlalchemy.orm import Session

from database.models.moldes import User

from database.schemas.UserSchema import UserPorIdSchema, UserSchema, UserLoginSchema
from database.schemas.FiltroSchema import FiltroPorFilialSchema, FiltroSchema

class UserRepository():
    
    def __init__(self, session: Session) -> None:
        self.session = session
        
    def Inserir(self, user: UserSchema):
        db_user = User(
            cod_matricula=user.cod_matricula,
            nome=user.nome,
            email=user.email,
            senha=user.senha,
            token="",
            image_url=user.image_url,
            cod_filial=user.cod_filial
        )
        
        self.session.add(db_user)
        self.session.commit()
        
        return db_user
    
    def AlterarPorID(self, user: UserSchema):
        db_user = update(User)\
                  .where(User.id == user.id)\
                  .values(
                        cod_matricula=user.cod_matricula,
                        nome=user.nome,
                        email=user.email,
                        cod_filial=user.cod_filial
                  )
        self.session.execute(db_user)
        self.session.commit()
        
        return "Usuário Alterado!"
    
    def ObterUserPorID(self, user: UserPorIdSchema):
        db_user = self.session.query(User)\
                            .filter(User.id == user.id)\
                            .first()
                      
        return db_user
    
    def ObterPorToken(self, token: str):
        db_user = self.session.query(User)\
                              .filter(User.token == token)\
                              .first()
                              
        return db_user
    
    def ObterHashPorEmail(self, email: str):
        db_user = self.session.query(User.senha)\
                              .filter(User.email == email)\
                              .first()
        if db_user:
            return db_user[0]
        return None
    
    def AlterarTokenPorEmail(self, email: str, new_token: str):
        db_user = update(User)\
                  .where(User.email == email)\
                  .values(token = new_token)
                  
        self.session.execute(db_user)
        self.session.commit()
        
        return True
    
    
    def VerificarEmailExiste(self, email):
        db_user = self.session.query(User)\
                              .filter(User.email == email)\
                              .first()
                              
        if db_user:
            return True
        
        return False
    
    def ListarUsuariosPorFilialeNome(self, filtro: FiltroPorFilialSchema):
        offset = (filtro.page - 1) * filtro.itens_page
        
        db_user = self.session.query(User)\
                              .filter(func.lower(User.nome).contains(func.lower(filtro.nome_usuario)))\
                              .filter(User.cod_filial == filtro.cod_filial)\
                              .limit(filtro.itens_page)\
                              .offset(offset)\
                              .all()
        return db_user
    
        
        
        
                              