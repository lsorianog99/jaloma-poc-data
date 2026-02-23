# 💊 Grupo Jaloma BI + IA — Proof of Concept

> **De la intuición a los datos** — Demo interactiva de Business Intelligence + Inteligencia Artificial para Grupo Jaloma

## 🎯 ¿Qué es esto?

Una plataforma de BI + IA diseñada para **Grupo Jaloma**, empresa 100% mexicana con más de 80 años dedicada a la fabricación y distribución de productos de **Cuidado Personal**, **Material de Curación**, **Productos para Bebé** e **Industria Farmacéutica**.

La PoC demuestra cómo la inteligencia artificial puede transformar los datos operativos de Jaloma en **decisiones accionables** que impactan directamente la rentabilidad.

## 📊 Módulos

| Módulo | Descripción |
|--------|-------------|
| 🏠 **Resumen Ejecutivo** | KPIs consolidados, venta por canal, top clientes |
| 🚨 **Alertas IA** | 3 alertas críticas: quiebres de stock, margen erosionado, churn |
| 💰 **Rentabilidad** | Análisis de margen real por cliente, canal y ejecutivo |
| 📦 **Inventario** | Quiebres, ventas perdidas, clasificación ABC de SKUs |
| 🔮 **Forecast IA** | Predicción de demanda por SKU — próximas 8 semanas |
| 🤖 **Chat IA** | Asistente conversacional entrenado con datos de Grupo Jaloma |

## 🚀 Instalación

```bash
# Clonar repositorio
git clone https://github.com/KAIROS-BT/jaloma-poc-data.git
cd jaloma-poc-data

# Crear entorno virtual
python -m venv venv
source venv/bin/activate  # macOS/Linux

# Instalar dependencias
pip install -r requirements.txt

# (Opcional) Configurar API Key para Chat IA con Claude
echo "ANTHROPIC_API_KEY=sk-ant-..." > .env

# Ejecutar
streamlit run app.py
```

## 📁 Estructura

```
jaloma-poc/
├── app.py                            # Dashboard principal
├── jaloma-logo-2x.png                # Logo corporativo
├── requirements.txt                  # Dependencias
├── pages/
│   ├── 1_🚨_Alertas_IA.py           # Alertas inteligentes
│   ├── 2_💰_Rentabilidad.py          # Análisis de rentabilidad
│   ├── 3_📦_Inventario.py            # Inventario y quiebres
│   ├── 4_🔮_Forecast_IA.py           # Predicción de demanda
│   └── 5_🤖_Chat_IA.py              # Asistente IA conversacional
├── utils/
│   ├── data_loader.py                # Carga y procesamiento de datos
│   └── ui.py                         # Componentes visuales (paleta roja Jaloma)
└── data/
    ├── generate_data.py              # Generador de datos sintéticos
    ├── ventas.csv                    # 81,674 transacciones (2023-2024)
    ├── clientes.csv                  # 80 clientes en 7 canales
    ├── productos.csv                 # 58 SKUs del catálogo Jaloma
    ├── inventario.csv                # Snapshots semanales de stock
    ├── pedidos_compra.csv            # Órdenes de compra a proveedores
    ├── rentabilidad_clientes.csv     # Margen real por cliente
    ├── analisis_abc_skus.csv         # Clasificación ABC de SKUs
    └── ventas_perdidas.csv           # Detalle de ventas perdidas por quiebre
```

## 💡 Datos del PoC

Los datos son **sintéticos pero realistas**, basados en el catálogo real de productos de Grupo Jaloma:

### Productos (58 SKUs)
- **Jaloma Belleza:** Aceites cosméticos (almendras, aguacate, argán, coco, ricino, rosa mosqueta), agua de rosas, gel de árnica, gel de pepino con ácido hialurónico, fijadores
- **Jaloma Curación:** Algodón, gasas estériles, vendas, curitas, cinta micropore, alcohol, agua oxigenada, botiquines
- **Jaloma Bebé:** Aceite para bebé, jabón, shampoo, talco, crema para rozaduras, toallitas húmedas
- **Jaloma (Farmacéutico):** Guantes de látex/nitrilo, cubrebocas, jeringas, suero fisiológico, glicerina
- **Plásticos Jaloma:** Envases PET, tapas, dosificadores (intercompañía)

### Clientes (80)
Farmacias Guadalajara, Farmacias del Ahorro, Benavides, Walmart, Soriana, Chedraui, OXXO, 7-Eleven, Grupo Nadro, Casa Marzam, IMSS, ISSSTE, Hospitales Ángeles, Amazon México, distribuidores regionales y exportadores a Centroamérica/USA.

### Canales (7)
Farmacia Cadena · Autoservicio · Conveniencia · Mayorista · Institucional · Exportación · E-commerce

## 🔑 Hallazgos Clave de la IA

> *"Se perdieron $10M MXN en ventas por quiebres de stock durante temporada de gripe — exactamente cuando la demanda era más alta."*

> *"Los canales de mayor volumen (Autoservicio, Institucional) tienen el margen más erosionado por descuentos. Farmacia y E-commerce son significativamente más rentables."*

> *"Solo 35 de 58 SKUs generan el 80% del margen. El resto inmoviliza capital sin retorno proporcional."*

## 🛠️ Tecnologías

- **Streamlit** — Dashboard interactivo
- **Plotly** — Visualizaciones dinámicas
- **Pandas / NumPy** — Procesamiento de datos
- **scikit-learn** — Modelos predictivos
- **Anthropic Claude** — Chat IA (opcional, funciona en modo demo sin API key)

## 📌 Próximos Pasos (Implementación Real)

- [ ] Conectar a ERP/WMS real de Grupo Jaloma
- [ ] Integrar datos de sell-out por punto de venta
- [ ] Forecast con modelos avanzados (Prophet/ARIMA)
- [ ] Alertas automáticas por email/WhatsApp
- [ ] Dashboard de producción (Laboratorios Jaloma)
- [ ] Análisis intercompañía (Plásticos ↔ Distribuidora)

---

*PoC desarrollada por KAIROS-BT — Transformación Digital para Grupo Jaloma*
