import cv2

camera = cv2.VideoCapture(0, cv2.CAP_MSMF)

camera.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
camera.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)


def gerar_frames():
    while True:
        sucesso, frame = camera.read()

        if not sucesso:
            continue

        ret, buffer = cv2.imencode(".jpg", frame)

        if not ret:
            continue

        frame_bytes = buffer.tobytes()

        yield (
            b"--frame\r\n"
            b"Content-Type: image/jpeg\r\n\r\n" + frame_bytes + b"\r\n"
        )


def capturar_imagem(caminho="static/imagem.jpg"):
    sucesso, frame = camera.read()

    if not sucesso:
        return False

    cv2.imwrite(caminho, frame)
    return True