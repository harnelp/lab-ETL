import sqlite3
import pandas as pd

def crear_base_de_datos():
    # Conexión a la base de datos (se crea si no existe)
    db = sqlite3.connect('calidad_aire.db')

    try:
        # Cargar y guardar datos demográficos en la base de datos
        df_demograficos = pd.read_csv("datos_demograficos.csv")
        print("Datos demográficos cargados correctamente.")
        print(df_demograficos.head())  # Imprime los primeros registros para verificar

        df_demograficos.to_sql('demografia', db, if_exists='replace', index=False)
        print("Datos demográficos guardados en la base de datos.")

        # Cargar y guardar datos de calidad del aire en la base de datos
        df_calidad_aire = pd.read_csv("calidad_aire.csv")
        print("Datos de calidad del aire cargados correctamente.")
        

        df_calidad_aire.to_sql('calidad_aire', db, if_exists='replace', index=False)
        print("Datos de calidad del aire guardados en la base de datos.")

    except Exception as e:
        print("Ocurrió un error durante la carga de datos: ", e)
    finally:
        # Cerrar la conexión a la base de datos
        db.close()
        print("Conexión a la base de datos cerrada.")

if __name__ == "__main__":
    crear_base_de_datos()


if __name__ == "__main__":
    crear_base_de_datos()