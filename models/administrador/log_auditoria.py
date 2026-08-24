from sqlalchemy import ForeignKey, DateTime
from datetime import datetime
from database import Base


from sqlalchemy.orm import Mapped, mapped_column, relationship


class LogAuditoria(Base):
    __tablename__ = "log_auditoria"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    acao: Mapped[str] = mapped_column(nullable=False)          # Ex: "Remover Registro"
    usuario_id: Mapped[int] = mapped_column(ForeignKey("usuario.id"))  # Ex: "admin"
    data: Mapped[datetime] = mapped_column(DateTime, default=lambda: datetime.now())

    usuario: Mapped["Usuario"] = relationship(back_populates="logs_auditoria")


class Proposta(Base):
    __tablename__ = "propostas"

    id: Mapped[int] = mapped_column(primary_key=True)
    status: Mapped[str] = mapped_column(default="pendente")
    dadosAntes: Mapped[str] 
    dadosDepois: Mapped[str]