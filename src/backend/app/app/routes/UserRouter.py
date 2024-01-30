from fastapi import APIRouter, Request, Depends
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from app.app.database.config.db import get_session
from app.app.util.security import obter_hash_senha

from app.app.database.repositories.UserRepository import UserRepository

from app.app.database.schemas.UserSchema import UserSchema, UserLoginSchema, UserPorIdSchema


router = APIRouter()

@router.post("/user/inserir", response_model=UserSchema)
def inserir_usuario(user: UserSchema, session: Session = Depends(get_session)):
    
    if not UserRepository(session).VerificarEmailExiste(user.email):
        senha_hash = obter_hash_senha(user.senha)
        user.senha = senha_hash
        new_user = UserRepository(session).Inserir(user)
    
    return new_user