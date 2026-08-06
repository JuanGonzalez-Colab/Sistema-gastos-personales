# Sistema de Gastos Personales

Un sistema de consola en Python para registrar y analizar gastos personales usando SQLite.
Permite llevar control de finanzas y ver resúmenes por mes y categoría.

## 🚀 Características

- *Agregar Gastos*: Guarda fecha, categoría, descripción y monto
- *Ver Historial*: Lista todos los gastos ordenados por fecha
- *Resumen Mensual*: Calcula el total gastado en un mes específico
- *Gastos por Categoría*: Agrupa y suma gastos usando GROUP BY de SQL
- *Base de Datos*: Usa SQLite para persistir los datos localmente

## 🛠️ Tecnologías Usadas

- *Python 3* (https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
- *SQLite3* - Base de datos embebida (https://img.shields.io/badge/SQLite-3776AB?style=for-the-badge&logo=sqlite&logoColor=white)
- *SQL* - Consultas con SELECT, SUM, GROUP BY, LIKE

## 📦 Cómo Usarlo

1.  Dale al siguiente botón: 
    [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/JuanGonzalez-Colab/Sistema-gastos-personales/blob/main/Gestor_gastos.ipynb)
2.  ´Ejecutar todo´ y listo
3.  Usa el menú: 1, 2, 3, 4, 5

## Ejemplo de uso
El sistema guarda los datos en un archivo ´gastos.db´ y te permite filtrar por mes:
´2026-08´ > Total gastado: $15300

## 👨‍💻 Autor
**Juan Gonzalez**
Proyecto realizado para practicar Python + SQL + Git/GitHub
