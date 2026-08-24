from fastapi import APIRouter

from schemas.treinador.captura import (
    CriarCaptura,
    CapturaResposta
)

# O schema CriarCaptura valida o corpo da requisicao antes de a funcao
# ser executada. O retorno precisa seguir o formato CapturaResposta.
# Quando a integracao estiver pronta, importe o CapturaService aqui e
# envie para ele o id do treinador e os dados validados.

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

# Exemplo de chamada pelo cliente:
# GET /treinador/capturas/
#
# O router nao deve montar consultas SQL diretamente. Ele deve receber
# a requisicao, identificar o usuario e chamar o service.