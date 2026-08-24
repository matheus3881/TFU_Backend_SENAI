# app/schemas/captura.py

from pydantic import BaseModel, ConfigDict, Field
from datetime import date
from typing import Optional, List

# Schemas validam a entrada e definem a resposta das rotas de captura.

class CriarCaptura(BaseModel):
    # Dados exigidos no POST /treinador/capturas.
    pokemon_id: int = Field(gt=0)
    local: str = Field(min_length=2, max_length=100)
    nivel: int = Field(gt=0, le=100)

class CapturaResposta(BaseModel):
    # Formato devolvido ao criar ou listar capturas.
    model_config = ConfigDict(from_attributes=True)
    
    id: int
    pokemon_id: int
    local: str
    nivel: int
    data_captura: date

class EntradaPokedexExportada(BaseModel):
    """
    Representa uma captura dentro da Pokédex exportada.
    """

    pokemon_nome: str
    numero_pokedex: int
    is_shiny: bool
    nivel: int
    local: Optional[str] = None
    data_captura: date


class ExportarPokedex(BaseModel):
    """
    Representa a Pokédex completa de um treinador.
    """

    treinador_nome: str
    total_capturado: int
    total_shiny: int

    entradas: List[EntradaPokedexExportada]