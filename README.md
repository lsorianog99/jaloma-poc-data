# 🌿 Alceda BI + IA — Proof of Concept

> **De la intuición a los datos** — Demo interactiva de Business Intelligence + Inteligencia Artificial para Alceda

---

## 📋 ¿Qué incluye esta PoC?

| Página | Descripción |
|--------|-------------|
| 🏠 **Home** | Resumen ejecutivo con KPIs globales 2023-2024 |
| 🚨 **Alertas IA** | 3 alertas críticas generadas automáticamente por IA (el "wow" de la demo) |
| 💰 **Rentabilidad** | Análisis de margen real por cliente, canal y ejecutivo |
| 📦 **Inventario** | Quiebres históricos, análisis ABC, ventas perdidas cuantificadas |
| 🔮 **Forecast IA** | Predicción de demanda por SKU para las próximas 8 semanas |
| 🤖 **Chat IA** | Asistente conversacional entrenado con datos de Alceda |

---

## ⚡ Instalación Rápida (Mac)

### Prerequisitos
- Python 3.10+ instalado ([python.org](https://www.python.org))
- Terminal (iTerm, Warp, o la nativa de Mac)

### Pasos

```bash
# 1. Navegar a la carpeta del proyecto
cd alceda-poc

# 2. Crear entorno virtual (recomendado)
python3 -m venv venv
source venv/bin/activate

# 3. Instalar dependencias
pip install -r requirements.txt

# 4. Configurar API Key de Anthropic (para el Chat IA)
cp .env.example .env
# Editar .env y pegar tu API Key:
# ANTHROPIC_API_KEY=sk-ant-xxxxxxxxxx

# 5. Lanzar la aplicación
streamlit run app.py
```

La app abrirá automáticamente en: **http://localhost:8501**

---

## 🔑 API Key de Anthropic (opcional pero recomendado)

El Chat IA funciona en **modo demo** sin API Key (respuestas pre-programadas con los datos reales).

Para activar el chat con IA real:
1. Crea una cuenta en [console.anthropic.com](https://console.anthropic.com)
2. Genera una API Key
3. Pégala en el archivo `.env` o directamente en la sidebar del Chat

---

## 📁 Estructura del Proyecto

```
alceda-poc/
├── app.py                          # Home - Resumen Ejecutivo
├── requirements.txt                # Dependencias Python
├── .env.example                    # Template de variables de entorno
├── README.md                       # Este archivo
│
├── pages/
│   ├── 1_🚨_Alertas_IA.py         # Alertas inteligentes (centerpiece)
│   ├── 2_💰_Rentabilidad.py        # Análisis de rentabilidad
│   ├── 3_📦_Inventario.py          # Inventario y quiebres
│   ├── 4_🔮_Forecast_IA.py         # Predicción de demanda
│   └── 5_🤖_Chat_IA.py             # Asistente conversacional
│
├── utils/
│   ├── data_loader.py              # Carga y procesamiento de datos
│   └── ui.py                       # Componentes visuales y CSS
│
└── data/
    ├── generate_data.py            # Script para regenerar datos sintéticos
    ├── ventas.csv                  # 57,351 transacciones (2023-2024)
    ├── clientes.csv                # 80 clientes por segmento y canal
    ├── productos.csv               # 58 SKUs del catálogo Alceda
    ├── inventario.csv              # Snapshots semanales de stock
    ├── pedidos_compra.csv          # Órdenes de compra a proveedores
    ├── rentabilidad_clientes.csv   # KPIs de rentabilidad por cliente
    ├── analisis_abc_skus.csv       # Clasificación ABC del catálogo
    └── ventas_perdidas.csv         # Quiebres y ventas no realizadas
```

---

## 📊 Los Números de la Historia

```
Venta Total 2023-2024:       $2,137,882,465 MXN
Margen Bruto Total:            $766,783,517 MXN  (35.9%)
─────────────────────────────────────────────────
💀 Venta Perdida (quiebres):   $10,784,590 MXN
💀 Margen Perdido:              $4,313,836 MXN

Clientes en Riesgo de Churn:  10 clientes (18+ días sin comprar)
Episodios de Quiebre:          6 (en temporadas de alta demanda)
SKUs Clase A:                  37 SKUs → 80% del margen
```

### El "Momento Wow" para el CEO

> *Los canales de MAYOR volumen (Retail Conveniencia, QSR) tienen el MENOR margen (35-36%).
> Los Dark Kitchens, con 80% menos volumen, generan 38-39% de margen.
> Nadie en Alceda lo sabía — hasta hoy.*

---

## 🔄 Regenerar Datos Sintéticos

Si necesitas datos frescos o modificar parámetros:

```bash
cd data
python generate_data.py
```

---

## 🛠️ Troubleshooting

**Puerto ocupado:**
```bash
streamlit run app.py --server.port 8502
```

**Error de módulo no encontrado:**
```bash
pip install -r requirements.txt --upgrade
```

**Streamlit no abre el navegador:**
Ir manualmente a: http://localhost:8501

---

## 🚀 Roadmap — Próximas Fases

- [ ] Conectar a ERP/Shopify real de Alceda
- [ ] Implementar pipeline de datos con Azure Data Factory
- [ ] Modelo de forecast con Prophet (mayor precisión)
- [ ] Alertas automáticas por WhatsApp / Email
- [ ] Dashboard móvil para ejecutivos de cuenta
- [ ] Integración con sistema de pedidos (generar OCs reales)

---

*PoC desarrollada por [Tu Consultora] — Transformación Digital para Alceda*
