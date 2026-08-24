
from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm

from database import SessionDep
from models.usuario.usuario import Usuario
from schemas.usuario.autenticacao import UsuarioAtual, criar_token, gerar_hash, verificar_senha
from schemas.usuario.usuario import UsuarioEntrada, UsuarioResposta, Token


router = APIRouter(tags=["Autenticacao"], prefix="/auth")

@router.post("/register", response_model=UsuarioResposta, status_code=status.HTTP_201_CREATED)
def registrar(dados: UsuarioEntrada, session: SessionDep):
    usuario = Usuario(username=dados.usuario, hashed_senha=gerar_hash(dados.senha))
    session.add(usuario)
    session.commit()
    return usuario


@router.post("/token", response_model=Token)
def login(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
    session: SessionDep):

    usuario = session.query(Usuario).filter(
        Usuario.username == form_data.username).first()
    if usuario is None or not verificar_senha(form_data.password, usuario.hashed_senha):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Usuario ou senha inválidos",
            headers={"WWW-Authenticate": "Bearer"})
    token = criar_token({"sub": usuario.username})
    return Token(access_token=token, token_type="bearer")

@router.get("/eu", response_model=UsuarioResposta)
def eu(usuario: UsuarioAtual):
    return usuario