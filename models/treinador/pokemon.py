from database import Base

from sqlalchemy.orm import Mapped, mapped_column, relationship



class Pokemon(Base):
    __tablename__ = "pokemons"

    id: Mapped[int] = mapped_column(primary_key=True)
    numeroPokedex: Mapped[int] = mapped_column(unique=True)
    descricao: Mapped[str]
    ataque: Mapped[int]
    defesa: Mapped[int]
    velocidade: Mapped[int]
    imagem: Mapped[str]

    propostas_alteracao: Mapped[list["PropostaAlteracao"]] = relationship(back_populates="pokemon") # type: ignore


    def getAtributosCombate(self):
        pass


