# conexion.py
from sqlalchemy import create_engine

def obtener_engine():
    server = 'NB-PROYECTOS30'
    database = 'IngenioAzucarero'
    username = 'sa'
    password = 'Biosalc635'

    # Crear string de conexión
    connection_string = (
        f"mssql+pyodbc://{username}:{password}@{server}/{database}"
        "?driver=ODBC+Driver+17+for+SQL+Server"
    )

    # Crear y retornar el engine SQLAlchemy
    engine = create_engine(connection_string)
    return engine
