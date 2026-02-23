"""
pages/5_🤖_Chat_IA.py
Asistente de IA entrenado con los datos de Grupo Jaloma
"""

import streamlit as st
import pandas as pd
import json
import sys
import os
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))
from utils.data_loader import load_all, get_kpis, get_alertas
from utils.ui import inject_css, page_header, fmt_mxn

st.set_page_config(page_title="Chat IA | Grupo Jaloma", page_icon="🤖", layout="wide")
inject_css()

page_header(
    "🤖 Asistente IA — Pregunta sobre tu Negocio",
    "IA entrenada con los datos de Grupo Jaloma. Haz preguntas en lenguaje natural."
)

ventas, clientes, productos, inventario, compras, rent_cli, abc_skus, perdidas = load_all()
kpis    = get_kpis()
alertas = get_alertas()

def build_context() -> str:
    top10 = rent_cli.head(10)[["nombre","canal","segmento","venta_total_mxn","margen_pct_real","descuento_promedio"]].copy()
    top10.loc[:, "venta_total_mxn"] = top10["venta_total_mxn"].round(0)
    top10.loc[:, "margen_pct_real"] = top10["margen_pct_real"].round(1)
    top10.loc[:, "descuento_promedio"] = top10["descuento_promedio"].round(1)

    margen_canal = rent_cli.copy()
    margen_canal_agg = margen_canal.groupby("canal").agg(
        venta=("venta_total_mxn","sum"), margen_pct=("margen_pct_real","mean"),
    ).round(1).reset_index()

    abc_res = abc_skus.groupby("clasificacion_abc").agg(
        n_skus=("sku","count"), margen_sum=("margen_total_mxn","sum"),
    ).reset_index()

    churn = alertas["churn"]
    quiebre = alertas["quiebre"]

    ctx = f"""
Eres el asistente de inteligencia de negocios de GRUPO JALOMA, empresa 100% mexicana con más de 80 años
dedicada a la fabricación y distribución de productos de Cuidado Personal, Material de Curación,
Productos para Bebé e Industria Farmacéutica. Cuenta con 3 divisiones: Laboratorios Jaloma,
Plásticos Jaloma y Distribuidora Jaloma. Presencia en México, Centroamérica, USA y Canadá.

=== DATOS CLAVE DE GRUPO JALOMA ===

RESUMEN EJECUTIVO (2023-2024):
- Venta total: {fmt_mxn(kpis['venta_total'])}
- Margen bruto total: {fmt_mxn(kpis['margen_total'])} ({kpis['margen_pct']:.1f}%)
- Venta perdida por quiebres de stock: {fmt_mxn(kpis['venta_perdida'])}
- Margen perdido: {fmt_mxn(kpis['margen_perdido'])}
- Clientes activos: {len(clientes)}
- SKUs en catálogo: {len(productos)}
- Marcas: Jaloma, Jaloma Belleza, Jaloma Curación, Jaloma Bebé, Plásticos Jaloma

CATEGORÍAS DE PRODUCTO:
{productos.groupby("marca")["categoria"].apply(lambda x: ", ".join(x.unique())).to_string()}

TOP 10 CLIENTES POR VOLUMEN:
{top10.to_string(index=False)}

MARGEN REAL POR CANAL:
{margen_canal_agg.to_string(index=False)}

ANÁLISIS ABC DE SKUs:
{abc_res.to_string(index=False)}
- Clase A: {kpis['skus_a']} SKUs → 80% del margen
- Clase C: {kpis['skus_total'] - kpis['skus_a']} SKUs → ~5% del margen

CLIENTES EN RIESGO DE CHURN (18+ días sin comprar):
{churn[['nombre','canal','dias_sin_compra','segmento']].to_string(index=False) if len(churn) > 0 else 'Ninguno detectado'}

QUIEBRES DE STOCK DETECTADOS:
{quiebre[['sku','stock_cajas','dias_inventario','venta_en_riesgo']].to_string(index=False) if len(quiebre) > 0 else 'Sin quiebres inminentes'}

EPISODIOS HISTÓRICOS DE QUIEBRE:
{perdidas[['nombre','temporada','dias_sin_stock','venta_perdida_mxn','margen_perdido_mxn']].to_string(index=False)}

INSIGHT CLAVE — PARADOJA DE RENTABILIDAD:
Los canales Institucional y Autoservicio negocian los descuentos más altos.
Los canales Farmacia y E-commerce mantienen los mejores márgenes.
Los quiebres se concentran en temporada de gripe/respiratoria (Oct-Feb) y Día de las Madres.

INSTRUCCIONES:
- Responde siempre con datos específicos de Grupo Jaloma
- Sé directo y ejecutivo — hablas con la dirección general
- Cuando detectes un problema, ofrece una recomendación accionable
- Usa formato claro con números concretos en MXN
- Responde en español
"""
    return ctx

SYSTEM_CONTEXT = build_context()

PREGUNTAS_SUGERIDAS = [
    "¿Cuál es mi cliente más rentable?",
    "¿Qué SKUs debo priorizar en inventario?",
    "¿Cuánto dinero perdí por quiebres de stock?",
    "¿Qué clientes están en riesgo de irse?",
    "¿Dónde está la mayor oportunidad de mejora de margen?",
    "¿Qué canal debería priorizar para crecer?",
    "¿Cuáles son mis SKUs clase C que debería revisar?",
    "Dame un resumen ejecutivo del negocio",
    "¿Cómo se comportan las ventas en temporada de gripe?",
    "¿Cómo se comparan los ejecutivos de cuenta?",
]

if "messages" not in st.session_state:
    st.session_state.messages = []
    st.session_state.messages.append({
        "role": "assistant",
        "content": f"""¡Hola! Soy el asistente de inteligencia de negocios de **Grupo Jaloma**.

Tengo acceso completo a los datos de ventas 2023-2024:
- **{len(ventas):,}** registros de transacciones
- **{len(clientes)}** clientes en **7 canales** (Farmacia, Autoservicio, Conveniencia, Mayorista, Institucional, Exportación, E-commerce)
- **{len(productos)}** SKUs de **5 líneas** (Jaloma, Jaloma Belleza, Jaloma Curación, Jaloma Bebé, Plásticos Jaloma)

Algunos hallazgos que ya detecté y puedes explorar:

🔴 **{fmt_mxn(kpis['venta_perdida'])}** en ventas perdidas por quiebres de stock en temporada respiratoria

🟡 Los canales **Autoservicio** e **Institucional** tienen el margen más erosionado por descuentos comerciales

🟣 **{len(alertas['churn'])} clientes** llevan más de 18 días sin comprar

¿Qué quieres analizar?"""
    })

with st.sidebar:
    st.markdown("### 💊 Grupo Jaloma BI + IA")
    st.markdown("---")
    st.markdown("**Configuración del Chat**")
    api_key = os.environ.get("ANTHROPIC_API_KEY", "")
    if not api_key:
        api_key = st.text_input("Anthropic API Key", type="password", placeholder="sk-ant-...",
            help="Requerida para el chat con IA. Obtén una en console.anthropic.com")
    else:
        st.success("✅ API Key cargada desde .env")
    st.markdown("---")
    st.markdown("**Preguntas sugeridas:**")
    for preg in PREGUNTAS_SUGERIDAS[:6]:
        if st.button(preg, use_container_width=True, key=f"sug_{preg[:20]}"):
            st.session_state.pending_question = preg
    st.markdown("---")
    if st.button("🗑️ Limpiar conversación"):
        st.session_state.messages = []
        st.rerun()

for msg in st.session_state.messages:
    with st.chat_message(msg["role"], avatar="💊" if msg["role"] == "assistant" else "👤"):
        st.markdown(msg["content"])

pregunta = st.chat_input("Pregunta sobre el negocio de Grupo Jaloma...")

if "pending_question" in st.session_state:
    pregunta = st.session_state.pending_question
    del st.session_state.pending_question


def _demo_response(pregunta: str, kpis, rent_cli, abc_skus, perdidas, alertas) -> str:
    p = pregunta.lower()

    TOPICS = {
        "rentabilidad":   ["rentable", "rentabilidad", "margen", "mejor cliente", "ganancia", "utilidad"],
        "inventario":     ["quiebre", "perdid", "stock", "inventario", "faltante", "desabasto"],
        "churn":          ["churn", "sin comprar", "perdiendo cliente", "abandono", "inactiv", "retención", "irse"],
        "abc":            ["sku", "producto", "abc", "priorizar", "catálogo", "catalogo", "clase"],
        "resumen":        ["resumen", "general", "negocio", "panorama", "dashboard"],
        "estacionalidad": ["estacional", "temporad", "gripe", "invierno", "variable", "patrón", "patron", "ciclo"],
        "canales":        ["canal", "farmacia", "autoservicio", "conveniencia", "descuento", "mayorista", "institucional", "exportación"],
        "ejecutivos":     ["ejecutivo", "vendedor", "cuenta", "equipo comercial", "fuerza de venta"],
        "oportunidad":    ["oportunidad", "mejora", "crecer", "crecimiento", "optimizar", "estrategia", "recomendación"],
    }

    matched = []
    for topic, keywords in TOPICS.items():
        if any(w in p for w in keywords):
            matched.append(topic)
    if len(matched) > 1 and "resumen" in matched:
        matched.remove("resumen")

    def _resp_rentabilidad():
        top = rent_cli.sort_values("margen_total_mxn", ascending=False).head(5)
        bottom = rent_cli.sort_values("margen_pct_real").head(3)
        r = "### 💰 Análisis de Rentabilidad\n\n**Top 5 clientes por margen total:**\n\n"
        for _, row in top.iterrows():
            r += f"- **{row['nombre']}** · {row['canal']} · Margen: {row['margen_pct_real']:.1f}% · {fmt_mxn(row['margen_total_mxn'])}\n"
        r += "\n**Clientes con margen más débil (alerta):**\n\n"
        for _, row in bottom.iterrows():
            r += f"- ⚠️ **{row['nombre']}** · {row['canal']} · Margen: {row['margen_pct_real']:.1f}% · Desc: {row['descuento_promedio']:.1f}%\n"
        mc = rent_cli.groupby("canal")["margen_pct_real"].mean().sort_values()
        gap = mc.iloc[-1] - mc.iloc[0]
        r += f"\n💡 **Insight:** El canal **{mc.index[-1]}** supera a **{mc.index[0]}** por **{gap:.1f} pts** de margen."
        return r

    def _resp_inventario():
        total = perdidas["venta_perdida_mxn"].sum()
        total_m = perdidas["margen_perdido_mxn"].sum()
        r = f"### 📦 Quiebres de Stock\n\n**Impacto total:** {fmt_mxn(total)} venta perdida · {fmt_mxn(total_m)} margen perdido\n\n"
        for _, row in perdidas.iterrows():
            r += f"- **{row['nombre']}** · Temporada {row['temporada']} · {row['dias_sin_stock']} días sin stock · Perdido: {fmt_mxn(row['venta_perdida_mxn'])}\n"
        r += "\n⚠️ Los quiebres ocurren en temporada de gripe/respiratoria y Día de las Madres, amplificando el impacto."
        r += f"\n\n🎯 **Acción:** Buffer de seguridad estacional 3-4 semanas antes para los {len(perdidas)} SKUs afectados."
        return r

    def _resp_churn():
        churn = alertas["churn"]
        churn_valor = alertas["churn_valor"]
        r = f"### 🟣 Clientes en Riesgo de Abandono\n\n**{len(churn)} clientes** con 18+ días sin comprar · Venta en riesgo: **{fmt_mxn(churn_valor)}**\n\n"
        for _, row in churn.iterrows():
            r += f"- **{row['nombre']}** · {row.get('canal','')} · Seg. {row.get('segmento','—')} · **{row['dias_sin_compra']} días**\n"
        r += "\n🎯 **Acción inmediata:** Contacto del ejecutivo en 48h con oferta de recompra personalizada."
        return r

    def _resp_abc():
        sa = abc_skus[abc_skus["clasificacion_abc"] == "A"]
        sb = abc_skus[abc_skus["clasificacion_abc"] == "B"]
        sc = abc_skus[abc_skus["clasificacion_abc"] == "C"]
        r = f"### 📊 Análisis ABC ({len(abc_skus)} SKUs)\n\n"
        r += f"🟢 **Clase A ({len(sa)}):** 80% del margen — disponibilidad permanente\n"
        r += f"🟡 **Clase B ({len(sb)}):** 15% del margen — stock mínimo calculado\n"
        r += f"🔴 **Clase C ({len(sc)}):** 5% del margen — evaluar descontinuación\n\n**Top 5 SKUs Clase A:**\n\n"
        for _, row in sa.head(5).iterrows():
            r += f"- **{row['nombre']}** · Margen: {fmt_mxn(row['margen_total_mxn'])} · Venta: {fmt_mxn(row['venta_total_mxn'])}\n"
        return r

    def _resp_resumen():
        return f"""### 📈 Resumen Ejecutivo — Grupo Jaloma 2023-2024

**Venta:** {fmt_mxn(kpis['venta_total'])} · **Margen:** {kpis['margen_pct']:.1f}% · **Margen $:** {fmt_mxn(kpis['margen_total'])}

**3 hallazgos críticos:**

🔴 **{fmt_mxn(kpis['venta_perdida'])} en venta perdida** por quiebres en temporada respiratoria y Día de las Madres.

🟡 **Paradoja de canal:** Los canales con mayor volumen (Autoservicio, Institucional) tienen el margen más erosionado por descuentos.

🟣 **{len(alertas['churn'])} clientes** con señal de abandono — {fmt_mxn(alertas['churn_valor'])} en venta anual en riesgo."""

    def _resp_estacionalidad():
        r = "### 🌡️ Estacionalidad y Temporada Respiratoria\n\n"
        r += "Los quiebres de Grupo Jaloma se concentran en dos temporadas:\n\n"
        r += "**1. Temporada de gripe/respiratoria (Oct-Feb):** Demanda de gel antibacterial, cubrebocas, alcohol y jeringas sube +80%. Los quiebres aquí son los más costosos.\n\n"
        r += "**2. Día de las Madres (Mayo):** Pico de demanda en aceites cosméticos, línea Jaloma Belleza.\n\n"
        r += "**Variables externas para integrar:**\n"
        r += "- 📅 Calendario de campañas de vacunación (IMSS/ISSSTE)\n"
        r += "- 🌧️ Índice de infecciones respiratorias por región\n"
        r += "- 💰 Calendario promocional de cadenas (Walmart, Farmacias GDL)\n"
        r += "- 📊 Precios de competencia (Genomma Lab, Medimart)\n\n"
        r += "🎯 **Recomendación:** Integrar calendario de salud pública + promos de clientes. Proyección: reducir quiebres 40-60%."
        return r

    def _resp_canales():
        mc = rent_cli.groupby("canal").agg(
            venta=("venta_total_mxn", "sum"), margen_pct=("margen_pct_real", "mean"),
            descuento=("descuento_promedio", "mean"), n=("cliente_id", "nunique"),
        ).sort_values("margen_pct", ascending=False).reset_index()
        r = "### 📊 Comparativa por Canal\n\n| Canal | Venta | Margen % | Desc. % | Clientes |\n|-------|-------|----------|---------|----------|\n"
        for _, row in mc.iterrows():
            r += f"| {row['canal']} | {fmt_mxn(row['venta'])} | {row['margen_pct']:.1f}% | {row['descuento']:.1f}% | {row['n']} |\n"
        mejor = mc.iloc[0]
        peor = mc.iloc[-1]
        r += f"\n🏆 **Más rentable:** {mejor['canal']} ({mejor['margen_pct']:.1f}%)\n"
        r += f"⚠️ **Menos rentable:** {peor['canal']} ({peor['margen_pct']:.1f}%)\n"
        return r

    def _resp_ejecutivos():
        ejec = rent_cli.merge(clientes[["cliente_id", "ejecutivo"]], on="cliente_id").groupby("ejecutivo").agg(
            venta=("venta_total_mxn", "sum"), margen=("margen_total_mxn", "sum"),
            margen_pct=("margen_pct_real", "mean"), n=("cliente_id", "nunique"), desc=("descuento_promedio", "mean"),
        ).sort_values("margen", ascending=False).reset_index()
        r = "### 👤 Rendimiento por Ejecutivo\n\n| Ejecutivo | Venta | Margen $ | Margen % | Desc. % | Clientes |\n|-----------|-------|----------|----------|---------|----------|\n"
        for _, row in ejec.iterrows():
            r += f"| {row['ejecutivo']} | {fmt_mxn(row['venta'])} | {fmt_mxn(row['margen'])} | {row['margen_pct']:.1f}% | {row['desc']:.1f}% | {row['n']} |\n"
        r += "\n💡 Los ejecutivos con mayor volumen no siempre generan mayor margen."
        return r

    def _resp_oportunidad():
        total_op = kpis["venta_perdida"] + alertas["margen"]["impacto"] + alertas["churn_valor"]
        r = f"### 🎯 Mapa de Oportunidades — Priorizado por Impacto\n\n**Oportunidad total: {fmt_mxn(total_op)}**\n\n"
        r += f"**1. Eliminar quiebres de stock** → {fmt_mxn(kpis['venta_perdida'])}\n"
        r += f"**2. Optimizar descuentos comerciales** → {fmt_mxn(alertas['margen']['impacto'])}\n"
        r += f"**3. Retener clientes en riesgo** → {fmt_mxn(alertas['churn_valor'])}\n\n"
        r += "📌 **Ninguna requiere nuevos clientes** — son eficiencias operativas con la base actual."
        return r

    GEN = {"rentabilidad": _resp_rentabilidad, "inventario": _resp_inventario, "churn": _resp_churn,
           "abc": _resp_abc, "resumen": _resp_resumen, "estacionalidad": _resp_estacionalidad,
           "canales": _resp_canales, "ejecutivos": _resp_ejecutivos, "oportunidad": _resp_oportunidad}

    if not matched:
        mc = rent_cli.groupby("canal")["margen_pct_real"].mean()
        gap = mc.max() - mc.min()
        return f"""Analicé tu pregunta: *"{pregunta}"*

Con base en los datos de Grupo Jaloma (2023-2024):

📈 **Ventas:** {fmt_mxn(kpis['venta_total'])} · Margen: {kpis['margen_pct']:.1f}%
📦 **Quiebres:** {fmt_mxn(kpis['venta_perdida'])} en venta perdida
💰 **Canales:** {rent_cli['canal'].nunique()} canales con hasta {gap:.1f} pts de diferencia en margen
🟣 **Churn:** {len(alertas['churn'])} clientes con señales de abandono

¿Sobre cuál quieres profundizar?"""

    parts = [GEN[t]() for t in matched[:3] if t in GEN]
    return "\n\n---\n\n".join(parts)


if pregunta:
    st.session_state.messages.append({"role": "user", "content": pregunta})
    with st.chat_message("user", avatar="👤"):
        st.markdown(pregunta)

    with st.chat_message("assistant", avatar="💊"):
        if not api_key:
            respuesta = _demo_response(pregunta, kpis, rent_cli, abc_skus, perdidas, alertas)
            st.markdown(respuesta)
        else:
            try:
                import anthropic
                client = anthropic.Anthropic(api_key=api_key)
                messages_api = [{"role": m["role"], "content": m["content"]}
                    for m in st.session_state.messages if m["role"] in ["user", "assistant"]]
                with st.spinner("Analizando datos..."):
                    response = client.messages.create(model="claude-sonnet-4-20250514",
                        max_tokens=1000, system=SYSTEM_CONTEXT, messages=messages_api)
                    respuesta = response.content[0].text
                st.markdown(respuesta)
            except ImportError:
                st.error("Instala anthropic: `pip install anthropic`")
                respuesta = "Error: librería anthropic no instalada."
            except Exception as e:
                respuesta = _demo_response(pregunta, kpis, rent_cli, abc_skus, perdidas, alertas)
                st.markdown(respuesta)
                st.caption(f"ℹ️ Modo demo (sin API): {str(e)[:80]}")

        st.session_state.messages.append({"role": "assistant", "content": respuesta})