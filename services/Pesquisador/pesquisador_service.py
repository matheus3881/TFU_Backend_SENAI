from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from schemas.Pesquisador.pokemon import PokemonCriacao

def cadastrar_nova_especie(db: Session, dados: PokemonCriacao):
    raise HTTPException(
        status_code=status.HTTP_501_NOT_IMPLEMENTED,
        detail="Lógica de inserção depende do model Pokemon que será feito na API Pública."
    )