import socket
import json

SERVER_HOST = 'localhost'
SERVER_PORT = 5000

def mostrar_menu():
    print("pollo, selecciona que tarea quieres realizar:")
    print("1. Sumar dos números")
    print("2. Convertir a mayúsculas")
    print("3. Invertir cadena")

def obtener_tarea():
    mostrar_menu()
    opcion = input("valecita, ingresa el número de la tarea: ")

    if opcion == '1':
        a = int(input("Primer número: "))
        b = int(input("Segundo número: "))
        tarea = {
            "tarea": "sumar",
            "parametros": [a, b]
        }
    elif opcion == '2':
        texto = input("Texto a convertir: ")
        tarea = {
            "tarea": "a_mayusculas",
            "parametros": [texto]
        }
    elif opcion == '3':
        texto = input("Texto a invertir: ")
        tarea = {
            "tarea": "invertir_cadena",
            "parametros": [texto]
        }
    else:
        print("Opción inválida.")
        return None

    return tarea

def main():
    tarea = obtener_tarea()
    if not tarea:
        return

    try:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((SERVER_HOST, SERVER_PORT))
        client_socket.sendall(json.dumps(tarea).encode())
        client_socket.close()
        print("pollo, ya te mandé la tarea al servidor.")
    except Exception as e:
        print("Error al conectar o enviar:", e)

if __name__ == "__main__":
    main()
