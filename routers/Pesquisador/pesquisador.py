from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from database import get_db
from dependencias import obter_usuario_logado

from schemas.Pesquisador.proposta import PropostaCriacao, PropostaResposta
from schemas.Pesquisador.pokemon import PokemonCriacao, PokemonResposta
from services.Pesquisador import proposta_service, pesquisador_service

router = APIRouter(prefix="/pesquisador", tags=["Pesquisador"])

def verificar_pesquisador(usuario = Depends(obter_usuario_logado)):
    if getattr(usuario, "role", None) != "PESQUISADOR":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Acesso restrito ao perfil de Pesquisador."
        )
    return usuario

@router.post("/propostas", response_model=PropostaResposta, status_code=status.HTTP_201_CREATED)
def propor_alteracao(
    proposta_in: PropostaCriacao,
    db: Session = Depends(get_db),
    usuario = Depends(verificar_pesquisador)
):
    return proposta_service.criar_proposta_alteracao(db, proposta_in, usuario.id)

@router.get("/propostas", response_model=List[PropostaResposta], status_code=status.HTTP_200_OK)
def listar_minhas_propostas(
    db: Session = Depends(get_db),
    usuario = Depends(verificar_pesquisador)
):
    return proposta_service.listar_propostas_pesquisador(db, usuario.id)

@router.get("/propostas/{proposta_id}", response_model=PropostaResposta, status_code=status.HTTP_200_OK)
def obter_proposta(
    proposta_id: int,
    db: Session = Depends(get_db),
    usuario = Depends(verificar_pesquisador)
):
    return proposta_service.buscar_proposta_por_id(db, proposta_id, usuario.id)