from fastapi import FastAPI, File, UploadFile
from processador import processar_gabarito
import shutil

app = FastAPI()

@app.post("/corrigir/")
async def corrigir_prova(file: UploadFile = File(...)):
    file_location = f"temp/{file.filename}"
    with open(file_location, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    resultado = processar_gabarito(file_location)
    return {"respostas": resultado}
