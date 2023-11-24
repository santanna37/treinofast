# Bibliotecas locais 
from src.bloguinho.config import Base


# Bibliotecas do sistema 
from pydantic import BaseModel
from typing import Optional

# Bibiotecas externas



#  Criando schemas 

class User(BaseModel):
    id: str
    nome: str
    email:str

    class Config:
        orm_mode= True 