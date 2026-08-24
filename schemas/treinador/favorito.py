#esse arquivo é responsável por definir os schemas 
# relacionados aos pokemons favoritos do treinador.

from pydantic import BaseModel, ConfigDict, Field
from datetime import date

class CriarFavorito(BaseModel):
    captura_id: int = Field(gt=0)

class FavoritoResposta(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    
    id: int
    treinador_id: int
    captura_id: int
    criado_em: date

