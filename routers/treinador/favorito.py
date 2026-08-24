from fastapi import APIRouter

from schemas.treinador.favorito import (
    CriarFavorito,
    FavoritoResposta
)

router = APIRouter(
    prefix="/treinador/favoritos",
    tags=["Treinador - Favoritos"]
)


@router.post("/", response_model=FavoritoResposta)
def criar_favorito(dados: CriarFavorito):
    """
    Marca uma captura como favorita.

    TODO:
    - identificar treinador autenticado
    - verificar se a captura existe
    - verificar se pertence ao treinador
    - salvar favorito
    """

    raise NotImplementedError(
        "Aguardando integração com banco e autenticação."
    )


@router.get("/", response_model=list[FavoritoResposta])
def listar_favoritos():
    """
    Lista os favoritos do treinador autenticado.
    """

    raise NotImplementedError(
        "Aguardando integração com banco."
    )


@router.delete("/{favorito_id}")
def remover_favorito(favorito_id: int):
    """
    Remove uma captura dos favoritos.
    """

    raise NotImplementedError(
        "Aguardando integração com banco."
    )