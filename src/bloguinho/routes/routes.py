# Bibliotecas locais 
from src.bloguinho.adapters.repositorio import RepositorioUser
from src.domain.schemas.schemas_user import User as UserSchemas
from src.bloguinho.config import get_db

# Bibliotecas do sistema 
from sqlalchemy.orm import Session
from fastapi import APIRouter

# Bibiotecas externas



# CRIANDO ROTAS 

router = APIRouter()

@router.post('/user')
def criar_user_rotas(user:UserSchemas, session:Session, Depends(get_db)):
    user_criado = RepositorioUser(session).criar_user_repositorio(user)
    return user_criado