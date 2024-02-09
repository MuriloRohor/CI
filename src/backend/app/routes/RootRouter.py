from typing import List
from fastapi import APIRouter, Form, Query, Request, Depends, status
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from database.config.db import get_session

from util.message import adicionar_cookie_mensagem, redirecionar_com_mensagem
from util.security import conferir_senha, criar_cookie_autenticacao, excluir_cookie_autenticacao, gerar_token, obter_usuario_logado

from database.repositories.UserRepository import UserRepository
from database.schemas.UserSchema import UserSchema, UserLoginSchema, UserPorIdSchema, UserSchemaRegister


router = APIRouter()

templates = Jinja2Templates(directory="templates")

@router.get("/login", response_class=HTMLResponse)
def get_login(request: Request):
    return templates.TemplateResponse(
        "login.html",
        {"request": request}
    )

@router.post("/login")
async def login_user(
    email: str = Form(...),
    senha: str = Form(...),
    return_url = Query("/"),
    session: Session = Depends(get_session)
):
    user = UserLoginSchema(email=email, senha=senha)
    
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
        
    