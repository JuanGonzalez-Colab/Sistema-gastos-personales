import sqlite3
from datetime import date

# 1. CONECTAR Y CREAR TABLA
conn = sqlite3.connect('gastos.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS gastos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    fecha TEXT NOT NULL,
    categoria TEXT NOT NULL,
    descripcion TEXT,
    monto REAL NOT NULL
)
''')
conn.commit()

# 2. FUNCIONES
def agregar_gasto():
    cat = input("Categoría: ")
    desc = input("Descripción: ")
    monto = float(input("Monto: $"))
    hoy = date.today()
    cursor.execute("INSERT INTO gastos (fecha, categoria, descripcion, monto) VALUES (?, ?, ?, ?)", 
                   (hoy, cat, desc, monto))
    conn.commit()
    print("Gasto guardado!")

def ver_gastos():
    cursor.execute("SELECT * FROM gastos ORDER BY fecha DESC")
    for fila in cursor.fetchall():
        print(fila)

def ver_total_mes():
    mes = input("Mes en formato AAAA-MM: ") # ej: 2026-08
    cursor.execute("SELECT SUM(monto) FROM gastos WHERE fecha LIKE ?", (mes+'%',))
    total = cursor.fetchone()[0]
    print(f"Total gastado en {mes}: ${total}")

def ver_gastos_por_categoria():
    cursor.execute("SELECT categoria, SUM(monto) FROM gastos GROUP BY categoria")
    print("\n--- GASTOS POR CATEGORÍA ---")
    for cat, total in cursor.fetchall():
        print(f"{cat}: ${total}")

# 3. MENÚ
while True:
    print("\n--- GESTOR DE GASTOS ---")
    print("1. Agregar Gasto")
    print("2. Ver todos los Gastos")
    print("3. Ver Total del Mes")
    print("4. Ver gastos por Categoría")
    print ("5. Salir")
    op = input("Opción: ")
    
    if op == "1": agregar_gasto()
    elif op == "2": ver_gastos()
    elif op == "3": ver_total_mes()
    elif op == "4": ver_gastos_por_categoria()
    elif op == "5": break
