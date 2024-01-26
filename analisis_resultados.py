import sqlite3
import pandas as pd

def ejecutar_consulta():
    # Conectar a la base de datos SQLite
    db = sqlite3.connect('calidad_aire.db')

    # Consulta SQL para JOIN entre las tablas y ordenar por población y calidad del aire
    consulta_sql = """
    SELECT d.City, d.State, d.`Total Population`, a.overall_aqi
    FROM demografia d
    INNER JOIN calidad_aire a ON d.City = a.city
    ORDER BY d.`Total Population` DESC, a.overall_aqi DESC
    LIMIT 10
    """

    # Ejecutar la consulta y obtener los resultados
    resultados = pd.read_sql_query(consulta_sql, db)
    print(resultados)

    # Cerrar la conexión a la base de datos
    db.close()


if __name__ == "__main__":
    ejecutar_consulta()
