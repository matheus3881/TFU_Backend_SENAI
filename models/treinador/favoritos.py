# app/models/favorito.py
# Responsável por definir o modelo SQLAlchemy dos favoritos.

from sqlalchemy import Column, Integer, Date, ForeignKey
from database import Base

# Modelo SQLAlchemy de capturas favoritas. A tabela usuarios e externa a este modulo.

class FavoritoResposta(Base):
    # TODO (integracao): criar schema, service e rotas para favoritos.
    __tablename__ = "favoritos"

    # O model representa a tabela; o schema FavoritoResposta representa
    # o formato que a API devolve. Sao responsabilidades diferentes.
    id = Column(Integer, primary_key=True, index=True)
    treinador_id = Column(Integer, ForeignKey("usuarios.id"))
    captura_id = Column(Integer, ForeignKey("capturas.id"))
    criado_em = Column(Date)
