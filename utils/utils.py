from typing import TypeVar

from fastapi import HTTPException,status

from database import Base

T = TypeVar("T", bound=Base)

def obter_ou_404(session, model: type[T], id, nome: str) -> T:
    obj = session.get(model,id)
    if obj is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"{nome} não encontrado!")
    return obj