from fastapi import APIRouter

from schemas.treinador.captura import (
    CriarCaptura,
    CapturaResposta
)

router = APIRouter(
    prefix="/treinador/capturas",
    tags=["Treinador - Capturas"]
)


@router.post("/", response_model=CapturaResposta)
def criar_captura(dados: CriarCaptura):
    """
    Registra uma nova captura.

    TODO:
    - receber usuario_logado
    - verificar se o Pokemon existe
    - chamar CapturaService
    - salvar através do SQLAlchemy
    """

    raise NotImplementedError(
        "Aguardando integração com Usuario, Pokemon e banco."
    )


@router.get("/")
def listar_capturas():
    """
    Lista as capturas do treinador autenticado.

    TODO:
    Utilizar usuario_logado para descobrir o treinador.
    """

    raise NotImplementedError(
        "Aguardando integração com banco e autenticação."
    )