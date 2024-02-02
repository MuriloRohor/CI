from typing import List
from fastapi import APIRouter, Query, Request, Depends, status
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session
from database.config.db import get_session

from util.message import adicionar_cookie_mensagem, redirecionar_com_mensagem
from util.security import conferir_senha, criar_cookie_autenticacao, excluir_cookie_autenticacao, gerar_token, obter_usuario_logado

from database.repositories.UserRepository import UserRepository
from database.schemas.UserSchema import UserSchema, UserLoginSchema, UserPorIdSchema, UserSchemaRegister


router = APIRouter()


@router.post("/login")
async def login_user(
    user: UserLoginSchema,
    return_url = Query("/"),
    session: Session = Depends(get_session)
):
    senha_hash_db = UserRepository(session).ObterHashPorEmail(user.email)
    if conferir_senha(user.senha, senha_hash_db):
        token = gerar_token()
        UserRepository(session).AlterarTokenPorEmail(user.email, token)
        response = RedirectResponse(return_url, status.HTTP_302_FOUND)
        criar_cookie_autenticacao(response, token)
        adicionar_cookie_mensagem(response, "Login efetuado!")
    else:
        response = redirecionar_com_mensagem(
            "/login",
            "Credenciais inválidas!"
        )
        
    return response


@router.get("/logout")
async def get_logout(usuario: UserSchema = Depends(obter_usuario_logado), session = Depends(get_session)):
    if usuario:
        UserRepository(session).AlterarTokenPorEmail(usuario.email, "")
    response = RedirectResponse("/", status.HTTP_302_FOUND)
    excluir_cookie_autenticacao(response)
    adicionar_cookie_mensagem(response, "Saída realizada com sucesso.")
    return response
        
    