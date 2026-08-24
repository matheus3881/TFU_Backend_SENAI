from database import Base, engine
import models.usuario.usuario
# import models.administrador.log_auditoria
import models.treinador.pokemon
import models.Pesquisador.proposta_alteracao
import models.treinador.captura
import models.treinador.favoritos


Base.metadata.create_all(bind=engine)
