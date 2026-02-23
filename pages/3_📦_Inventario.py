"""
pages/3_📦_Inventario.py
Análisis de inventario, quiebres y abastecimiento
"""

import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))
from utils.data_loader import load_all
from utils.ui import inject_css, page_header, fmt_mxn

st.set_page_config(page_title="Inventario | Grupo Jaloma", page_icon="📦", layout="wide")
inject_css()

ventas, clientes, productos, inventario, compras, rent_cli, abc_skus, perdidas = load_all()

with st.sidebar:
    st.markdown("### 💊 Grupo Jaloma BI + IA")
    st.markdown("---")
    marcas_disp = ["Todas"] + sorted(productos["marca"].unique().tolist())
    filtro_marca = st.selectbox("Marca", marcas_disp)
    cats_disp    = ["Todas"] + sorted(productos["categoria"].unique().tolist())
    filtro_cat   = st.selectbox("Categoría", cats_disp)

page_header("📦 Inventario & Abastecimiento", "Detecta quiebres antes de que ocurran — no después")

inv = inventario.merge(productos[["sku","nombre","marca","categoria","precio_lista_mxn","costo_mxn"]], on="sku")
if filtro_marca != "Todas":
    inv = inv[inv["marca"] == filtro_marca]
if filtro_cat != "Todas":
    inv = inv[inv["categoria"] == filtro_cat]

total_quiebres = inv["quiebre_stock"].sum()
total_merma = inv["merma_cajas"].sum()
valor_quiebres = perdidas["venta_perdida_mxn"].sum()
valor_merma = (inv["merma_cajas"] * inv["costo_mxn"]).sum()

c1, c2, c3, c4 = st.columns(4)
c1.metric("Episodios de Quiebre", f"{total_quiebres}", "Semanas-SKU sin stock")
c2.metric("Venta Perdida", fmt_mxn(valor_quiebres), "Por quiebres en demanda alta", delta_color="inverse")
c3.metric("Merma Total", f"{total_merma:,.0f} cajas", "Producto no vendible")
c4.metric("Costo de Merma", fmt_mxn(valor_merma), "Capital destruido", delta_color="inverse")

st.markdown("---")
st.markdown("#### 📉 Historial de Quiebres de Stock por Semana")
st.caption("Los picos coinciden con temporadas de alta demanda — exactamente cuando más duelen")

quiebres_sem = inv.groupby("semana")["quiebre_stock"].sum().reset_index()
fig = px.area(quiebres_sem, x="semana", y="quiebre_stock",
    labels={"semana": "", "quiebre_stock": "SKUs en quiebre"}, color_discrete_sequence=["#E63946"])
fig.update_traces(fill="tozeroy", fillcolor="rgba(230,57,70,0.15)")
fig.update_layout(height=200, paper_bgcolor="white", plot_bgcolor="white",
    margin=dict(l=0, r=0, t=10, b=0), xaxis=dict(showgrid=False), yaxis=dict(showgrid=True, gridcolor="#F3F4F6"))
st.plotly_chart(fig, use_container_width=True)

left, right = st.columns([2, 3])
with left:
    st.markdown("#### 🔴 SKUs con Más Quiebres Históricos")
    quiebres_sku = inv.groupby(["sku","nombre","marca"]).agg(
        n_quiebres=("quiebre_stock","sum"), dias_promedio_inv=("dias_inventario","mean"),
    ).reset_index().sort_values("n_quiebres", ascending=False).head(10)
    fig2 = px.bar(quiebres_sku, x="n_quiebres", y="nombre", orientation="h", color="n_quiebres",
        color_continuous_scale=["#FEF2F2","#FCA5A5","#E63946"], text="n_quiebres",
        labels={"n_quiebres": "Semanas en quiebre", "nombre": ""})
    fig2.update_traces(textposition="outside")
    fig2.update_layout(height=380, paper_bgcolor="white", plot_bgcolor="white",
        margin=dict(l=0, r=40, t=10, b=0), coloraxis_showscale=False,
        yaxis=dict(tickfont=dict(size=9)), xaxis=dict(showgrid=True, gridcolor="#F3F4F6"))
    st.plotly_chart(fig2, use_container_width=True)

with right:
    st.markdown("#### 💸 Ventas Perdidas por Quiebre — Detalle")
    perdidas_fmt = perdidas.copy()
    perdidas_fmt.loc[:, "venta_perdida_fmt"] = perdidas_fmt["venta_perdida_mxn"].apply(fmt_mxn)
    perdidas_fmt.loc[:, "margen_perdido_fmt"] = perdidas_fmt["margen_perdido_mxn"].apply(fmt_mxn)
    for _, row in perdidas_fmt.iterrows():
        temp_color = {"Gripe/Respiratoria": "#EF4444", "Día de las Madres": "#F59E0B", "Regular": "#6B7280"}.get(row["temporada"], "#6B7280")
        st.markdown(f"""
        <div style="background:white;border-radius:10px;padding:1rem 1.2rem;margin-bottom:0.6rem;box-shadow:0 1px 6px rgba(0,0,0,0.07);border-left:4px solid {temp_color}">
            <div style="display:flex;justify-content:space-between;align-items:flex-start">
                <div>
                    <div style="font-weight:600;font-size:0.88rem;color:#1F2937">{row['nombre']}</div>
                    <div style="font-size:0.78rem;color:#9CA3AF;margin-top:0.1rem">{row['quiebre_inicio']} → {row['quiebre_fin']} · <span style="color:{temp_color};font-weight:600">{row['temporada']}</span> · {row['dias_sin_stock']} días sin stock</div>
                </div>
                <div style="text-align:right">
                    <div style="font-weight:700;color:#E63946;font-size:1rem">{row['venta_perdida_fmt']}</div>
                    <div style="font-size:0.75rem;color:#9CA3AF">margen: {row['margen_perdido_fmt']}</div>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)
    total_p = perdidas_fmt["venta_perdida_mxn"].sum()
    total_m = perdidas_fmt["margen_perdido_mxn"].sum()
    st.markdown(f"""
    <div style="background:#FEF2F2;border:1.5px solid #FCA5A5;border-radius:10px;padding:0.8rem 1.2rem;margin-top:0.5rem">
        <div style="font-weight:700;color:#991B1B">TOTAL PERDIDO: {fmt_mxn(total_p)}</div>
        <div style="font-size:0.83rem;color:#B91C1C">Margen directo perdido: {fmt_mxn(total_m)}</div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")
st.markdown("#### 📊 Clasificación ABC — Concentración del Margen por SKU")
abc_plot = abc_skus.sort_values("margen_total_mxn", ascending=False).copy()
abc_plot.loc[:, "margen_acum_pct"] = abc_plot["margen_total_mxn"].cumsum() / abc_plot["margen_total_mxn"].sum() * 100
fig3 = go.Figure()
fig3.add_trace(go.Bar(x=abc_plot["nombre"].str[:25], y=abc_plot["margen_total_mxn"],
    marker_color=abc_plot["clasificacion_abc"].map({"A":"#C8102E","B":"#FCA5A5","C":"#D1D5DB"}), name="Margen por SKU"))
fig3.add_trace(go.Scatter(x=abc_plot["nombre"].str[:25], y=abc_plot["margen_acum_pct"],
    yaxis="y2", name="Margen acumulado %", line=dict(color="#F4A261", width=2), mode="lines"))
fig3.update_layout(height=380, paper_bgcolor="white", plot_bgcolor="white",
    yaxis=dict(title="Margen MXN", showgrid=True, gridcolor="#F3F4F6", tickformat=",.0f"),
    yaxis2=dict(title="% Acumulado", overlaying="y", side="right", range=[0,105], ticksuffix="%"),
    xaxis=dict(tickangle=45, tickfont=dict(size=8)),
    legend=dict(orientation="h", yanchor="bottom", y=1.02), margin=dict(l=0, r=60, t=30, b=80))
fig3.add_hline(y=80, yref="y2", line_dash="dash", line_color="#E63946", annotation_text="80% del margen", annotation_position="top left")
st.plotly_chart(fig3, use_container_width=True)

skus_a = abc_skus[abc_skus["clasificacion_abc"]=="A"]
skus_c = abc_skus[abc_skus["clasificacion_abc"]=="C"]
col1, col2 = st.columns(2)
with col1:
    st.success(f"✅ **{len(skus_a)} SKUs Clase A** generan el 80% del margen. Prioriza su disponibilidad permanente.")
with col2:
    st.warning(f"⚠️ **{len(skus_c)} SKUs Clase C** generan solo el 5% del margen pero consumen capital de inventario.")
