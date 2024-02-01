from sqlalchemy import delete, update
from sqlalchemy.orm import Session

from database.models.moldes import User

from database.schemas.UserSchema import UserPorIdSchema, UserSchema, UserLoginSchema
from database.schemas.FiltroPageSchema import FiltroSchema

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
    
    
        
        
        
                              