"""
Generador de Datos Sintéticos — Grupo Jaloma PoC
BI + IA: De la Intuición a los Datos
Autor: PoC Team
"""

import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random
import os

np.random.seed(42)
random.seed(42)

OUTPUT_DIR = os.path.join(os.path.dirname(__file__))
os.makedirs(OUTPUT_DIR, exist_ok=True)

# ─────────────────────────────────────────────
# PARÁMETROS GLOBALES
# ─────────────────────────────────────────────
START_DATE = datetime(2023, 1, 1)
END_DATE   = datetime(2024, 12, 31)
DATES      = pd.date_range(START_DATE, END_DATE, freq="D")

print("🚀 Iniciando generación de datos sintéticos Grupo Jaloma...")

# ─────────────────────────────────────────────
# 1. CLIENTES
# ─────────────────────────────────────────────
print("\n📋 Generando clientes...")

clientes_data = [
    # Canal FARMACIA CADENA
    ("CLI001", "Farmacias Guadalajara Nacional",     "Farmacia Cadena",  "Occidente", "Carlos Mendoza",   30, "A", 2800000),
    ("CLI002", "Farmacias del Ahorro Corporativo",   "Farmacia Cadena",  "CDMX",      "Carlos Mendoza",   30, "A", 2400000),
    ("CLI003", "Farmacias Benavides Nacional",       "Farmacia Cadena",  "Norte",     "Laura Castillo",   30, "A", 1900000),
    ("CLI004", "Farmacias San Pablo CDMX",           "Farmacia Cadena",  "CDMX",      "Carlos Mendoza",   30, "A",  980000),
    ("CLI005", "Farmacias Similares Corporativo",    "Farmacia Cadena",  "CDMX",      "Laura Castillo",   30, "A", 1500000),
    ("CLI006", "Farmacias YZA Sureste",              "Farmacia Cadena",  "Sur",       "Ricardo Navarro",  30, "B",  560000),
    ("CLI007", "Farmacon Occidente",                 "Farmacia Cadena",  "Occidente", "Ana Gutiérrez",    30, "B",  420000),
    ("CLI008", "Farmacias El Fénix",                 "Farmacia Cadena",  "Occidente", "Ana Gutiérrez",    30, "B",  380000),
    ("CLI009", "Super Farmacia Occidente",           "Farmacia Cadena",  "Occidente", "Ana Gutiérrez",    30, "B",  310000),
    ("CLI010", "Farmacias La Generosa",              "Farmacia Cadena",  "Centro",    "Miguel Herrera",   30, "C",  180000),

    # Canal AUTOSERVICIO
    ("CLI011", "Walmart de México Operaciones",      "Autoservicio",     "CDMX",      "Carlos Mendoza",   45, "A", 3200000),
    ("CLI012", "Soriana Supermercados Nacional",      "Autoservicio",     "Norte",     "Laura Castillo",   45, "A", 1800000),
    ("CLI013", "Chedraui Corporativo",               "Autoservicio",     "Centro",    "Miguel Herrera",   45, "A", 1400000),
    ("CLI014", "La Comer / Fresko",                  "Autoservicio",     "CDMX",      "Carlos Mendoza",   45, "B",  650000),
    ("CLI015", "HEB México",                         "Autoservicio",     "Norte",     "Laura Castillo",   30, "B",  580000),
    ("CLI016", "Mega Soriana",                       "Autoservicio",     "Norte",     "Laura Castillo",   45, "B",  490000),
    ("CLI017", "Bodega Aurrera Nacional",             "Autoservicio",     "CDMX",      "Carlos Mendoza",   30, "A", 1200000),

    # Canal CONVENIENCIA
    ("CLI018", "OXXO Región Centro",                 "Conveniencia",     "CDMX",      "Miguel Herrera",   30, "A", 1100000),
    ("CLI019", "OXXO Región Occidente",              "Conveniencia",     "Occidente", "Ana Gutiérrez",    30, "A",  950000),
    ("CLI020", "OXXO Región Norte",                  "Conveniencia",     "Norte",     "Laura Castillo",   30, "A",  870000),
    ("CLI021", "7-Eleven México",                    "Conveniencia",     "CDMX",      "Miguel Herrera",   30, "B",  380000),
    ("CLI022", "Circle K México",                    "Conveniencia",     "Norte",     "Laura Castillo",   30, "B",  310000),

    # Canal MAYORISTA
    ("CLI023", "Grupo Nadro Distribución",           "Mayorista",        "CDMX",      "Carlos Mendoza",   45, "A", 2200000),
    ("CLI024", "Casa Marzam",                        "Mayorista",        "CDMX",      "Carlos Mendoza",   45, "A", 1700000),
    ("CLI025", "Distribuidora Fármacos Nacionales",  "Mayorista",        "Norte",     "Laura Castillo",   45, "A", 1400000),
    ("CLI026", "Droguería Cosmopolita Nacional",     "Mayorista",        "CDMX",      "Miguel Herrera",   45, "B",  780000),
    ("CLI027", "Distribuidora TAD Occidente",        "Mayorista",        "Occidente", "Ana Gutiérrez",    45, "B",  560000),
    ("CLI028", "Maypo Distribuidora",                "Mayorista",        "Centro",    "Miguel Herrera",   45, "B",  420000),
    ("CLI029", "Abarrotera del Bajío",               "Mayorista",        "Centro",    "Ricardo Navarro",  45, "B",  380000),
    ("CLI030", "Distribuidora Occidente Salud",      "Mayorista",        "Occidente", "Ana Gutiérrez",    45, "C",  210000),

    # Canal INSTITUCIONAL (Gobierno / Hospitales)
    ("CLI031", "IMSS Abasto Nacional",               "Institucional",    "CDMX",      "Ricardo Navarro",  60, "A", 1600000),
    ("CLI032", "ISSSTE Abasto Central",              "Institucional",    "CDMX",      "Ricardo Navarro",  60, "B",  680000),
    ("CLI033", "Hospitales Ángeles Corporativo",     "Institucional",    "CDMX",      "Ricardo Navarro",  45, "B",  520000),
    ("CLI034", "Cruz Roja Mexicana",                 "Institucional",    "CDMX",      "Ricardo Navarro",  60, "B",  380000),
    ("CLI035", "Hospital Civil de Guadalajara",      "Institucional",    "Occidente", "Ana Gutiérrez",    60, "B",  340000),
    ("CLI036", "Secretaría de Salud Jalisco",        "Institucional",    "Occidente", "Ana Gutiérrez",    60, "C",  280000),
    ("CLI037", "DIF Nacional",                       "Institucional",    "CDMX",      "Ricardo Navarro",  60, "C",  220000),

    # Canal EXPORTACIÓN
    ("CLI038", "Dist. Farmacéutica Guatemala",       "Exportación",      "Centroamérica", "Ricardo Navarro", 45, "A",  920000),
    ("CLI039", "Dist. Productos Salud El Salvador",  "Exportación",      "Centroamérica", "Ricardo Navarro", 45, "B",  480000),
    ("CLI040", "Dist. Honduras Medical Supplies",    "Exportación",      "Centroamérica", "Ricardo Navarro", 60, "B",  350000),
    ("CLI041", "Latin Products USA Inc.",             "Exportación",      "USA",           "Carlos Mendoza",  45, "B",  620000),
    ("CLI042", "Hispanic Health Products CA",        "Exportación",      "USA",           "Carlos Mendoza",  45, "C",  280000),

    # Canal E-COMMERCE
    ("CLI043", "Amazon México Marketplace",          "E-commerce",       "CDMX",      "Miguel Herrera",   15, "A",  780000),
    ("CLI044", "Mercado Libre México",               "E-commerce",       "CDMX",      "Miguel Herrera",   15, "B",  420000),
    ("CLI045", "Cornershop / Uber Eats Salud",       "E-commerce",       "CDMX",      "Miguel Herrera",   15, "B",  280000),

    # Clientes medianos y pequeños (long tail)
    *[
        (f"CLI{45+i:03d}", f"Cliente Regional {45+i}",
         random.choice(["Farmacia Cadena", "Mayorista", "Farmacia Independiente", "Autoservicio Regional"]),
         random.choice(["CDMX", "Norte", "Occidente", "Centro", "Sur", "Centroamérica"]),
         random.choice(["Carlos Mendoza", "Laura Castillo", "Ana Gutiérrez", "Miguel Herrera", "Ricardo Navarro"]),
         random.choice([15, 30, 45]),
         "C",
         random.randint(35000, 150000))
        for i in range(1, 36)
    ]
]

clientes = pd.DataFrame(clientes_data, columns=[
    "cliente_id", "nombre", "canal", "region",
    "ejecutivo", "credito_dias", "segmento", "venta_anual_potencial_mxn"
])

# Fecha de alta: mayoría antes del período, algunos nuevos en 2023-2024
clientes["fecha_alta"] = [
    START_DATE - timedelta(days=random.randint(180, 1800)) if i < 60
    else START_DATE + timedelta(days=random.randint(0, 400))
    for i in range(len(clientes))
]

clientes.to_csv(f"{OUTPUT_DIR}/clientes.csv", index=False)
print(f"  ✅ {len(clientes)} clientes generados")


# ─────────────────────────────────────────────
# 2. PRODUCTOS (basado en catálogo real Grupo Jaloma)
# ─────────────────────────────────────────────
print("\n📦 Generando catálogo de productos...")

productos_data = [
    # SKU, Nombre, Marca, Categoría, Precio_lista_MXN, Costo_MXN, Peso_kg, Uds/caja, Rotación, Temporalidad

    # ACEITES COSMÉTICOS — Línea estrella de Jaloma
    ("SKU001", "Aceite de Almendras Dulces 12/120ml",      "Jaloma Belleza",  "Cuidado Personal",   720,  360, 1.5,  12, "alta",   "todo_año"),
    ("SKU002", "Aceite de Almendras Dulces 12/250ml",      "Jaloma Belleza",  "Cuidado Personal",  1080,  540, 3.0,  12, "alta",   "todo_año"),
    ("SKU003", "Aceite de Aguacate Orgánico 12/120ml",     "Jaloma Belleza",  "Cuidado Personal",   840,  420, 1.5,  12, "alta",   "todo_año"),
    ("SKU004", "Aceite de Argán Premium 12/60ml",          "Jaloma Belleza",  "Cuidado Personal",  1440,  720, 0.8,  12, "media",  "todo_año"),
    ("SKU005", "Aceite de Coco Orgánico 12/120ml",         "Jaloma Belleza",  "Cuidado Personal",   780,  390, 1.5,  12, "alta",   "verano"),
    ("SKU006", "Aceite de Ricino Puro 12/120ml",           "Jaloma Belleza",  "Cuidado Personal",   660,  330, 1.5,  12, "alta",   "todo_año"),
    ("SKU007", "Aceite de Oliva Cosmético 12/120ml",       "Jaloma Belleza",  "Cuidado Personal",   720,  360, 1.5,  12, "media",  "todo_año"),
    ("SKU008", "Aceite de Mamey para Cabello 12/120ml",    "Jaloma Belleza",  "Cuidado Personal",   690,  345, 1.5,  12, "media",  "todo_año"),
    ("SKU009", "Aceite de Rosa Mosqueta 12/60ml",          "Jaloma Belleza",  "Cuidado Personal",  1560,  780, 0.8,  12, "baja",   "todo_año"),

    # CUIDADO PERSONAL — Geles, Cremas, Agua
    ("SKU010", "Agua de Rosas Tónico Facial 12/250ml",     "Jaloma Belleza",  "Cuidado Personal",   600,  300, 3.0,  12, "alta",   "todo_año"),
    ("SKU011", "Gel de Árnica Antiinflamatorio 12/250ml",   "Jaloma Belleza",  "Cuidado Personal",   780,  390, 3.0,  12, "alta",   "todo_año"),
    ("SKU012", "Gel de Pepino c/ Ácido Hialurónico 12/250ml","Jaloma Belleza","Cuidado Personal",   840,  420, 3.0,  12, "alta",   "todo_año"),
    ("SKU013", "Vaselina Pura 12/215g",                    "Jaloma",          "Cuidado Personal",   480,  240, 2.6,  12, "alta",   "invierno"),
    ("SKU014", "Gel Antibacterial 12/250ml",               "Jaloma",          "Cuidado Personal",   540,  270, 3.0,  12, "alta",   "invierno"),
    ("SKU015", "Fijador para Cabello Extra Fuerte 12/350ml","Jaloma Belleza", "Cuidado Personal",   720,  360, 4.2,  12, "media",  "todo_año"),
    ("SKU016", "Gel para Cabello Extra Fuerte 12/250g",    "Jaloma Belleza",  "Cuidado Personal",   600,  300, 3.0,  12, "media",  "todo_año"),
    ("SKU017", "Loción Calamina 12/120ml",                 "Jaloma",          "Cuidado Personal",   540,  270, 1.5,  12, "media",  "verano"),

    # MATERIAL DE CURACIÓN
    ("SKU018", "Algodón Absorbente 12/100g",               "Jaloma Curación", "Material de Curación", 420, 210, 1.2,  12, "alta",   "todo_año"),
    ("SKU019", "Algodón Absorbente 12/300g",               "Jaloma Curación", "Material de Curación", 840, 420, 3.6,  12, "alta",   "todo_año"),
    ("SKU020", "Gasas Estériles 7.5x5cm 12/100pz",        "Jaloma Curación", "Material de Curación", 960, 480, 1.2,  12, "alta",   "todo_año"),
    ("SKU021", "Vendas Elásticas 7.5cm 12/12pz",          "Jaloma Curación", "Material de Curación", 720, 360, 1.0,  12, "alta",   "todo_año"),
    ("SKU022", "Vendas Elásticas 10cm 12/12pz",           "Jaloma Curación", "Material de Curación", 840, 420, 1.3,  12, "alta",   "todo_año"),
    ("SKU023", "Curitas Adhesivas Surtidas 24/100pz",      "Jaloma Curación", "Material de Curación", 960, 480, 2.4,  24, "alta",   "todo_año"),
    ("SKU024", "Cinta Adhesiva Micropore 24/5m",           "Jaloma Curación", "Material de Curación", 720, 360, 1.5,  24, "alta",   "todo_año"),
    ("SKU025", "Solución Antiséptica Yodada 12/120ml",     "Jaloma Curación", "Material de Curación", 540, 270, 1.5,  12, "alta",   "todo_año"),
    ("SKU026", "Alcohol Desnaturalizado 12/500ml",         "Jaloma Curación", "Material de Curación", 480, 240, 6.0,  12, "alta",   "invierno"),
    ("SKU027", "Agua Oxigenada 12/480ml",                  "Jaloma Curación", "Material de Curación", 420, 210, 5.8,  12, "alta",   "todo_año"),
    ("SKU028", "Botiquín Primeros Auxilios Básico 6/1pz",  "Jaloma Curación", "Material de Curación",1680, 840, 3.0,   6, "baja",   "todo_año"),
    ("SKU029", "Tela Adhesiva 12/5m",                      "Jaloma Curación", "Material de Curación", 540, 270, 1.0,  12, "media",  "todo_año"),
    ("SKU030", "Termómetro Digital 12/1pz",                "Jaloma Curación", "Material de Curación",1440, 720, 0.5,  12, "media",  "invierno"),

    # PRODUCTOS PARA BEBÉ
    ("SKU031", "Aceite para Bebé Hipoalergénico 12/250ml", "Jaloma Bebé",     "Productos para Bebé", 780, 390, 3.0,  12, "alta",   "todo_año"),
    ("SKU032", "Jabón Líquido para Bebé 12/400ml",        "Jaloma Bebé",     "Productos para Bebé", 720, 360, 4.8,  12, "alta",   "todo_año"),
    ("SKU033", "Shampoo para Bebé Sin Lágrimas 12/400ml", "Jaloma Bebé",     "Productos para Bebé", 780, 390, 4.8,  12, "alta",   "todo_año"),
    ("SKU034", "Talco para Bebé 12/200g",                 "Jaloma Bebé",     "Productos para Bebé", 540, 270, 2.4,  12, "alta",   "todo_año"),
    ("SKU035", "Crema para Rozaduras 12/120g",            "Jaloma Bebé",     "Productos para Bebé", 660, 330, 1.5,  12, "alta",   "todo_año"),
    ("SKU036", "Toallitas Húmedas Bebé 12/80pz",          "Jaloma Bebé",     "Productos para Bebé", 600, 300, 6.0,  12, "alta",   "todo_año"),
    ("SKU037", "Colonia para Bebé 12/250ml",              "Jaloma Bebé",     "Productos para Bebé", 660, 330, 3.0,  12, "media",  "todo_año"),
    ("SKU038", "Jabón en Barra Bebé 24/100g",             "Jaloma Bebé",     "Productos para Bebé", 480, 240, 2.4,  24, "media",  "todo_año"),

    # ACCESORIOS FARMACÉUTICOS / DESECHABLES
    ("SKU039", "Guantes de Látex Caja 10/100pz",          "Jaloma",          "Accesorios Farmacéuticos", 1200, 600, 5.0,  10, "alta",   "todo_año"),
    ("SKU040", "Guantes de Nitrilo Caja 10/100pz",        "Jaloma",          "Accesorios Farmacéuticos", 1500, 750, 5.0,  10, "alta",   "todo_año"),
    ("SKU041", "Cubrebocas Tricapa 10/50pz",              "Jaloma",          "Accesorios Farmacéuticos",  480, 240, 2.5,  10, "alta",   "invierno"),
    ("SKU042", "Batas Desechables 12/10pz",               "Jaloma",          "Accesorios Farmacéuticos",  720, 360, 2.0,  12, "media",  "todo_año"),
    ("SKU043", "Jeringas Desechables 3ml 50/100pz",       "Jaloma",          "Accesorios Farmacéuticos", 1800, 900, 5.0,  50, "alta",   "invierno"),
    ("SKU044", "Cofias Desechables 12/100pz",             "Jaloma",          "Accesorios Farmacéuticos",  360, 180, 1.0,  12, "baja",   "todo_año"),
    ("SKU045", "Abatelenguas de Madera 12/500pz",         "Jaloma",          "Accesorios Farmacéuticos",  480, 240, 3.0,  12, "media",  "invierno"),

    # LÍNEA FARMACÉUTICA
    ("SKU046", "Suero Fisiológico 12/500ml",              "Jaloma",          "Industria Farmacéutica", 600, 300, 6.0,  12, "alta",   "todo_año"),
    ("SKU047", "Glicerina Líquida 12/120ml",              "Jaloma",          "Industria Farmacéutica", 420, 210, 1.5,  12, "media",  "todo_año"),
    ("SKU048", "Bicarbonato de Sodio Farma 12/250g",      "Jaloma",          "Industria Farmacéutica", 360, 180, 3.0,  12, "media",  "todo_año"),
    ("SKU049", "Aceite Mineral USP 12/250ml",             "Jaloma",          "Industria Farmacéutica", 540, 270, 3.0,  12, "alta",   "todo_año"),
    ("SKU050", "Tintura de Yodo 12/30ml",                 "Jaloma",          "Industria Farmacéutica", 480, 240, 0.4,  12, "media",  "todo_año"),

    # EMPAQUES PLÁSTICOS (Intercompañía Plásticos Jaloma → Distribuidora)
    ("SKU051", "Envase PET 120ml Transparente 1000/pz",   "Plásticos Jaloma","Envases y Empaques",  2400,1200,15.0,1000, "alta",   "todo_año"),
    ("SKU052", "Envase PET 250ml Transparente 500/pz",    "Plásticos Jaloma","Envases y Empaques",  1800, 900,12.0, 500, "alta",   "todo_año"),
    ("SKU053", "Tapa Rosca 28mm 2000/pz",                 "Plásticos Jaloma","Envases y Empaques",   960, 480, 5.0,2000, "alta",   "todo_año"),
    ("SKU054", "Envase HDPE 500ml Blanco 500/pz",         "Plásticos Jaloma","Envases y Empaques",  2100,1050,14.0, 500, "alta",   "todo_año"),
    ("SKU055", "Dosificador Spray 28mm 1000/pz",          "Plásticos Jaloma","Envases y Empaques",  1500, 750, 6.0,1000, "media",  "todo_año"),

    # HIGIENE Y BIENESTAR
    ("SKU056", "Jabón Antibacterial Líquido 12/500ml",    "Jaloma",          "Cuidado Personal",    660, 330, 6.0,  12, "alta",   "invierno"),
    ("SKU057", "Gel Desinfectante Manos 12/1L",           "Jaloma",          "Cuidado Personal",    840, 420, 12.0, 12, "alta",   "invierno"),
    ("SKU058", "Crema Corporal Humectante 12/250ml",      "Jaloma Belleza",  "Cuidado Personal",    720, 360, 3.0,  12, "media",  "invierno"),
]

productos = pd.DataFrame(productos_data, columns=[
    "sku", "nombre", "marca", "categoria",
    "precio_lista_mxn", "costo_mxn", "peso_kg",
    "unidades_por_caja", "rotacion_esperada", "temporalidad"
])
productos["margen_bruto_pct"] = ((productos["precio_lista_mxn"] - productos["costo_mxn"]) / productos["precio_lista_mxn"] * 100).round(1)

productos.to_csv(f"{OUTPUT_DIR}/productos.csv", index=False)
print(f"  ✅ {len(productos)} SKUs generados")


# ─────────────────────────────────────────────
# HELPER: Factor de estacionalidad realista
# ─────────────────────────────────────────────
def estacionalidad_factor(fecha, temporalidad):
    mes = fecha.month

    base = 1.0

    if temporalidad == "todo_año":
        if mes in [11, 12]: base *= 1.20
        elif mes in [1, 2]: base *= 0.90
        elif mes in [5]:     base *= 1.15  # Día de las madres

    elif temporalidad == "verano":
        if mes in [5, 6, 7, 8]: base *= 1.5
        elif mes in [11, 12, 1]: base *= 0.7
        else: base *= 1.0

    elif temporalidad == "invierno":
        # Temporada de gripe e infecciones respiratorias
        if mes in [10, 11, 12, 1, 2]: base *= 1.8
        elif mes in [5, 6, 7]: base *= 0.6
        else: base *= 0.9

    return base


def canal_sku_affinity(canal, categoria, marca):
    """Determina qué tan probable es que un canal compre un SKU dado"""
    affinities = {
        "Farmacia Cadena":       {"Cuidado Personal": 1.8, "Material de Curación": 1.9, "Productos para Bebé": 1.6, "Accesorios Farmacéuticos": 1.5, "Industria Farmacéutica": 1.7, "Envases y Empaques": 0.1},
        "Autoservicio":          {"Cuidado Personal": 1.9, "Productos para Bebé": 1.8, "Material de Curación": 1.4, "Accesorios Farmacéuticos": 0.8, "Industria Farmacéutica": 0.6, "Envases y Empaques": 0.1},
        "Conveniencia":          {"Cuidado Personal": 1.6, "Material de Curación": 1.3, "Productos para Bebé": 0.8, "Accesorios Farmacéuticos": 0.6, "Industria Farmacéutica": 0.3, "Envases y Empaques": 0.0},
        "Mayorista":             {"Cuidado Personal": 1.5, "Material de Curación": 1.6, "Productos para Bebé": 1.5, "Accesorios Farmacéuticos": 1.7, "Industria Farmacéutica": 1.5, "Envases y Empaques": 0.3},
        "Institucional":         {"Material de Curación": 2.2, "Accesorios Farmacéuticos": 2.0, "Industria Farmacéutica": 1.8, "Cuidado Personal": 0.8, "Productos para Bebé": 0.5, "Envases y Empaques": 0.1},
        "Exportación":           {"Cuidado Personal": 1.6, "Material de Curación": 1.5, "Productos para Bebé": 1.4, "Accesorios Farmacéuticos": 1.3, "Industria Farmacéutica": 1.2, "Envases y Empaques": 0.2},
        "E-commerce":            {"Cuidado Personal": 2.0, "Productos para Bebé": 1.8, "Material de Curación": 1.3, "Accesorios Farmacéuticos": 0.7, "Industria Farmacéutica": 0.5, "Envases y Empaques": 0.0},
        "Farmacia Independiente": {"Cuidado Personal": 1.5, "Material de Curación": 1.8, "Productos para Bebé": 1.3, "Accesorios Farmacéuticos": 1.4, "Industria Farmacéutica": 1.5, "Envases y Empaques": 0.1},
        "Autoservicio Regional":  {"Cuidado Personal": 1.6, "Productos para Bebé": 1.5, "Material de Curación": 1.3, "Accesorios Farmacéuticos": 0.6, "Industria Farmacéutica": 0.5, "Envases y Empaques": 0.0},
    }
    canal_aff = affinities.get(canal, {})
    factor = canal_aff.get(categoria, 1.0)

    # Bonus especial para Plásticos Jaloma en canal Institucional/Mayorista (intercompañía)
    if marca == "Plásticos Jaloma" and canal in ["Institucional", "Mayorista"]:
        factor *= 1.4
    if marca == "Plásticos Jaloma" and canal in ["Conveniencia", "E-commerce", "Farmacia Cadena"]:
        factor *= 0.1

    return factor


# ─────────────────────────────────────────────
# 3. VENTAS — el corazón de la PoC
# ─────────────────────────────────────────────
print("\n💰 Generando ventas (esto toma un momento)...")

# SKUs "estrella" que generarán quiebres de stock
SKUS_ESTRELLA = ["SKU001", "SKU002", "SKU005", "SKU011", "SKU014", "SKU018",
                 "SKU020", "SKU023", "SKU031", "SKU039", "SKU040", "SKU041"]

# Períodos donde habrá quiebre (para dramatizar la historia)
QUIEBRES_PROGRAMADOS = {
    "SKU014": [(datetime(2023, 11, 15), datetime(2023, 12, 5)),     # Gel antibacterial en temporada gripe
               (datetime(2024, 1, 10), datetime(2024, 1, 25))],     # Gripe enero
    "SKU041": [(datetime(2023, 10, 20), datetime(2023, 11, 8)),     # Cubrebocas temporada respiratoria
               (datetime(2024, 11, 1), datetime(2024, 11, 18))],
    "SKU020": [(datetime(2024, 6, 1), datetime(2024, 6, 18))],      # Gasas estériles
    "SKU001": [(datetime(2024, 4, 25), datetime(2024, 5, 12))],     # Aceite almendras antes día de mamá
}

def esta_en_quiebre(sku, fecha):
    for inicio, fin in QUIEBRES_PROGRAMADOS.get(sku, []):
        if inicio <= fecha <= fin:
            return True
    return False

ventas_rows = []

# Patrones de frecuencia de compra por segmento
freq_compra = {"A": 3, "B": 8, "C": 18}

cliente_sku_catalogo = {}

for _, cliente in clientes.iterrows():
    n_skus = {"A": random.randint(20, 40), "B": random.randint(8, 20), "C": random.randint(3, 10)}[cliente["segmento"]]

    # Ponderar SKUs por afinidad canal-categoría
    pesos = []
    for _, prod in productos.iterrows():
        aff = canal_sku_affinity(cliente["canal"], prod["categoria"], prod["marca"])
        pesos.append(aff)
    pesos = np.array(pesos)
    pesos = pesos / pesos.sum()

    skus_cliente = np.random.choice(productos["sku"].values, size=min(n_skus, len(productos)), replace=False, p=pesos)
    cliente_sku_catalogo[cliente["cliente_id"]] = skus_cliente

    # Simular churn en Q3 2024
    es_churn = cliente["segmento"] == "B" and random.random() < 0.15
    fecha_churn = datetime(2024, random.randint(7, 10), random.randint(1, 28)) if es_churn else None

    fecha_actual = max(START_DATE, cliente["fecha_alta"])
    if isinstance(fecha_actual, pd.Timestamp):
        fecha_actual = fecha_actual.to_pydatetime()

    while fecha_actual <= END_DATE:
        if fecha_churn and fecha_actual >= fecha_churn:
            break

        dias_siguiente = int(np.random.normal(freq_compra[cliente["segmento"]], freq_compra[cliente["segmento"]] * 0.4))
        dias_siguiente = max(1, dias_siguiente)

        n_skus_pedido = max(1, int(np.random.normal(len(skus_cliente) * 0.45, len(skus_cliente) * 0.2)))
        skus_pedido = random.sample(list(skus_cliente), min(n_skus_pedido, len(skus_cliente)))

        canal_pedido = random.choices(
            ["Representante", "E-commerce", "EDI", "WhatsApp", "Teléfono"],
            weights=[0.35, 0.25, 0.20, 0.12, 0.08]
        )[0]

        for sku in skus_pedido:
            if esta_en_quiebre(sku, fecha_actual):
                continue

            prod = productos[productos["sku"] == sku].iloc[0]
            factor_est = estacionalidad_factor(fecha_actual, prod["temporalidad"])

            vol_base = {"A": random.randint(10, 80), "B": random.randint(3, 25), "C": random.randint(1, 8)}[cliente["segmento"]]
            cantidad_cajas = max(1, int(vol_base * factor_est * np.random.normal(1.0, 0.25)))

            desc_max = {"A": 0.12, "B": 0.07, "C": 0.03}[cliente["segmento"]]
            descuento_pct = round(random.uniform(0, desc_max), 3)

            precio_neto = round(prod["precio_lista_mxn"] * (1 - descuento_pct), 2)
            monto_total = round(precio_neto * cantidad_cajas, 2)
            costo_total  = round(prod["costo_mxn"] * cantidad_cajas, 2)
            margen_mxn   = round(monto_total - costo_total, 2)

            ventas_rows.append({
                "fecha":           fecha_actual.strftime("%Y-%m-%d"),
                "cliente_id":      cliente["cliente_id"],
                "sku":             sku,
                "canal_pedido":    canal_pedido,
                "region":          cliente["region"],
                "ejecutivo":       cliente["ejecutivo"],
                "cantidad_cajas":  cantidad_cajas,
                "precio_lista":    prod["precio_lista_mxn"],
                "descuento_pct":   round(descuento_pct * 100, 1),
                "precio_neto":     precio_neto,
                "monto_total_mxn": monto_total,
                "costo_total_mxn": costo_total,
                "margen_bruto_mxn":margen_mxn,
                "margen_pct":      round((margen_mxn / monto_total * 100) if monto_total > 0 else 0, 1),
            })

        fecha_actual += timedelta(days=dias_siguiente)

ventas = pd.DataFrame(ventas_rows)
ventas["fecha"] = pd.to_datetime(ventas["fecha"])
ventas = ventas.sort_values("fecha").reset_index(drop=True)
ventas["venta_id"] = [f"VTA{i+1:06d}" for i in range(len(ventas))]
ventas.to_csv(f"{OUTPUT_DIR}/ventas.csv", index=False)
print(f"  ✅ {len(ventas):,} registros de ventas generados")
print(f"     Período: {ventas['fecha'].min().date()} → {ventas['fecha'].max().date()}")
print(f"     Venta total: ${ventas['monto_total_mxn'].sum():,.0f} MXN")
print(f"     Margen total: ${ventas['margen_bruto_mxn'].sum():,.0f} MXN")


# ─────────────────────────────────────────────
# 4. INVENTARIO (snapshots semanales)
# ─────────────────────────────────────────────
print("\n📦 Generando inventario semanal...")

semanas = pd.date_range(START_DATE, END_DATE, freq="W-MON")
inventario_rows = []

demanda_semanal = ventas.copy()
demanda_semanal["semana"] = pd.to_datetime(demanda_semanal["fecha"]).dt.to_period("W").apply(lambda r: r.start_time)
demanda_sku_semana = demanda_semanal.groupby(["semana", "sku"])["cantidad_cajas"].sum().reset_index()

for _, prod in productos.iterrows():
    sku = prod["sku"]
    stock_actual = random.randint(200, 800)

    for semana in semanas:
        dem = demanda_sku_semana[(demanda_sku_semana["semana"] == semana) & (demanda_sku_semana["sku"] == sku)]
        demanda = dem["cantidad_cajas"].sum() if len(dem) > 0 else 0

        punto_reorden = demanda * 3 if demanda > 0 else 50
        reabasto = 0
        if stock_actual < punto_reorden:
            reabasto = int(demanda * random.uniform(4, 8))
            stock_actual += reabasto

        quiebre = esta_en_quiebre(sku, semana.to_pydatetime()) and prod["rotacion_esperada"] == "alta"
        if quiebre:
            stock_actual = random.randint(0, 5)

        stock_post = max(0, stock_actual - demanda)
        dias_inv = round(stock_post / (demanda / 7 + 0.001), 1) if demanda > 0 else 999.0
        dias_inv = min(dias_inv, 365)

        merma = max(0, int(stock_post * random.uniform(0, 0.015)))

        inventario_rows.append({
            "semana":           semana.strftime("%Y-%m-%d"),
            "sku":              sku,
            "stock_cajas":      int(stock_post),
            "demanda_semana":   int(demanda),
            "reabasto_cajas":   int(reabasto),
            "dias_inventario":  dias_inv,
            "quiebre_stock":    1 if (stock_post == 0 and demanda > 0) or quiebre else 0,
            "merma_cajas":      merma,
            "punto_reorden":    int(punto_reorden),
        })

        stock_actual = stock_post - merma

inventario = pd.DataFrame(inventario_rows)
n_quiebres = inventario["quiebre_stock"].sum()
inventario.to_csv(f"{OUTPUT_DIR}/inventario.csv", index=False)
print(f"  ✅ {len(inventario):,} registros de inventario generados")
print(f"     Quiebres de stock detectados: {n_quiebres} semana-SKU")


# ─────────────────────────────────────────────
# 5. PEDIDOS DE COMPRA A PROVEEDORES
# ─────────────────────────────────────────────
print("\n🛒 Generando pedidos de compra...")

proveedores_por_marca = {
    "Jaloma":           "PROV001 - Laboratorios Jaloma SA de CV",
    "Jaloma Belleza":   "PROV001 - Laboratorios Jaloma SA de CV",
    "Jaloma Curación":  "PROV002 - División Material de Curación Jaloma",
    "Jaloma Bebé":      "PROV003 - Línea Infantil Jaloma",
    "Plásticos Jaloma": "PROV004 - Plásticos Jaloma SA de CV",
}

lead_times = {
    "PROV001 - Laboratorios Jaloma SA de CV":       (5, 10),
    "PROV002 - División Material de Curación Jaloma":(7, 14),
    "PROV003 - Línea Infantil Jaloma":              (5, 10),
    "PROV004 - Plásticos Jaloma SA de CV":          (3, 7),
}

compras_rows = []
for row in inventario_rows:
    if row["reabasto_cajas"] > 0:
        prod = productos[productos["sku"] == row["sku"]]
        if len(prod) == 0:
            continue
        prod = prod.iloc[0]
        proveedor = proveedores_por_marca.get(prod["marca"], "PROV005 - Proveedor Materia Prima Externo")
        lt_min, lt_max = lead_times.get(proveedor, (10, 20))
        lead_time = random.randint(lt_min, lt_max)
        fecha_pedido = datetime.strptime(row["semana"], "%Y-%m-%d") - timedelta(days=lead_time)

        factor_costo = np.random.normal(1.0, 0.04)
        costo_real = round(prod["costo_mxn"] * factor_costo, 2)

        compras_rows.append({
            "oc_id":            f"OC{len(compras_rows)+1:05d}",
            "fecha_pedido":     fecha_pedido.strftime("%Y-%m-%d"),
            "fecha_recepcion_esperada": row["semana"],
            "proveedor":        proveedor,
            "sku":              row["sku"],
            "marca":            prod["marca"],
            "cantidad_cajas":   row["reabasto_cajas"],
            "costo_unitario":   costo_real,
            "monto_total_mxn":  round(costo_real * row["reabasto_cajas"], 2),
            "lead_time_dias":   lead_time,
            "condicion_pago":   random.choice(["30 días", "45 días", "60 días", "Contado"]),
            "recibido":         1 if datetime.strptime(row["semana"], "%Y-%m-%d") <= END_DATE else 0,
        })

compras = pd.DataFrame(compras_rows)
compras.to_csv(f"{OUTPUT_DIR}/pedidos_compra.csv", index=False)
print(f"  ✅ {len(compras):,} órdenes de compra generadas")


# ─────────────────────────────────────────────
# 6. VENTAS PERDIDAS
# ─────────────────────────────────────────────
print("\n💸 Calculando ventas perdidas por quiebre de stock...")

perdidas_rows = []
for sku, periodos in QUIEBRES_PROGRAMADOS.items():
    prod = productos[productos["sku"] == sku].iloc[0]
    for inicio, fin in periodos:
        dias_quiebre = (fin - inicio).days
        ventas_sku = ventas[ventas["sku"] == sku]
        demanda_diaria_prom = ventas_sku["cantidad_cajas"].sum() / max(1, len(ventas_sku["fecha"].dt.date.unique()))

        factor = estacionalidad_factor(inicio, prod["temporalidad"])

        cajas_perdidas = int(demanda_diaria_prom * dias_quiebre * factor * 1.2)
        venta_perdida = round(cajas_perdidas * prod["precio_lista_mxn"] * 0.92, 2)
        margen_perdido = round(cajas_perdidas * (prod["precio_lista_mxn"] - prod["costo_mxn"]) * 0.92, 2)

        perdidas_rows.append({
            "sku":              sku,
            "nombre":           prod["nombre"],
            "marca":            prod["marca"],
            "quiebre_inicio":   inicio.strftime("%Y-%m-%d"),
            "quiebre_fin":      fin.strftime("%Y-%m-%d"),
            "dias_sin_stock":   dias_quiebre,
            "cajas_perdidas_estimadas": cajas_perdidas,
            "venta_perdida_mxn":venta_perdida,
            "margen_perdido_mxn":margen_perdido,
            "temporada":        "Gripe/Respiratoria" if inicio.month in [10,11,12,1,2] else "Día de las Madres" if inicio.month == 5 else "Regular",
        })

perdidas = pd.DataFrame(perdidas_rows)
perdidas.to_csv(f"{OUTPUT_DIR}/ventas_perdidas.csv", index=False)

total_venta_perdida = perdidas["venta_perdida_mxn"].sum()
total_margen_perdido = perdidas["margen_perdido_mxn"].sum()

print(f"  ✅ {len(perdidas)} episodios de quiebre documentados")
print(f"     💀 Venta perdida total estimada: ${total_venta_perdida:,.0f} MXN")
print(f"     💀 Margen perdido total:         ${total_margen_perdido:,.0f} MXN")


# ─────────────────────────────────────────────
# 7. RESUMEN EJECUTIVO
# ─────────────────────────────────────────────
print("\n📊 Calculando KPIs ejecutivos...")

rent_cliente = ventas.merge(clientes[["cliente_id","nombre","canal","segmento"]], on="cliente_id")
rent_cliente_agg = rent_cliente.groupby(["cliente_id","nombre","canal","segmento"]).agg(
    venta_total_mxn=("monto_total_mxn", "sum"),
    margen_total_mxn=("margen_bruto_mxn", "sum"),
    pedidos=("venta_id", "nunique"),
    skus_distintos=("sku", "nunique"),
    descuento_promedio=("descuento_pct", "mean"),
).reset_index()
rent_cliente_agg["margen_pct_real"] = (rent_cliente_agg["margen_total_mxn"] / rent_cliente_agg["venta_total_mxn"] * 100).round(1)
rent_cliente_agg["ticket_promedio"] = (rent_cliente_agg["venta_total_mxn"] / rent_cliente_agg["pedidos"]).round(0)
rent_cliente_agg = rent_cliente_agg.sort_values("venta_total_mxn", ascending=False)
rent_cliente_agg.to_csv(f"{OUTPUT_DIR}/rentabilidad_clientes.csv", index=False)

# Análisis ABC de SKUs
abc_sku = ventas.groupby("sku").agg(
    venta_total_mxn=("monto_total_mxn", "sum"),
    margen_total_mxn=("margen_bruto_mxn", "sum"),
    cajas_vendidas=("cantidad_cajas", "sum"),
).reset_index()
abc_sku = abc_sku.sort_values("margen_total_mxn", ascending=False)
abc_sku["margen_acumulado_pct"] = (abc_sku["margen_total_mxn"].cumsum() / abc_sku["margen_total_mxn"].sum() * 100).round(1)
abc_sku["clasificacion_abc"] = abc_sku["margen_acumulado_pct"].apply(
    lambda x: "A" if x <= 80 else ("B" if x <= 95 else "C")
)
abc_sku = abc_sku.merge(productos[["sku","nombre","marca","categoria"]], on="sku")
abc_sku.to_csv(f"{OUTPUT_DIR}/analisis_abc_skus.csv", index=False)

# ─────────────────────────────────────────────
# RESUMEN FINAL
# ─────────────────────────────────────────────
print("\n" + "="*60)
print("🎯 RESUMEN DE DATOS GENERADOS — GRUPO JALOMA POC")
print("="*60)
print(f"\n  Clientes:          {len(clientes):>8,}")
print(f"  SKUs en catálogo:  {len(productos):>8,}")
print(f"  Registros ventas:  {len(ventas):>8,}")
print(f"  Registros inv.:    {len(inventario):>8,}")
print(f"  Órdenes de compra: {len(compras):>8,}")
print(f"\n  📈 Venta total 2023-2024:   ${ventas['monto_total_mxn'].sum():>15,.0f} MXN")
print(f"  📈 Margen total:             ${ventas['margen_bruto_mxn'].sum():>15,.0f} MXN")
print(f"  💀 Venta perdida estimada:  ${total_venta_perdida:>15,.0f} MXN")
print(f"  💀 Margen perdido:          ${total_margen_perdido:>15,.0f} MXN")

pct_perdido = total_venta_perdida / (ventas['monto_total_mxn'].sum() + total_venta_perdida) * 100
print(f"\n  ⚠️  La empresa perdió aprox. el {pct_perdido:.1f}% de su venta potencial")
print(f"      por quiebres de stock en productos clave.")
print(f"\n  Top 5 clientes por VOLUMEN vs MARGEN:")

top5 = rent_cliente_agg.head(5)[["nombre","canal","venta_total_mxn","margen_pct_real","descuento_promedio"]]
for _, r in top5.iterrows():
    print(f"    {r['nombre'][:30]:<30} | Venta: ${r['venta_total_mxn']:>10,.0f} | Margen: {r['margen_pct_real']:>5.1f}% | Desc: {r['descuento_promedio']:>4.1f}%")

skus_a = abc_sku[abc_sku["clasificacion_abc"] == "A"]
skus_c = abc_sku[abc_sku["clasificacion_abc"] == "C"]
print(f"\n  📦 Análisis ABC:")
print(f"    SKUs clase A: {len(skus_a)} ({len(skus_a)/len(abc_sku)*100:.0f}% de SKUs → 80% del margen)")
print(f"    SKUs clase C: {len(skus_c)} ({len(skus_c)/len(abc_sku)*100:.0f}% de SKUs → 5% del margen)")

print(f"\n✅ Todos los archivos guardados en: {OUTPUT_DIR}/")
print("="*60)
