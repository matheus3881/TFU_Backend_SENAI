# app/services/captura_service.py

from datetime import date
from database import SessionLocal
from models.treinador.captura import Captura
from schemas.treinador.captura import CriarCaptura, CapturaResposta

# Regras de negocio para registrar e consultar capturas.

class CapturaService:
    """
    Regras de negócio relacionadas às capturas.

    Acesso ao banco será integrado posteriormente.
    """

    @staticmethod
    def validar_captura(
        pokemon_id: int,
        nivel: int,
        local: str
    ) -> None:

        if pokemon_id <= 0:
            raise ValueError(
                "O ID do Pokémon deve ser maior que zero."
            )

        if nivel <= 0:
            raise ValueError(
                "O nível deve ser maior que zero."
            )

        if not local.strip():
            raise ValueError(
                "O local da captura não pode ser vazio."
            )

def registrar_captura(treinador_id: int, dados: CriarCaptura):
    """
    TODO: Quando o model Pokemon estiver pronto:
    - Verificar se o Pokemon existe (RN02)
    """

    # TODO (integracao): consultar o modulo Pokemon e confirmar que o
    # pokemon_id existe antes de persistir a captura.
    
    # Por enquanto, assume que o Pokemon existe
    # Depois você substitui pela verificação real
    
    captura = Captura(
        pokemon_id=dados.pokemon_id,
        local=dados.local,
        nivel=dados.nivel,
        treinador_id=treinador_id,
        data_captura=date.today()
    )
    
    db = SessionLocal()
    try:
        db.add(captura)
        db.commit()
        db.refresh(captura)
        return captura
    finally:
        db.close()

def listar_capturas_do_treinador(treinador_id: int):
    """Retorna somente as capturas pertencentes ao treinador informado."""
    db = SessionLocal()
    try:
        return db.query(Captura).filter(Captura.treinador_id == treinador_id).all()
    finally:
        db.close()
