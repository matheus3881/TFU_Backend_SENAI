from pydantic import BaseModel, ConfigDict


class TreinadorResposta(BaseModel):
    """
    Representa os dados básicos de um treinador.

    IMPORTANTE:
    O Treinador será obtido a partir do Usuario autenticado.
    Este schema NÃO cria um novo usuário.
    """

    model_config = ConfigDict(from_attributes=True)

    id: int
    nome: str
    email: str
    role: str


class TreinadorResumo(BaseModel):
    """
    Resumo das informações do treinador.

    Pode ser utilizado futuramente na tela
    da Pokédex pessoal.
    """

    id: int
    nome: str
    total_capturas: int
    total_shiny: int