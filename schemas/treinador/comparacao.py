from pydantic import BaseModel, Field, field_validator


class CompararPokemon(BaseModel):
    """
    Recebe os IDs dos Pokémon que serão comparados.

    Regra:
    A comparação precisa ter entre 2 e 4 Pokémon.
    """

    pokemon_ids: list[int] = Field(
        min_length=2,
        max_length=4
    )

    @field_validator("pokemon_ids")
    @classmethod
    def validar_ids(cls, ids):
        """
        Garante que todos os IDs sejam positivos.
        """

        if any(pokemon_id <= 0 for pokemon_id in ids):
            raise ValueError(
                "Todos os IDs dos Pokémon devem ser maiores que zero."
            )

        return ids