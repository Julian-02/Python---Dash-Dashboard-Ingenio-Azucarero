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

---

## 📁 Estructura del proyecto

```bash
dashboard-ingenio/
├── app.py              # Código principal de la app con Dash
├── datos.py            # Consultas SQL con pandas + SQLAlchemy
├── conexion.py         # Conexión a SQL Server (ajustar según entorno)
├── requirements.txt    # Lista de dependencias del proyecto
└── README.md           # Documentación del proyecto
