class FavoritoService:
    """
    Regras de negócio relacionadas aos favoritos.

    Operações dependentes de banco e autenticação serão integradas
    posteriormente: criar, listar e remover favoritos, verificar a captura,
    verificar sua propriedade e evitar duplicidades.
    """

    @staticmethod
    def validar_captura_id(captura_id: int) -> None:
        """
        Validação básica do ID da captura.
        """

        if captura_id <= 0:
            raise ValueError(
                "O ID da captura deve ser maior que zero."
            )