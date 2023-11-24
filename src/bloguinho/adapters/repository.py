# Bibliotecas locais 
from src.domain.schemas.schemas_user import User as UserSchema
from src.domain.models.models_user import User as UserModel

# Bibliotecas do sistema 
from sqlalchemy.orm import Session


# Bibiotecas externas



# Repositorio de usuarios 

class RepositorioUser():
    def __init__(self, session:Session):
        self.session = session

    def criar_user_repositorio(self, user:UserSchema.User):
        db_user = UserModel(
            id = user.id,
            nome = user.nome,
            email = user.email
        )

        self.session.add(db_user)
        self.session.commit()
        self.session.refresh(db_user)
        return db_user