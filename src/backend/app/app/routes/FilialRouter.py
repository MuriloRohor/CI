from typing import List
from fastapi import APIRouter, Request, Depends
from sqlalchemy.orm import Session

from app.database.config.db import get_session

from app.database.repositories.FilialRepository import FilialRepository

from app.database.schemas.FilialSchema import FilialSchema, FilialPorIdSchema
from app.database.schemas.FiltroPageSchema import FiltroSchema

router = APIRouter()

@router.get("/filial/listar", response_model=List[FilialSchema])
def get_filiais_page(filtro: FiltroSchema, session: Session = Depends(get_session)):
    print("1")
    filial = FilialRepository(session).ListarFiliaisPorPag(filtro)
    print("2")
    return filial

@router.post("/filial/inserir", response_model=FilialSchema)
def inserir_filial(filial: FilialSchema, session: Session = Depends(get_session)):
    new_filial = FilialRepository(session).Inserir(filial)
    return new_filial

@router.post("/filial/alterar", response_model=FilialSchema)
def alterar_filial(filial: FilialSchema, session: Session = Depends(get_session)):
    filial_alterada = FilialRepository(session).AlterarFilialPorID(filial)
    return filial_alterada
    
    

