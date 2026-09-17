from sqlalchemy import ForeignKey, DateTime, func
from datetime import datetime
from database import Base


from sqlalchemy.orm import Mapped, mapped_column, relationship


class LogAuditoria(Base):
    __tablename__ = "logs_auditoria"

    id: Mapped[int] = mapped_column(primary_key=True)
    acao: Mapped[str] = mapped_column(nullable=False)          # Ex: "Remover Registro"
    usuario_id: Mapped[int] = mapped_column(ForeignKey("usuario.id"))  # Ex: "admin"
    data: Mapped[datetime] = mapped_column(DateTime, server_default=func.now(), nullable=False)

    usuario_id: Mapped["Usuario"] = relationship(back_populates="logs_auditoria") # type: ignore


class Proposta(Base):
    __tablename__ = "propostas"

    id: Mapped[int] = mapped_column(primary_key=True)
    status: Mapped[str] = mapped_column(default="pendente")
    dados_antes: Mapped[str] 
    dados_depois: Mapped[str]