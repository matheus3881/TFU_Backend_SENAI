class ComparacaoService:
    """
    Contém as regras relacionadas à comparação de Pokémon.

    Neste momento o Service não consulta o banco.
    Ele apenas valida as regras que não dependem do ORM.

    A consulta dos Pokémon será integrada posteriormente
    com o Model Pokemon do colega responsável.

    Exemplo de uso em um router:
    1. O router recebe CompararPokemon.
    2. Chama validar_quantidade(dados.pokemon_ids).
    3. Busca os Pokémon no banco ou em um servico externo.
    4. Compara os dados e devolve um schema de resposta.
    """

    @staticmethod
    def validar_quantidade(pokemon_ids: list[int]) -> None:
        """
        Verifica se existem entre 2 e 4 Pokémon.

        RN06:
        A comparação exige entre 2 e 4 Pokémon.
        """

        quantidade = len(pokemon_ids)

        if quantidade < 2:
            raise ValueError(
                "É necessário informar pelo menos 2 Pokémon."
            )

        if quantidade > 4:
            raise ValueError(
                "É permitido comparar no máximo 4 Pokémon."
            )