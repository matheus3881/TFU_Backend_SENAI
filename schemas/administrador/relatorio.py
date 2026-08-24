from pydantic import BaseModel
from typing import List

class RelatorioEstatistico(BaseModel):
    total_registros: int 
    registros_removidos: int
    propostas_aprovadas: int
    propostas_rejeitadas: int

