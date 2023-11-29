# Bibliotecas locais 
from src.bloguinho.routes import routes_user as userRoutes
from src.bloguinho.config import criar_db

# Bibliotecas do sistema 
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI

# Bibiotecas externas



# Start da aplicação
app=FastAPI()
criar_db()

# Ativando Banco de Dados 


# Ativando Rotas 
app.include_router(userRoutes.router)

#teste 1 
@app.get('/')
def home():
    return {'bom dia'}




# # Middlewares -  configurado para banco em docker e app em terminal
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["http://localhost:5432"],
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"]
# )
