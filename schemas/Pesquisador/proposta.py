from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class PropostaBase(BaseModel):
    campo_alterado: str
    valor_proposto: str
    justificativa: str

class PropostaCriacao(PropostaBase):
    pokemon_id: Optional[int] = None

class PropostaResposta(PropostaBase):
    id: int
    pesquisador_id: int
    pokemon_id: Optional[int] = None
    status: str
    data_criacao: datetime

    class Config:
        orm_mode = True