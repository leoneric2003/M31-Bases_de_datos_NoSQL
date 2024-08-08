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

def mostrar_registro(data):
    if data:
        print("Registro en formato plano:")
        for key, value in data.items():
            print(f"{key}: {value}")

def main():
    # Obtener todos los registros para contar y mostrar el rango de IDs
    registros = obtener_registros()
    if not registros:
        return

    # Extraer y mostrar el rango de IDs
    ids = [int(registro['id']) for registro in registros if 'id' in registro]
    if ids:
        print(f"Rango de IDs disponibles: {min(ids)} a {max(ids)}")
    else:
        print("No se encontraron IDs en los registros.")
        return

    # Solicitar al usuario que ingrese el ID del registro que desea mostrar
    try:
        registro_id = int(input("Ingrese el ID del registro que desea mostrar: "))
    except ValueError:
        print("ID no válido. Debe ser un número entero.")
        return

    # Validar que el ID ingresado esté dentro del rango
    if registro_id not in ids:
        print("ID no válido. Por favor, ingrese un ID dentro del rango mostrado.")
        return

    # Obtener y mostrar el registro específico
    response = requests.get(f"{url}/{registro_id}")
    if response.status_code == 200:
        try:
            data = response.json()
            mostrar_registro(data)
        except json.JSONDecodeError as e:
            print(f"Error al decodificar el JSON: {e}")
    else:
        print(f"Error al realizar la solicitud: {response.status_code}")

if __name__ == "__main__":
    main()
