# Bibliotecas locais 


# Bibliotecas do sistema 
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI

# Bibiotecas externas



# Start da aplicação
app=FastAPI()

#teste 1 
@app.get('/')
def home():
    return {'bom dia'}



# Middlewares -  configurado para banco em docker e app em terminal
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5432"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)
