from typing import List
from fastapi import APIRouter, Request, Depends
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from database.schemas.UserSchema import UserSchema
from util.message import redirecionar_com_mensagem
from util.security import obter_usuario_logado

from database.config.db import get_session

router = APIRouter()

templates = Jinja2Templates(directory="templates")

@router.get("/ci/enviados", response_class=HTMLResponse)
def get_enviados(
            request: Request,
            usuario: UserSchema = Depends(obter_usuario_logado)
            ):
    
    if not usuario:
        response = redirecionar_com_mensagem(
            "/login",
            "Faça login para se conectar!",         
        )
        return response
    
    return templates.TemplateResponse(
        "ci/enviados.html",
        {"request": request, "usuario": usuario}
    )
    
@router.get("/ci/cadastrar", response_class=HTMLResponse)
def get_criar_ci(
    request: Request,
    usuario: UserSchema = Depends(obter_usuario_logado)
):
    
    if not usuario:
        response = redirecionar_com_mensagem(
            "/login",
            "Faça login para se conectar!",         
        )
        return response
    
    return templates.TemplateResponse(
        "ci/cadastrar.html",
        {"request": request, "usuario": usuario}
    )