from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

class LogAuditoria(Base):
    _tablename_ = "log_auditoria"

    id = Column(Integer, primary_key=True, index=True)
    acao = Column(String, nullable=False)          # Ex: "Remover Registro"
    usuario = Column(String, nullable=False)       # Ex: "admin"
    data = Column(DateTime, default=lambda: datetime.now())