# syntax=docker/dockerfile:1

# imagem do python 
FROM python:3.8-slim-buster

# Definir o diretório do app 
WORKDIR /src

# Copiar a requirement
COPY requirements.txt .

# Copiar o Diretório 
COPY . .

# Instala as dependencias do requirements.txt
RUN pip install -r requirements.txt 

# Porta disponivel 
EXPOSE 80 

# Executa o main
CMD ["uvicorn", "main.py", "--host", "0.0.0.0", "--port", "80", "--reload"]