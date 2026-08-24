from fastapi import APIRouter, HTTPException
from services import administrador_service

router = APIRouter(prefix="/adim", tags=["Adminstrador"])

# PATCH /admin/pakemon/{id}
@router.patch("/pokemon/{id}")
async def atualizar_pokemon(id: int, dados: dict):
    return administrador_service.atualizar_pokemon(id, dados)

# DELETE /admin/ pokemon/ {id}
@router.delete("/pokemon/{id}")
async def atualizar_pokemon(id: int, dados: dict):
    return administrador_service.remover_pokemon(id)

#GET /admin / relatorios 
@router.get("/relatorio")
async def gerar_relatorios():
    return administrador_service.gerar_relatorios()

#GET / admin/proposta
@router.get ("/proposta")
async def listar_propostas():
    return administrador_service.listar_propostas()

#PATCH / admin /propostas / {id}/aprovar
@router.patch("/propostas/{id}/aprovar")
async def aprovar_peoposta(id: int):
    return administrador_service.aprovar_proposta(id)

# PATCH / admin/ propostas/ {id} / rejeitar
@ router.patch("/propostas/{id}/rejeitar")
async def rejeitar_proposta( id: int):
    return administrador_service.service_rejeitar_proposta(id)

# PATCH / admin / auditoria 
@router.get("/auditoria")
async def visualizar_auditoria():
    return administrador_service.visualizar_auditoria()