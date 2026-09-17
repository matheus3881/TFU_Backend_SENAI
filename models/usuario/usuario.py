from database import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship


class Usuario(Base):
    __tablename__ = "usuarios"

    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(unique=True)
    hashed_senha: Mapped[str]
    papel: Mapped[str] = mapped_column(default="Comum")

    logs_auditoria: Mapped[list["LogAuditoria"]] = relationship(back_populates="usuario_id") # type: ignore
    propostas_alteracao: Mapped[list["PropostaAlteracao"]] = relationship(back_populates="usuario") # type: ignore
    
