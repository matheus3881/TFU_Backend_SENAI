from pydantic import BaseModel
from datetime import datetime

class Auditoria(BaseModel):
    id: int
    acao: str
    usuario: str
    data: datetime
    