import requests
import json

# URL de la API de MockAPI
url = "https://66b4e4d59f9169621ea4c11a.mockapi.io/api/v1/contactos"  # Reemplaza <tu-ID> con el ID correcto de tu proyecto


def obtener_registro(registro_id):
    response = requests.get(f"{url}/{registro_id}")
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error al realizar la solicitud: {response.status_code}")
        return None


def actualizar_registro(registro_id, datos_actualizados):
    response = requests.put(f"{url}/{registro_id}", json=datos_actualizados)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error al actualizar el registro: {response.status_code}")
        return None


def mostrar_registro(data):
    if data:
        print("Registro en formato plano:")
        for key, value in data.items():
            print(f"{key}: {value}")


def main():
    # Solicitar al usuario que ingrese el ID del registro que desea modificar
    registro_id = input("Ingrese el ID del registro que desea modificar: ")

    # Obtener el registro existente
    registro_existente = obtener_registro(registro_id)
    if not registro_existente:
        return

    # Mostrar los detalles del registro existente
    print("Detalles del registro existente:")
    mostrar_registro(registro_existente)

    # Solicitar al usuario que ingrese los nuevos valores
    datos_actualizados = {
        "nombre": input(f"Ingrese el nuevo nombre (actual: {registro_existente['nombre']}): ") or registro_existente[
            'nombre'],
        "email": input(f"Ingrese el nuevo email (actual: {registro_existente['email']}): ") or registro_existente[
            'email'],
        # Agrega aquí los campos adicionales que esperas en el registro
    }

    # Confirmar antes de actualizar el registro
    print("\nDetalles actualizados del registro:")
    mostrar_registro(datos_actualizados)

    confirmar = input("\n¿Desea actualizar este registro? (sí/no): ").strip().lower()
    if confirmar in ['sí', 'si', 'yes', 'y']:
        # Actualizar el registro
        registro_actualizado = actualizar_registro(registro_id, datos_actualizados)
        if registro_actualizado:
            # Mostrar el registro actualizado
            print("\nRegistro actualizado:")
            mostrar_registro(registro_actualizado)
    else:
        print("Actualización no realizada.")


if __name__ == "__main__":
    main()
