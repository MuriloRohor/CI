from sqlalchemy import delete, update
from sqlalchemy.orm import Session

from app.database.models.moldes import User

from app.database.schemas.UserSchema import UserPorIdSchema, UserSchema, UserLoginSchema
from app.database.schemas.FiltroPageSchema import FiltroSchema

class UserRepository():
    
    def __init__(self, session: Session) -> None:
        self.session = session
        
    def Inserir(self, user: UserSchema):
        db_user = User(
            nome=user.nome,
            senha=user.senha,
            token=user.token,
            image_url=user.image_url,
            filial_id=user.filial_id
        )
        
        self.session.add(db_user)
        self.session.commit()
        
        return db_user
    
    def ObterUserPorID(self, user: UserPorIdSchema):
        db_user = self.session.query(User)\
                            .filter(User.id == user.id)\
                            .first()
        return db_user
    
    def VerificarEmailExiste(self, email):
        db_user = self.session.query(User)\
                              .where(User.email == email)
                              
        return db_user
                              