from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from models.Pesquisador.proposta_alteracao import PropostaAlteracao
from schemas.Pesquisador.proposta import PropostaCriacao

def criar_proposta_alteracao(db: Session, dados: PropostaCriacao, pesquisador_id: int):
    nova_proposta = PropostaAlteracao(
        pesquisador_id=pesquisador_id,
        pokemon_id=dados.pokemon_id,
        campo_alterado=dados.campo_alterado,
        valor_proposto=dados.valor_proposto,
        justificativa=dados.justificativa,
        status="Pendente"
    )
    db.add(nova_proposta)
    db.commit()
    db.refresh(nova_proposta)
    return nova_proposta

def listar_propostas_pesquisador(db: Session, pesquisador_id: int):
    return db.query(PropostaAlteracao).filter(PropostaAlteracao.pesquisador_id == pesquisador_id).all()

def buscar_proposta_por_id(db: Session, proposta_id: int, pesquisador_id: int):
    proposta = db.query(PropostaAlteracao).filter(
        PropostaAlteracao.id == proposta_id,
        PropostaAlteracao.pesquisador_id == pesquisador_id
    ).first()
    
    if not proposta:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Proposta não encontrada."
        )
    return proposta