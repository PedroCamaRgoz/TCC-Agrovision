import tensorflow as tf
import numpy as np
import cv2

# CARREGAR MODELO TFLITE

interpreter = tf.lite.Interpreter(
    model_path="model/modelo.tflite"
)

interpreter.allocate_tensors()

# ENTRADAS E SAÍDAS

input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()


def classificar_imagem(caminho_imagem):

    # LER IMAGEM

    imagem = cv2.imread(caminho_imagem)

    if imagem is None:
        return "Erro ao carregar imagem."

    # REDIMENSIONAR

    imagem = cv2.resize(imagem, (224, 224))

    # NORMALIZAR

    imagem = imagem.astype(np.float32) / 255.0

    # ADICIONAR DIMENSÃO

    imagem = np.expand_dims(imagem, axis=0)

    # ENVIAR PARA O MODELO

    interpreter.set_tensor(
        input_details[0]['index'],
        imagem
    )

    interpreter.invoke()

    # RESULTADO

    resultado = interpreter.get_tensor(
        output_details[0]['index']
    )

    probabilidade = resultado[0][0]

    print(f"Probabilidade: {probabilidade}")

    # CLASSIFICAÇÃO

    if probabilidade >= 0.5:
        return f"Folha COM sinais de pragas ({probabilidade:.2f})"

    else:
        return f"Folha SAUDÁVEL ({1 - probabilidade:.2f})"