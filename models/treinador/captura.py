# app/models/captura.py

from sqlalchemy import Column, Integer, String, Date, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

# Modelo SQLAlchemy das capturas. Base sera configurada em database.py.

class Captura(Base):
    # TODO (integracao): ligar os relacionamentos a Usuario e Pokemon quando
    # esses modelos estiverem prontos no projeto.
    __tablename__ = "capturas"

    # Campos obrigatórios
    # Cada atributo abaixo representa uma coluna da tabela capturas.
    id = Column(Integer, primary_key=True, index=True)
    data_captura = Column(Date, nullable=False)
    local = Column(String(100), nullable=True)  # opcional
    nivel = Column(Integer, nullable=False)

    # Chaves estrangeiras (como strings - sem importar os models dos colegas)
    # ForeignKey liga uma captura ao treinador e ao Pokemon.
    treinador_id = Column(Integer, ForeignKey("usuarios.id"), nullable=False)
    pokemon_id = Column(Integer, ForeignKey("pokemon.id"), nullable=False)

    # Relacionamentos (quando os models dos colegas existirem)
    # treinador = relationship("Usuario", back_populates="capturas")
    # pokemon = relationship("Pokemon", back_populates="capturas")
