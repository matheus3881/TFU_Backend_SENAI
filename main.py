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
