from sqlalchemy import Column, Integer, String, Text, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from database import Base

from models.treinador.pokemon import Pokemon

class PropostaAlteracao(Base):
    __tablename__ = "propostas_alteracao"

    id = Column(Integer, primary_key=True, index=True)
    pesquisador_id = Column(Integer, ForeignKey("usuarios.id"), nullable=False)
    pokemon_id = Column(Integer, ForeignKey("pokemons.id"), nullable=True)
    
    campo_alterado = Column(String(50), nullable=False)
    valor_proposto = Column(Text, nullable=False)
    justificativa = Column(Text, nullable=False)
    status = Column(String(20), default="Pendente")
    data_criacao = Column(DateTime, default=datetime.utcnow)

    pesquisador = relationship("Usuario")
    pokemon = relationship(Pokemon)