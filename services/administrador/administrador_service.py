from sqlalchemy.orm import Session
from services import auditoria_service

def remover_pokemon(db: Session, id: int):
    # lógica de remoção...
    auditoria_service.registrar_acao(db, "Remover Registro", "admin")
    return {"msg": f"Pokemon {id} removido com sucesso"}


