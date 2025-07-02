# 📊 Dashboard Ingenio Azucarero

Dashboard interactivo desarrollado con **Dash** y **Plotly**, conectado a una base de datos **SQL Server**, diseñado para visualizar y analizar la operación de proveedores en un Ingenio Azucarero.

---

## 🔎 Funcionalidades

✅ Visualización de:
- Toneladas de caña cosechadas por proveedor  
- Rendimiento promedio (%)  
- Ventas totales por proveedor  
- Calidad promedio (Brix y Pol)  
- Mapa interactivo de zonas de cosecha  
- Tendencia de toneladas cosechadas por fecha  

🎛️ Filtros:
- Proveedor  
- Rango de fechas  

🌗 Cambiar entre **tema claro y oscuro**

## 🧠 Técnicas de Python Utilizadas

### 🔗 Conexión a Base de Datos (SQLAlchemy + PyODBC)
Se utiliza `SQLAlchemy` como ORM ligero junto con `pyodbc` para conectarse a bases de datos SQL Server. La conexión se realiza en el archivo `conexion.py`:
