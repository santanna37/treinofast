# Bibliotecas locais 


# Bibliotecas do sistema 
from sqlalchemy.dialects.postgresql import psycopg2
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine


# Bibiotecas externas



#conexão com o banco 
#SQLALCHEMY_DATABASE_URL=postgresql://postgres:password@localhost/db_docker
# explicação ---------------------://<usuario>:senha@localhost/<database>
SQLALCHEMY_DATABASE_URL="postgresql://postgres:password@localhost:5432/bloguinho"


#
engine = create_engine(
    SQLALCHEMY_DATABASE_URL
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
