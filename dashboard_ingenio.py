from dash import Dash, html, dcc, Input, Output, State
import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd
from datos import obtener_datos_dashboard, obtener_datos_mapa

# Tema inicial oscuro
tema_oscuro = dbc.themes.DARKLY
tema_claro = dbc.themes.FLATLY

app = Dash(__name__, external_stylesheets=[tema_oscuro], suppress_callback_exceptions=True)
app.title = "Dashboard Ingenio Azucarero"

# Cargar datos
toneladas_df, rendimiento_df, ventas_df, calidad_df = obtener_datos_dashboard()
mapa_df = obtener_datos_mapa()

# Lista de proveedores
todos_proveedores = sorted(list(set(toneladas_df['PROVEEDOR']) | set(rendimiento_df['PROVEEDOR']) | set(ventas_df['PROVEEDOR']) | set(calidad_df['PROVEEDOR'])))

# Layout
app.layout = html.Div([
    dcc.Store(id="tema-store", data={"tema": "oscuro"}),

    dbc.Container([
        dbc.Row([
            dbc.Col(html.H1("📊 Dashboard - Ingenio Azucarero", className="text-white"), width=10),
            dbc.Col([
                html.Button("💡", id="btn-tema", title="Cambiar tema", style={
                    "fontSize": "24px", "backgroundColor": "transparent", "color": "white", "border": "none"
                })
            ], width=2, style={"textAlign": "right", "paddingTop": "10px"})
        ], className="my-2"),

        dbc.Row([
            dbc.Col([
                html.Label("Proveedor", className="text-white"),
                dcc.Dropdown(
                    id="filtro-proveedor",
                    options=[{"label": prov, "value": prov} for prov in todos_proveedores],
                    value=None,
                    placeholder="Seleccione un proveedor (opcional)",
                    clearable=True,
                    style={
                        "backgroundColor": "#ffffff",
                        "color": "#000000",
                        "border": "1px solid #7f8c8d",
                        "borderRadius": "4px",
                        "width": "100%"
                    }
                )
            ], width=6),
            dbc.Col([
                html.Label("Rango de Fecha de Cosecha", className="text-white"),
                dcc.DatePickerRange(
                    id="filtro-fechas",
                    start_date=mapa_df['FECHA_COSECHA'].min(),
                    end_date=mapa_df['FECHA_COSECHA'].max(),
                    display_format="YYYY-MM-DD",
                    start_date_placeholder_text="Fecha inicial",
                    end_date_placeholder_text="Fecha final",
                    style={
                        "backgroundColor": "#2c3e50",
                        "color": "white",
                        "border": "1px solid #7f8c8d",
                        "padding": "6px",
                        "borderRadius": "4px",
                        "width": "100%"
                    },
                    clearable=True
                )
            ], width=6)
        ], className="mb-4"),

        dbc.Row([
            dbc.Col(dcc.Graph(id="grafico-toneladas"), width=6),
            dbc.Col(dcc.Graph(id="grafico-rendimiento"), width=6),
        ]),

        dbc.Row([
            dbc.Col(dcc.Graph(id="grafico-ventas"), width=6),
            dbc.Col(dcc.Graph(id="grafico-calidad"), width=6),
        ], className="my-4"),

        dbc.Row([
            dbc.Col(dcc.Graph(id="grafico-mapbox"), width=12)
        ]),

        dbc.Row([
            dbc.Col(dcc.Graph(id="grafico-nuevo-kpi"))
        ], className="my-4")
    ], fluid=True)
])

# Callback para alternar el tema
@app.callback(
    Output("tema-store", "data"),
    Input("btn-tema", "n_clicks"),
    State("tema-store", "data"),
    prevent_initial_call=True
)
def cambiar_tema(n_clicks, data_actual):
    tema_actual = data_actual["tema"]
    nuevo_tema = "claro" if tema_actual == "oscuro" else "oscuro"
    return {"tema": nuevo_tema}

# Callback principal para actualizar gráficas
@app.callback(
    Output("grafico-toneladas", "figure"),
    Output("grafico-rendimiento", "figure"),
    Output("grafico-ventas", "figure"),
    Output("grafico-calidad", "figure"),
    Output("grafico-mapbox", "figure"),
    Output("grafico-nuevo-kpi", "figure"),
    Input("filtro-proveedor", "value"),
    Input("filtro-fechas", "start_date"),
    Input("filtro-fechas", "end_date"),
    Input("tema-store", "data")
)
def actualizar_dashboard(filtro_prov, fecha_ini, fecha_fin, tema_info):
    toneladas, rendimiento, ventas, calidad = obtener_datos_dashboard()
    mapa = obtener_datos_mapa()

    # Asegurar fechas como datetime
    mapa['FECHA_COSECHA'] = pd.to_datetime(mapa['FECHA_COSECHA'])

    if filtro_prov:
        toneladas = toneladas[toneladas['PROVEEDOR'] == filtro_prov]
        rendimiento = rendimiento[rendimiento['PROVEEDOR'] == filtro_prov]
        ventas = ventas[ventas['PROVEEDOR'] == filtro_prov]
        calidad = calidad[calidad['PROVEEDOR'] == filtro_prov]
        mapa = mapa[mapa['NOMBRE_ZONA'].str.contains(filtro_prov, case=False, na=False)]

    if fecha_ini and fecha_fin:
        mapa_filtrado = mapa[(mapa['FECHA_COSECHA'] >= pd.to_datetime(fecha_ini)) & 
                             (mapa['FECHA_COSECHA'] <= pd.to_datetime(fecha_fin))]
    else:
        mapa_filtrado = mapa

    tema_plotly = "plotly_dark" if tema_info["tema"] == "oscuro" else "plotly_white"
    fondo_transparente = 'rgba(0,0,0,0)' if tema_info["tema"] == "oscuro" else 'white'

    fig_ton = px.bar(toneladas, x='PROVEEDOR', y='TOTAL_TONELADAS', title="Toneladas Cosechadas por Proveedor",
                     template=tema_plotly, color='PROVEEDOR').update_layout(paper_bgcolor=fondo_transparente,
                     plot_bgcolor=fondo_transparente)

    fig_rdto = px.bar(rendimiento, x='PROVEEDOR', y='RDTO_PROMEDIO', title="Rendimiento Promedio (%)",
                      template=tema_plotly, color='PROVEEDOR').update_layout(paper_bgcolor=fondo_transparente,
                      plot_bgcolor=fondo_transparente)

    fig_ventas = px.pie(ventas, values='VENTA_TOTAL', names='PROVEEDOR', title="Distribución de Ventas por Proveedor",
                        template=tema_plotly).update_layout(paper_bgcolor=fondo_transparente)

    fig_calidad = px.bar(calidad, x='PROVEEDOR', y=['BRIX_PROM', 'POL_PROM'], title="Calidad Promedio (Brix y Pol)",
                         barmode='group', template=tema_plotly).update_layout(paper_bgcolor=fondo_transparente,
                         plot_bgcolor=fondo_transparente)

    fig_mapa = px.scatter_mapbox(mapa_filtrado, lat="LATITUD", lon="LONGITUD", hover_name="NOMBRE_ZONA",
                  hover_data={"TONELADAS_CANA": True, "RDTO_PORC": True}, color="TONELADAS_CANA",
                  size="TONELADAS_CANA", zoom=8, mapbox_style="open-street-map",
                  title="📍 Zonas de Cosecha por Toneladas").update_layout(paper_bgcolor=fondo_transparente)

    df_fecha = mapa_filtrado.groupby("FECHA_COSECHA")["TONELADAS_CANA"].sum().reset_index()
    fig_kpi_nuevo = px.line(df_fecha, x="FECHA_COSECHA", y="TONELADAS_CANA", markers=True,
                            title="Tendencia de Toneladas por Fecha de Cosecha",
                            template=tema_plotly).update_layout(paper_bgcolor=fondo_transparente,
                            plot_bgcolor=fondo_transparente)

    return fig_ton, fig_rdto, fig_ventas, fig_calidad, fig_mapa, fig_kpi_nuevo

if __name__ == '__main__':
    app.run(debug=True)
