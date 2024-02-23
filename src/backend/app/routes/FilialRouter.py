from typing import List
from fastapi import APIRouter, Request, Depends
from sqlalchemy.orm import Session

from database.config.db import get_session

from database.repositories.FilialRepository import FilialRepository

from database.schemas.FilialSchema import FilialSchema, FilialPorIdSchema
from database.schemas.FiltroSchema import FiltroSchema

router = APIRouter()

@router.get("/filial/listar", response_model=List[FilialSchema])
def get_filiais_page(filtro: FiltroSchema, session: Session = Depends(get_session)):
    filial = FilialRepository(session).ListarFiliaisPorPag(filtro)
    return filial

@router.post("/filial/inserir", response_model=FilialSchema)
def inserir_filial(filial: FilialSchema, session: Session = Depends(get_session)):
    new_filial = FilialRepository(session).Inserir(filial)
    return new_filial

@router.post("/filial/alterar", response_model=FilialSchema)
def alterar_filial(filial: FilialSchema, session: Session = Depends(get_session)):
    filial_alterada = FilialRepository(session).AlterarFilialPorID(filial)
    return filial_alterada
    
    

