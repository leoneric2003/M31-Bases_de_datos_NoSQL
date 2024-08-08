import requests
import pandas as pd
import json

# URL de la API de MockAPI (verifica que esta sea la correcta)
url = "https://66b4e4d59f9169621ea4c11a.mockapi.io/api/v1/contactos"  # Reemplaza <tu-ID> con el ID correcto de tu proyecto

# Realizar la solicitud GET a la API
response = requests.get(url)

# Verificar si la solicitud fue exitosa
if response.status_code == 200:
    # Imprimir el contenido de la respuesta
    print("Contenido de la respuesta:")
    print(response.text)

    # Verificar si la respuesta tiene contenido
    if response.content:
        try:
            # Convertir la respuesta JSON a un diccionario de Python
            data = response.json()

            # Mostrar los datos en formato JSON formateado
            print("Datos en JSON formateado:")
            print(json.dumps(data, indent=4))

            # Convertir los datos en un DataFrame de pandas
            df = pd.DataFrame(data)

            # Mostrar el DataFrame
            print("\nDatos en DataFrame:")
            print(df)

            # Exportar el DataFrame a un archivo CSV
            df.to_csv("contactos.csv", index=False)
            print("\nDatos exportados a 'contactos.csv'")
        except json.JSONDecodeError as e:
            print(f"Error al decodificar el JSON: {e}")
    else:
        print("La respuesta está vacía.")
else:
    print(f"Error al realizar la solicitud: {response.status_code}")
