import pandas as pd
from typing import Set
import requests

def ej_1_cargar_datos_demograficos() -> pd.DataFrame:
    url = "https://public.opendatasoft.com/explore/dataset/us-cities-demographics/download/?format=csv&timezone=Europe/Berlin&lang=en&use_labels_for_header=true&csv_separator=%3B"
    data = pd.read_csv(url, sep=';')
    data.drop(columns=['Race', 'Count', 'Number of Veterans'], inplace=True)
    data.drop_duplicates(inplace=True)

    # Guardar los datos demográficos en un archivo CSV
    data.to_csv("datos_demograficos.csv", index=False)

    return data

def obtener_calidad_aire(ciudad: str, api_key: str) -> dict:
    api_url = f'https://api.api-ninjas.com/v1/airquality?city={ciudad}'
    response = requests.get(api_url, headers={'X-Api-Key': api_key})

    if response.status_code == requests.codes.ok:
        data = response.json()  # La respuesta se guarda en data

        try:
            # volcamos resultados a la variable concentraciones
            concentraciones = {k: v['concentration'] for k, v in data.items() if k != 'overall_aqi'}
            concentraciones['city'] = ciudad
            concentraciones['overall_aqi'] = data['overall_aqi']
            # devolvemos resultados obtenidos
            return concentraciones
        # manejamos errores
        except KeyError as e:
            print(f"Error en el formato de datos para la ciudad: {ciudad}, Error: {e}")
            return {}
    else:
        print("Error en la solicitud:", response.status_code, response.text)
        return {}
    
# segunda funcion
def ej_2_cargar_calidad_aire(ciudades: Set[str], api_key: str) -> None:
    calidad_aire = []
    for ciudad in ciudades:
        try:
            print(f"Obteniendo datos de calidad del aire para la ciudad: {ciudad}")
            datos = obtener_calidad_aire(ciudad, api_key)
            if datos:
                calidad_aire.append(datos)
        except Exception as e:
            print(f"No se pudieron obtener datos para la ciudad: {ciudad}. Error: {e}")

    if calidad_aire:  # Verifica si se recuperaron datos
        df_calidad_aire = pd.DataFrame(calidad_aire)
        df_calidad_aire.to_csv("calidad_aire.csv", index=False)
    else:
        print("No se recuperaron datos de calidad del aire.")


