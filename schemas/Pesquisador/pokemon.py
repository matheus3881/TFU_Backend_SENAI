from pydantic import BaseModel
from typing import List, Optional

class PokemonBase(BaseModel):
    numero_pokedex: int
    nome: str
    descricao: str
    altura: float
    peso: float
    categoria: str
    geracao: int
    regiao: str

class PokemonCriacao(PokemonBase):
    tipos_ids: Optional[List[int]] = []

class PokemonResposta(PokemonBase):
    id: int

    class Config:
        orm_mode = True