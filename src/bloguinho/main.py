# Bibliotecas locais 


# Bibliotecas do sistema 
from fastapi import FastAPI

# Bibiotecas externas



# Start da aplicação
app=FastAPI()

#teste 1 
@app.get('/')
def home():
    return {'bom dia'}