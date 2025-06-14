from fastapi import FastAPI, UploadFile, File
from fastapi.responses import JSONResponse
import cv2
import numpy as np

app = FastAPI()

@app.post("/corrigir")
async def corrigir(imagem: UploadFile = File(...)):
    # Lê a imagem
    conteudo = await imagem.read()
    nparr = np.frombuffer(conteudo, np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

    # Aqui vai a lógica do OpenCV para detectar marcações

    resultado = {
        "01": "B",
        "02": "C",
        "03": "A"
    }

    return JSONResponse(content=resultado)
