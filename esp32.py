import serial

porta_serial = None

def conectar_esp32(porta="COM3", baudrate=9600):
    global porta_serial

    try:
        porta_serial = serial.Serial(porta, baudrate, timeout=1)
        print("ESP32 conectado com sucesso!")
    except Exception as erro:
        porta_serial = None
        print(f"ESP32 não conectado: {erro}")


def enviar_comando(comando):
    global porta_serial

    print(f"Comando recebido: {comando}")

    if porta_serial is not None:
        porta_serial.write(comando.encode())
        print(f"Comando enviado ao ESP32: {comando}")
    else:
        print("Modo teste: ESP32 não conectado.")