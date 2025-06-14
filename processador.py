import cv2
import numpy as np

def processar_gabarito(imagem_path):
    # Lê a imagem
    imagem = cv2.imread(imagem_path, cv2.IMREAD_GRAYSCALE)

    # Simula a identificação – substitua por sua lógica com contornos
    # Aqui deve-se implementar a identificação de quadrados preenchidos

    respostas = {
        "01": "B",
        "02": "Sem marcação",
        "03": "Marcação incorreta"
    }

    return respostas
