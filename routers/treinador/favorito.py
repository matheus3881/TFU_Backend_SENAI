from fastapi import APIRouter

from schemas.treinador.favorito import (
    CriarFavorito,
    FavoritoResposta
)

# ============================================================
# EXEMPLO DE INTEGRACAO COM OS OUTROS ARQUIVOS
# ============================================================
# Este arquivo e o router. Ele recebe a requisicao da API e chama
# o service para executar as regras do sistema.
#
# 1. No main.py, o router precisa ser importado e registrado:
#
# from fastapi import FastAPI
# from routers.treinador.favorito import router as favorito_router
#
# app = FastAPI()
# app.include_router(favorito_router)
#
# Depois disso, este endpoint ficara disponivel em:
# POST /treinador/favoritos/
#
# 2. O schema CriarFavorito, em schemas/treinador/favorito.py,
#    recebe e valida os dados enviados pelo usuario:
#
# {
#     "captura_id": 1
# }
#
# 3. Quando o service estiver pronto, o router pode chama-lo assim:
#
# from services.treinador.favorito_service import FavoritoService
#
# @router.post("/", response_model=FavoritoResposta)
# def criar_favorito(dados: CriarFavorito):
#     # O service concentra as regras de negocio.
#     FavoritoService.validar_captura_id(dados.captura_id)
#
#     # Aqui tambem seria feita a busca da captura e do treinador.
#     # Depois, o favorito seria salvo usando o model do banco:
#     # novo_favorito = Favorito(
#     #     treinador_id=treinador_logado.id,
#     #     captura_id=dados.captura_id
#     # )
#     # db.add(novo_favorito)
#     # db.commit()
#     # db.refresh(novo_favorito)
#
#     # Por fim, retornamos o objeto salvo para a API.
#     # return novo_favorito
#
# A ideia e: router recebe, schema valida, service aplica as regras,
# model representa a tabela e database faz a conexao com o banco.

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