from flask import Flask, render_template, Response, redirect, url_for
from camera import gerar_frames, capturar_imagem
from modelo import classificar_imagem
from esp32 import enviar_comando

app = Flask(__name__)

resultado_atual = "Nenhuma classificação realizada."


@app.route("/")
def index():
    return render_template("index.html", resultado=resultado_atual)


@app.route("/video")
def video():
    return Response(
        gerar_frames(),
        mimetype="multipart/x-mixed-replace; boundary=frame"
    )


@app.route("/capturar", methods=["POST"])
def capturar():
    sucesso = capturar_imagem("static/imagem.jpg")

    if sucesso:
        print("Imagem capturada com sucesso!")
    else:
        print("Erro ao capturar imagem.")

    return redirect(url_for("index"))


@app.route("/classificar", methods=["POST"])
def classificar():
    global resultado_atual

    caminho_imagem = "static/imagem.jpg"
    resultado_atual = classificar_imagem(caminho_imagem)

    return redirect(url_for("index"))


@app.route("/controle/<comando>", methods=["POST"])
def controle(comando):
    enviar_comando(comando)
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True)