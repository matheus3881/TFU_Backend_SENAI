from sqlalchemy.orm import Session
from models.administrador.log_auditoria import LogAuditoria
from datetime import datetime

# Registrar uma ação de auditoria
def registrar_acao(db: Session, acao: str, usuario: str):
    log = LogAuditoria(
        acao=acao,
        usuario=usuario,
        data=datetime.utcnow()
    )
    db.add(log)
    db.commit()
    db.refresh(log)
    return log

# Consultar histórico de auditoria
def listar_auditoria(db: Session):
    return db.query(LogAuditoria).all()

