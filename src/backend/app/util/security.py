import secrets
import bcrypt
from typing import Optional
from fastapi import Depends, Request
from sqlalchemy.orm import Session
from database.config.db import get_session

from database.repositories.UserRepository import UserRepository
from database.models.UserModel import User

async def obter_usuario_logado(request: Request, session: Session = Depends(get_session)) -> Optional[User]:
    try:
        token = request.cookies["auth_token"]
        if token.strip() == "":
            return None
        usuario = UserRepository(session).ObterPorToken(token)
        return usuario
    except KeyError:
        return None

def conferir_senha(senha: str, hash_senha: str) -> bool:
    try:
        return bcrypt.checkpw(senha.encode(), hash_senha.encode())
    except (ValueError, AttributeError):
        return False
    
def obter_hash_senha(senha: str) -> str:
    try:
        hashed = bcrypt.hashpw(senha.encode(), bcrypt.gensalt())
        return hashed.decode()
    except ValueError:
        return ""

def gerar_token(length: int = 32) -> str:
    try:
        return secrets.token_hex(length)
    except ValueError:
        return ""
    
def criar_cookie_autenticacao(response, token):
    response.set_cookie(
        key="auth_token",
        value=token,
        max_age=1800,
        httponly=True,
        samesite="lax",
    )
    return response

def excluir_cookie_autenticacao(response):
    response.delete_cookie(key="auth_token")
    return response