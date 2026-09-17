from sqlalchemy import Column, Integer, String, Text, ForeignKey, DateTime, func
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import datetime
from database import Base


class PropostaAlteracao(Base):
    __tablename__ = "propostas_alteracao"

    id: Mapped[int] = mapped_column(primary_key=True)
    usuario_id: Mapped[int] = mapped_column(ForeignKey("usuarios.id"))
    pokemon_id: Mapped[int] = mapped_column(ForeignKey("pokemons.id"))

    campo_alterado: Mapped[str] = mapped_column(String(50), nullable=False)
    valor_proposto: Mapped[str]
    justificativa: Mapped[str]
    status: Mapped[str] = mapped_column(String(20), default="pendente")
    data_criacao: Mapped[datetime] = mapped_column(DateTime, server_default=func.now(), nullable=False)

    usuario: Mapped["Usuario"] =  relationship(back_populates="propostas_alteracao") # type: ignore
    pokemon: Mapped["Pokemon"] = relationship(back_populates="propostas_alteracao") # type: ignore
