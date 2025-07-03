# 📊 Dashboard Ingenio Azucarero

Dashboard interactivo desarrollado con **Dash** y **Plotly**, conectado a una base de datos **SQL Server**, diseñado para visualizar y analizar la operación de proveedores en un Ingenio Azucarero.

Link de exposición del proyecto: https://youtu.be/2PavQ8z2gxk

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

![image](https://github.com/user-attachments/assets/1c45c072-a29f-4d3a-8056-6839013b2d9b)

## 🧠 Técnicas de Python Utilizadas

### 🔗 Conexión a Base de Datos (SQLAlchemy + PyODBC)
Se utiliza `SQLAlchemy` como ORM ligero junto con `pyodbc` para conectarse a bases de datos SQL Server. La conexión se realiza en el archivo `conexion.py`:

![image](https://github.com/user-attachments/assets/6f1c406b-c699-48d4-beb5-a531262949c6)



