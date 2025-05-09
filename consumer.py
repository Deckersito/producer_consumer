import socket
import json

SERVER_HOST = 'localhost'
SERVER_PORT = 5000

def sumar(a, b):
    return a + b

def a_mayusculas(texto):
    return texto.upper()

def invertir_cadena(texto):
    return texto[::-1]

tareas = {
    "sumar": sumar,
    "a_mayusculas": a_mayusculas,
    "invertir_cadena": invertir_cadena
}

def main():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((SERVER_HOST, SERVER_PORT))

    print("esperando que envies la tarea papa bello...")

    while True:
        mensaje = client_socket.recv(1024)
        if not mensaje:
            break

        try:
            data = json.loads(mensaje.decode())
            tarea = data["tarea"]
            parametros = data["parametros"]

            if tarea in tareas:
                resultado = tareas[tarea](*parametros)
                print(f"pollo, este es el resultado de'{tarea}': {resultado}")
            else:
                print("Tarea no válida.")
        except Exception as e:
            print("Error al procesar la tarea:", e)

    client_socket.close()

if __name__ == "__main__":
    main()
