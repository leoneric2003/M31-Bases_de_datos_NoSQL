import requests
import json

# URL de la API de MockAPI
url = "https://66b4e4d59f9169621ea4c11a.mockapi.io/api/v1/contactos"  # Reemplaza <tu-ID> con el ID correcto de tu proyecto

def obtener_registros():
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error al realizar la solicitud: {response.status_code}")
        return []

def agregar_registro(nuevo_registro):
    response = requests.post(url, json=nuevo_registro)
    if response.status_code == 201:
        return response.json()
    else:
        print(f"Error al agregar el registro: {response.status_code}")
        return None

def mostrar_registro(data):
    if data:
        print("Registro en formato plano:")
        for key, value in data.items():
            print(f"{key}: {value}")

def main():
    # Obtener todos los registros para encontrar el ID máximo actual
    registros = obtener_registros()
    if not registros:
        max_id = 0
    else:
        ids = [int(registro['id']) for registro in registros if 'id' in registro]
        max_id = max(ids)

    # Crear un nuevo ID para el registro
    nuevo_id = max_id + 1

    # Mostrar el ID del nuevo registro
    print(f"El ID del nuevo registro será: {nuevo_id}")

    # Solicitar al usuario que ingrese los detalles del nuevo registro
    nuevo_registro = {
        "id": nuevo_id,
        "nombre": input("Ingrese el nombre: "),
        "email": input("Ingrese el email: "),
        # Agrega aquí los campos adicionales que esperas en el registro
    }

    # Mostrar los detalles del nuevo registro antes de agregarlo
    print("\nDetalles del nuevo registro:")
    mostrar_registro(nuevo_registro)

    # Confirmar antes de agregar el registro
    confirmar = input("\n¿Desea agregar este registro? (sí/no): ").strip().lower()
    if confirmar in ['sí', 'si', 'yes', 'y']:
        # Agregar el nuevo registro
        registro_agregado = agregar_registro(nuevo_registro)
        if registro_agregado:
            # Mostrar el registro agregado
            mostrar_registro(registro_agregado)
    else:
        print("Registro no agregado.")

if __name__ == "__main__":
    main()
