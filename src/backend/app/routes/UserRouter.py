from fastapi import APIRouter, Request, Depends
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from database.config.db import get_session
from util.security import obter_hash_senha

from database.repositories.UserRepository import UserRepository

from database.schemas.UserSchema import UserSchema, UserLoginSchema, UserPorIdSchema, UserSchemaRegister

router = APIRouter()

@router.post("/user/inserir", response_model=UserSchemaRegister)
def inserir_usuario(user: UserSchemaRegister, session: Session = Depends(get_session)):
    
    if not UserRepository(session).VerificarEmailExiste(user.email):
        senha_hash = obter_hash_senha(user.senha)
        user.senha = senha_hash
        new_user = UserRepository(session).Inserir(user)
    
    return new_user
