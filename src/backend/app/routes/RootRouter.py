from typing import List
from fastapi import APIRouter, Query, Request, Depends, status
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session

from app.util.message import adicionar_cookie_mensagem, redirecionar_com_mensagem
from app.util.security import conferir_senha, criar_cookie_autenticacao, gerar_token

from database.repositories.UserRepository import UserRepository
from database.schemas.UserSchema import UserSchema, UserLoginSchema, UserPorIdSchema, UserSchemaRegister

router = APIRouter()

@router.post("/login")
async def login_user(
    user: UserLoginSchema,
    return_url = Query("/")
):
    senha_hash_db = UserRepository.ObterHashPorEmail(user.email)
    if conferir_senha(user.senha, senha_hash_db):
        token = gerar_token()
        UserRepository.AlterarTokenPorEmail(user.email, token)
        response = RedirectResponse(return_url, status.HTTP_302_FOUND)
        criar_cookie_autenticacao(response, token)
        adicionar_cookie_mensagem(response, "Login efetuado!")
    else:
        response = redirecionar_com_mensagem(
            "/login",
            "Credenciais inválidas!"
        )
        
    return response
        
    