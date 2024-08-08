import requests

# URL de la API de MockAPI
url = "https://66b4e4d59f9169621ea4c11a.mockapi.io/api/v1/contactos"  # Reemplaza <tu-ID> con el ID correcto de tu proyecto


def obtener_registro(registro_id):
    response = requests.get(f"{url}/{registro_id}")
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error al realizar la solicitud: {response.status_code}")
        return None


def eliminar_registro(registro_id):
    response = requests.delete(f"{url}/{registro_id}")
    if response.status_code == 200:
        return True
    else:
        print(f"Error al eliminar el registro: {response.status_code}")
        return False


def mostrar_registro(data):
    if data:
        print("Registro en formato plano:")
        for key, value in data.items():
            print(f"{key}: {value}")


def main():
    # Solicitar al usuario que ingrese el ID del registro que desea eliminar
    registro_id = input("Ingrese el ID del registro que desea eliminar: ")

    # Obtener el registro existente
    registro_existente = obtener_registro(registro_id)
    if not registro_existente:
        print("El registro no existe o no se pudo recuperar.")
        return

    # Mostrar los detalles del registro existente
    print("Detalles del registro a eliminar:")
    mostrar_registro(registro_existente)

    # Confirmar antes de eliminar el registro
    confirmar = input("\n¿Desea eliminar este registro? (sí/no): ").strip().lower()
    if confirmar in ['sí', 'si', 'yes', 'y']:
        # Eliminar el registro
        exito = eliminar_registro(registro_id)
        if exito:
            print("Registro eliminado exitosamente.")
        else:
            print("No se pudo eliminar el registro.")
    else:
        print("Eliminación no realizada.")


if __name__ == "__main__":
    main()
