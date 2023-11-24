# Bibliotecas locais 
from src.bloguinho.config import Base


# Bibliotecas do sistema 
from sqlalchemy import (
    Column,
    String,
    Integer
)

# Bibiotecas externas



# Criando modelos 

class User(Base):
    __tablename__ = 'usuarios'
    id = Column(String, primary_key=True, index=True)
    nome = Column(String)
    email = Column(String)