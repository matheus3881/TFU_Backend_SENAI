from datetime import date

from pydantic import BaseModel, Field


class EntradaPokedex(BaseModel):
    """
    Representa um Pokémon capturado dentro
    da Pokédex pessoal.
    """

    pokemon_id: int = Field(gt=0)
    pokemon_nome: str = Field(min_length=1)
    numero_pokedex: int = Field(gt=0)
    nivel: int = Field(ge=0)
    is_shiny: bool
    local: str | None = None
    data_captura: date


class PokedexResposta(BaseModel):
    """
    Representa a Pokédex pessoal completa.
    """

    treinador_id: int = Field(gt=0)
    treinador_nome: str = Field(min_length=1)

    total_capturado: int = Field(ge=0)
    total_shiny: int = Field(ge=0)

    pokemons: list[EntradaPokedex]

# O service monta este formato depois de buscar as capturas do treinador.