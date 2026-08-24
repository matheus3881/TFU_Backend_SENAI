# app/routers/treinador.py

from fastapi import APIRouter, Depends, HTTPException
from schemas.treinador.captura import CriarCaptura, CapturaResposta
from schemas.usuario.autenticacao import UsuarioAtual
from services.treinador import captura_service

# Rotas HTTP para operacoes feitas pelo treinador.
# Este router usa Depends para obter o usuario atual. No projeto real,
# get_current_user_mock sera trocado pela dependencia de autenticacao.

router = APIRouter(prefix="/treinador", tags=["Treinador"])

# 🔥 MOCK - Depois substituir pela dependência real da Pessoa 4
async def get_current_user_mock():
    # TODO (integracao): trocar este usuario fixo pela autenticacao real.
    # Enquanto isso, todas as operacoes sao associadas ao treinador de id 1.
    class UsuarioMock:
        id = 1
        nome = "Treinador Teste"
        role = "TREINADOR"
    return UsuarioMock()

@router.post("/capturas", response_model=CapturaResposta)
def registrar_captura(
    dados: CriarCaptura,
    usuario=UsuarioAtual  # ← MOCK
):
    try:
        # O router encaminha os dados para o service.
        # A regra de negocio e a gravacao ficam fora desta camada.
        return captura_service.registrar_captura(usuario.id, dados)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/capturas", response_model=list[CapturaResposta])
def listar_minhas_capturas(
    usuario=UsuarioAtual  # ← MOCK
):
    # O id do usuario evita que um treinador veja capturas de outro.
    return captura_service.listar_capturas_do_treinador(usuario.id)

@router.get("/")
def obter_treinador():
    """
    Retorna os dados do treinador autenticado.

    TODO:
    Substituir o usuário mock pela dependência
    usuario_logado fornecida pelo módulo de autenticação.
    """

    return {
        "mensagem": "Endpoint preparado para integração.",
        "observacao": (
            "O treinador será identificado pelo usuario_logado."
        )
    }