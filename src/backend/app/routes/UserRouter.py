from typing import List
from fastapi import APIRouter, Request, Depends
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from util.message import redirecionar_com_mensagem
from database.config.db import get_session
from util.security import obter_hash_senha, obter_usuario_logado

from database.repositories.UserRepository import UserRepository

from database.schemas.UserSchema import ListagemUsuarioSchema, UserSchema, UserLoginSchema, UserPorIdSchema, UserSchemaRegister

from database.schemas.FiltroSchema import FiltroPorFilialSchema

router = APIRouter()

@router.post("/user/inserir", response_model=UserSchemaRegister)
def inserir_usuario(user: UserSchemaRegister, session: Session = Depends(get_session)):
    
    if not UserRepository(session).VerificarEmailExiste(user.email):
        senha_hash = obter_hash_senha(user.senha)
        user.senha = senha_hash
        new_user = UserRepository(session).Inserir(user)
        
    return new_user

@router.get("/user/filtrar-por-filial", response_model=List[ListagemUsuarioSchema])
def filtrar_usuario_por_nome_e_filial(
    filtro: FiltroPorFilialSchema, 
    session: Session = Depends(get_session), 
    usuario: UserSchema = Depends(obter_usuario_logado)
    ):
    
    #if not usuario:
        #response = redirecionar_com_mensagem(
            #"/login",
            #"Faça login para se conectar!",         
        #)
        #return response

    list_user = UserRepository(session).ListarUsuariosPorFilialeNome(filtro)
    
    return list_user
    
    
