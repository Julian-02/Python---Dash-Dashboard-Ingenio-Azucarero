# datos.py
import pandas as pd
from conexion import obtener_engine

def obtener_datos_dashboard():
    engine = obtener_engine()

    toneladas = pd.read_sql("""
        SELECT P.NOMBRE AS PROVEEDOR, SUM(C.TONELADAS_CANA) AS TOTAL_TONELADAS
        FROM COSECHAS C
        INNER JOIN FINCAS F ON C.ID_FINCA = F.ID_FINCA
        INNER JOIN PROVEEDORES P ON F.ID_PROVEEDOR = P.ID_PROVEEDOR
        GROUP BY P.NOMBRE
    """, engine)

    rendimiento = pd.read_sql("""
        SELECT P.NOMBRE AS PROVEEDOR, AVG(C.RDTO_PORC) AS RDTO_PROMEDIO
        FROM COSECHAS C
        INNER JOIN FINCAS F ON C.ID_FINCA = F.ID_FINCA
        INNER JOIN PROVEEDORES P ON F.ID_PROVEEDOR = P.ID_PROVEEDOR
        GROUP BY P.NOMBRE
    """, engine)

    ventas = pd.read_sql("""
        SELECT P.NOMBRE AS PROVEEDOR, SUM(V.MONTO_TOTAL) AS VENTA_TOTAL
        FROM VENTAS V
        INNER JOIN PROVEEDORES P ON V.ID_PROVEEDOR = P.ID_PROVEEDOR
        GROUP BY P.NOMBRE
    """, engine)

    calidad = pd.read_sql("""
        SELECT P.NOMBRE AS PROVEEDOR, AVG(Q.Brix) AS BRIX_PROM, AVG(Q.Pol) AS POL_PROM
        FROM CALIDAD_CANA Q
        INNER JOIN COSECHAS C ON Q.ID_COSECHA = C.ID_COSECHA
        INNER JOIN FINCAS F ON C.ID_FINCA = F.ID_FINCA
        INNER JOIN PROVEEDORES P ON F.ID_PROVEEDOR = P.ID_PROVEEDOR
        GROUP BY P.NOMBRE
    """, engine)

    return toneladas, rendimiento, ventas, calidad

# ✅ Esta función DEBE estar fuera
def obtener_datos_mapa():
    engine = obtener_engine()
    mapa_df = pd.read_sql("""
        SELECT ID_ZONA, NOMBRE_ZONA, LATITUD, LONGITUD,
               TONELADAS_CANA, RDTO_PORC, FECHA_COSECHA
        FROM ZONAS_COSECHA
    """, con=engine)
    return mapa_df
