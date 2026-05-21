import requests
import serial

IP_ESP32 = "192.168.0.103"

porta_serial = None

rotas = {
    "F": "/frente",
    "B": "/tras",
    "L": "/esquerda",
    "R": "/direita",
    "S": "/parar",

    "G": "/frente_direita",
    "H": "/frente_esquerda",
    "I": "/tras_direita",
    "J": "/tras_esquerda"
}

def conectar_esp32(porta="COM3", baudrate=115200):

    global porta_serial

    try:
        porta_serial = serial.Serial(porta, baudrate, timeout=1)

        print("ESP32 Serial conectado!")

    except Exception as erro:

        porta_serial = None

        print(f"Serial não conectou: {erro}")

def enviar_comando(comando):

    print(f"Comando recebido: {comando}")

    # ================= SERIAL =================

    if porta_serial is not None:

        try:

            porta_serial.write(comando.encode())

            print(f"Comando enviado via Serial: {comando}")

            return

        except Exception as erro:

            print(f"Erro Serial: {erro}")

    # ================= WIFI =================

    if comando.startswith("V"):

        valor = comando[1:]

        try:

            resposta = requests.get(
                f"http://{IP_ESP32}/vel?valor={valor}",
                timeout=1
            )

            print(f"Velocidade enviada: {valor}")

        except Exception as erro:

            print(f"Erro ao enviar velocidade: {erro}")

        return

    rota = rotas.get(comando)

    if rota is None:
        print("Comando inválido")
        return

    try:

        resposta = requests.get(
            f"http://{IP_ESP32}{rota}",
            timeout=1
        )

        print(f"Comando enviado via Wi-Fi: {comando}")

    except Exception as erro:

        print(f"Erro Wi-Fi: {erro}")