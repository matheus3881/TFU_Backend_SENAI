# Este arquivo concentra a configuracao da conexao com o banco.
#
# Exemplo usando SQLite com SQLAlchemy:
#
# from sqlalchemy import create_engine
# from sqlalchemy.orm import declarative_base, sessionmaker
#
# DATABASE_URL = "sqlite:///./pokedex.db"
# engine = create_engine(
#     DATABASE_URL,
#     connect_args={"check_same_thread": False}
# )
# SessionLocal = sessionmaker(
#     autocommit=False,
#     autoflush=False,
#     bind=engine
# )
# Base = declarative_base()
#
# Depois de importar os models, as tabelas podem ser criadas assim:
# Base.metadata.create_all(bind=engine)
#
# O service usa SessionLocal para abrir uma sessao, salvar ou consultar
# dados e fechar a sessao no final da operacao.
