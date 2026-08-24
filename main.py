# Arquivo principal da API.
#
# Exemplo de integracao dos routers:
#
# from fastapi import FastAPI
# from routers.treinador.captura import router as captura_router
# from routers.treinador.favorito import router as favorito_router
# from routers.treinador.treinador import router as treinador_router
#
# app = FastAPI(title="Pokedex Digital")
#
# app.include_router(captura_router)
# app.include_router(favorito_router)
# app.include_router(treinador_router)
#
# O include_router faz as rotas de cada arquivo ficarem disponiveis
# na mesma aplicacao FastAPI.

from fastapi import FastAPI, status
from fastapi.responses import JSONResponse

from routers.auth import auth
from routers.pesquisador import pesquisador
# from routers.administrador import administrador
from routers.treinador import captura, favorito, treinador
from excecoes import RecursoNaoEncontrado



app = FastAPI(title="API Pokedéx", version="1.0.0")

# app.include_router(administrador.router)
app.include_router(pesquisador.router)
app.include_router(auth.router)
app.include_router(treinador.router)
app.include_router(favorito.router)
app.include_router(captura.router)

@app.get("/")
def inicio():
    return {"mensagem": "API NO AR"}

@app.get("/status")
def status():
    return {"status": "OK"}

@app.exception_handler(RecursoNaoEncontrado)
def tratar_nao_encontradao(request, exc):
    return JSONResponse(status_code=404, content={"detail":f"{exc.recurso} nao econtrado!"})
