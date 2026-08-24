from collections.abc import Collection, Iterable
from typing import Protocol


class _CapturaComShiny(Protocol):
    is_shiny: bool


class PokedexService:
    """
    Regras relacionadas à Pokédex pessoal.

    A busca das capturas será implementada quando
    o banco e os Models estiverem integrados.

    Exemplo de integracao:
    o router busca as capturas do treinador e envia a lista para
    calcular_total_capturado e calcular_total_shiny. Depois, monta
    o objeto PokedexResposta para devolver ao cliente.
    """

    @staticmethod
    def calcular_total_shiny(
        capturas: Iterable[_CapturaComShiny],
    ) -> int:
        """
        Conta quantas capturas são Shiny.

        A função recebe uma lista de objetos que possuam
        o atributo 'is_shiny'.
        """

        return sum(
            1
            for captura in capturas
            if captura.is_shiny
        )

    @staticmethod
    def calcular_total_capturado(capturas: Collection[object]) -> int:
        """
        Retorna a quantidade total de capturas.
        """

        return len(capturas)