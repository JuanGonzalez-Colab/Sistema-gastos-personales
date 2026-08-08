import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import sqlite3
from datetime import datetime

st.set_page_config(page_title="Gestor de Gastos v3.0", layout="wide")
st.title("💸 Mi Gestor de Gastos Personal")
st.markdown("Cargá tus gastos y analizalos al instante")

conn = sqlite3.connect('gastos.db')
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS gastos
             (id INTEGER PRIMARY KEY, fecha TEXT, categoria TEXT, monto REAL, descripcion TEXT)''')

st.sidebar.header("Agregar Nuevo Gasto")
with st.sidebar.form("nuevo_gasto"):
    fecha = st.date_input("Fecha", datetime.now())
    categoria = st.selectbox("Categoría", ['Comida', 'Transporte', 'Servicios', 'Ocio', 'Salud', 'Otros'])
    monto = st.number_input("Monto $", min_value=1.0, format="%.2f")
    descripcion = st.text_input("Descripción")
    submitted = st.form_submit_button("Guardar Gasto")
    
    if submitted:
        c.execute("INSERT INTO gastos (fecha, categoria, monto, descripcion) VALUES (?, ?, ?, ?)",
                  (str(fecha), categoria, monto, descripcion))
        conn.commit()
        st.sidebar.success("Gasto guardado!")
        st.rerun()

st.header("📊 Análisis de tus Gastos")
df = pd.read_sql_query("SELECT * FROM gastos", conn)

if not df.empty:
    df['fecha'] = pd.to_datetime(df['fecha'])
    
    col1, col2, col3 = st.columns(3)
    col1.metric("Total Gastado", f"${df['monto'].sum():,.2f}")
    col2.metric("Promedio por Gasto", f"${df['monto'].mean():,.2f}")
    col3.metric("Cantidad de Gastos", len(df))

    st.subheader("Gastos por Categoría")
    gastos_cat = df.groupby('categoria')['monto'].sum()
    fig, ax = plt.subplots()
    gastos_cat.plot(kind='bar', ax=ax, color='skyblue')
    ax.set_ylabel("Monto $")
    ax.set_xlabel("Categoría")
    st.pyplot(fig)

    st.subheader("Detalle de Gastos")
    st.dataframe(df, use_container_width=True)
else:
    st.info("Aún no cargaste gastos. Usá el formulario de la izquierda 👈")

conn.close()
