{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyM8+3VwDv4ikVRlwUJ5QV0U",
      "include_colab_link": True
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/JuanGonzalez-Colab/Sistema-gastos-personales/blob/main/app_gastos.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "!pip install streamlit"
      ],
      "metadata": {
        "id": "kpJBLel2wqbb"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "%%writefile app_gastos.py\n",
        "import streamlit as st\n",
        "import pandas as pd\n",
        "import matplotlib.pyplot as plt\n",
        "import sqlite3\n",
        "from datetime import datetime\n",
        "\n",
        "st.set_page_config(page_title=\"Gestor de Gastos v3.0\", layout=\"wide\")\n",
        "st.title(\"💸 Mi Gestor de Gastos Personal\")\n",
        "st.markdown(\"Cargá tus gastos y analizalos al instante\")\n",
        "\n",
        "conn = sqlite3.connect('gastos.db')\n",
        "c = conn.cursor()\n",
        "c.execute('''CREATE TABLE IF NOT EXISTS gastos\n",
        "             (id INTEGER PRIMARY KEY, fecha TEXT, categoria TEXT, monto REAL, descripcion TEXT)''')\n",
        "\n",
        "st.sidebar.header(\"Agregar Nuevo Gasto\")\n",
        "with st.sidebar.form(\"nuevo_gasto\"):\n",
        "    fecha = st.date_input(\"Fecha\", datetime.now())\n",
        "    categoria = st.selectbox(\"Categoría\", ['Comida', 'Transporte', 'Servicios', 'Ocio', 'Salud', 'Otros'])\n",
        "    monto = st.number_input(\"Monto $\", min_value=1.0, format=\"%.2f\")\n",
        "    descripcion = st.text_input(\"Descripción\")\n",
        "    submitted = st.form_submit_button(\"Guardar Gasto\")\n",
        "\n",
        "    if submitted:\n",
        "        c.execute(\"INSERT INTO gastos (fecha, categoria, monto, descripcion) VALUES (?, ?, ?, ?)\",\n",
        "                  (str(fecha), categoria, monto, descripcion))\n",
        "        conn.commit()\n",
        "        st.sidebar.success(\"Gasto guardado!\")\n",
        "        st.rerun()\n",
        "\n",
        "st.header(\"📊 Análisis de tus Gastos\")\n",
        "df = pd.read_sql_query(\"SELECT * FROM gastos\", conn)\n",
        "\n",
        "if not df.empty:\n",
        "    df['fecha'] = pd.to_datetime(df['fecha'])\n",
        "\n",
        "    col1, col2, col3 = st.columns(3)\n",
        "    col1.metric(\"Total Gastado\", f\"${df['monto'].sum():,.2f}\")\n",
        "    col2.metric(\"Promedio por Gasto\", f\"${df['monto'].mean():,.2f}\")\n",
        "    col3.metric(\"Cantidad de Gastos\", len(df))\n",
        "\n",
        "    st.subheader(\"Gastos por Categoría\")\n",
        "    gastos_cat = df.groupby('categoria')['monto'].sum()\n",
        "    fig, ax = plt.subplots()\n",
        "    gastos_cat.plot(kind='bar', ax=ax, color='skyblue')\n",
        "    ax.set_ylabel(\"Monto $\")\n",
        "    st.pyplot(fig)\n",
        "\n",
        "    st.subheader(\"Detalle de Gastos\")\n",
        "    st.dataframe(df, use_container_width=True)\n",
        "else:\n",
        "    st.info(\"Aún no cargaste gastos. Usá el formulario de la izquierda 👈\")\n",
        "\n",
        "conn.close()"
      ],
      "metadata": {
        "id": "Os9bHSrOwt3E"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "!streamlit run app_gastos.py --server.headless true & npx localtunnel --port 8501"
      ],
      "metadata": {
        "id": "EqmO4sqcwynR"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}
