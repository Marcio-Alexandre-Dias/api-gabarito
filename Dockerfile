FROM python:3.12-slim

# Instala dependências do sistema necessárias pro OpenCV
RUN apt-get update && apt-get install -y \
    libgl1-mesa-glx \
    libglib2.0-0 \
    && rm -rf /var/lib/apt/lists/*

# Cria diretório da aplicação
WORKDIR /app


# Copia os arquivos da aplicação
COPY . .

# Instala as dependências do projeto
RUN pip install --no-cache-dir -r requirements.txt

# Expõe a porta usada pelo Railway
EXPOSE 8080

# Comando para iniciar a aplicação
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]
