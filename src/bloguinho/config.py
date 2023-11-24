# Bibliotecas locais 


# Bibliotecas do sistema 
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from dotenv import Load_dotenv
import os 

# Bibiotecas externas



# Carregar o arquivo .env
Load_dotenv()

#conexão com o banco 
#SQLALCHEMY_DATABASE_URL= "postgres://postgres:password@localhost/cadastro_cpf"
SQLALCHEMY_DATABASE_URL=os.getenv('URL')


#
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread":False}
)

# Sessão local
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

#
Base = declarative_base()


# Criar e ativar banco de dados
def criar_db():
    Base.metadata.create_all(bind=engine)



def get_db():
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()
