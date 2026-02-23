"""
utils/ui.py
Componentes visuales enterprise para Grupo Jaloma PoC
"""

import streamlit as st

JALOMA_COLORS = {
    "primary":   "#C8102E",   # rojo Jaloma
    "accent":    "#E63946",   # rojo medio
    "light":     "#FEE2E2",   # rojo claro / rosa
    "warning":   "#F4A261",   # naranja
    "danger":    "#991B1B",   # rojo oscuro
    "success":   "#2DC653",   # verde éxito
    "neutral":   "#F8F9FB",
    "dark":      "#1A1A2E",   # dark charcoal enterprise
    "muted":     "#6C757D",
    "sidebar":   "#16213E",   # sidebar azul-oscuro
}

def inject_css():
    st.markdown(f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');

    html, body, [class*="css"] {{
        font-family: 'Inter', sans-serif;
    }}

    /* ─── Fondo principal ──────────────────────────────── */
    .main {{ background-color: #F8F9FB; }}

    /* ─── Sidebar enterprise ───────────────────────────── */
    [data-testid="stSidebar"] {{
        background: linear-gradient(180deg, {JALOMA_COLORS["dark"]} 0%, {JALOMA_COLORS["sidebar"]} 100%);
    }}
    [data-testid="stSidebar"] * {{
        color: rgba(255,255,255,0.9) !important;
    }}
    [data-testid="stSidebar"] .stSelectbox label {{
        color: rgba(255,255,255,0.55) !important;
        font-size: 0.75rem;
        text-transform: uppercase;
        letter-spacing: 0.08em;
        font-weight: 600;
    }}
    [data-testid="stSidebar"] hr {{
        border-color: rgba(255,255,255,0.08) !important;
        margin: 1rem 0;
    }}
    [data-testid="stSidebar"] .stMarkdown p {{
        font-size: 0.88rem;
        letter-spacing: 0.01em;
    }}
    [data-testid="stSidebar"] img {{
        border-radius: 8px;
        margin-bottom: 0.5rem;
    }}

    /* ─── Page header enterprise ───────────────────────── */
    .page-header {{
        background: linear-gradient(135deg, {JALOMA_COLORS["dark"]} 0%, #2D1F3D 60%, #3D1F2E 100%);
        padding: 1.8rem 2.2rem;
        border-radius: 10px;
        color: white;
        margin-bottom: 1.5rem;
        border-bottom: 3px solid {JALOMA_COLORS["primary"]};
        box-shadow: 0 4px 20px rgba(26,26,46,0.15);
        position: relative;
        overflow: hidden;
    }}
    .page-header::after {{
        content: '';
        position: absolute;
        top: 0; right: 0;
        width: 300px; height: 100%;
        background: radial-gradient(ellipse at 100% 50%, rgba(200,16,46,0.12) 0%, transparent 70%);
        pointer-events: none;
    }}
    .page-header h1 {{
        color: white;
        font-size: 1.65rem;
        font-weight: 700;
        margin: 0;
        letter-spacing: -0.01em;
        position: relative;
        z-index: 1;
    }}
    .page-header p {{
        color: rgba(255,255,255,0.7);
        margin: 0.3rem 0 0;
        font-size: 0.9rem;
        font-weight: 400;
        position: relative;
        z-index: 1;
    }}

    /* ─── KPI Cards enterprise ─────────────────────────── */
    .kpi-card {{
        background: white;
        border-radius: 10px;
        padding: 1.2rem 1.4rem;
        border-top: 3px solid {JALOMA_COLORS["primary"]};
        box-shadow: 0 2px 12px rgba(0,0,0,0.04);
        transition: all 0.25s ease;
        position: relative;
    }}
    .kpi-card:hover {{
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(0,0,0,0.08);
    }}
    .kpi-label {{
        font-size: 0.72rem;
        color: {JALOMA_COLORS["muted"]};
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 0.08em;
        margin-bottom: 0.3rem;
    }}
    .kpi-value {{
        font-size: 1.85rem;
        font-weight: 800;
        color: {JALOMA_COLORS["dark"]};
        line-height: 1.1;
    }}
    .kpi-delta {{
        font-size: 0.78rem;
        color: {JALOMA_COLORS["muted"]};
        margin-top: 0.3rem;
        line-height: 1.3;
    }}
    .kpi-danger {{ border-top-color: {JALOMA_COLORS["danger"]}; }}
    .kpi-warn   {{ border-top-color: {JALOMA_COLORS["warning"]}; }}
    .kpi-success{{ border-top-color: {JALOMA_COLORS["success"]}; }}

    /* ─── Alerta Cards ─────────────────────────────────── */
    .alerta-critica {{
        background: white;
        border: 1px solid #FECACA;
        border-left: 5px solid {JALOMA_COLORS["danger"]};
        border-radius: 10px;
        padding: 1.3rem 1.5rem;
        margin-bottom: 1rem;
        box-shadow: 0 2px 12px rgba(153,27,27,0.06);
        transition: box-shadow 0.2s ease;
    }}
    .alerta-critica:hover {{
        box-shadow: 0 4px 18px rgba(153,27,27,0.10);
    }}
    .alerta-warning {{
        background: white;
        border: 1px solid #FDE68A;
        border-left: 5px solid {JALOMA_COLORS["warning"]};
        border-radius: 10px;
        padding: 1.3rem 1.5rem;
        margin-bottom: 1rem;
        box-shadow: 0 2px 12px rgba(244,162,97,0.06);
        transition: box-shadow 0.2s ease;
    }}
    .alerta-warning:hover {{
        box-shadow: 0 4px 18px rgba(244,162,97,0.10);
    }}
    .alerta-info {{
        background: white;
        border: 1px solid #E5E7EB;
        border-left: 5px solid {JALOMA_COLORS["primary"]};
        border-radius: 10px;
        padding: 1.3rem 1.5rem;
        margin-bottom: 1rem;
        box-shadow: 0 2px 12px rgba(0,0,0,0.04);
        transition: box-shadow 0.2s ease;
    }}
    .alerta-info:hover {{
        box-shadow: 0 4px 18px rgba(0,0,0,0.08);
    }}

    .alerta-badge {{
        display: inline-block;
        padding: 0.2rem 0.65rem;
        border-radius: 4px;
        font-size: 0.68rem;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 0.06em;
        margin-bottom: 0.5rem;
    }}
    .badge-red   {{ background: #FEE2E2; color: {JALOMA_COLORS["danger"]}; }}
    .badge-orange{{ background: #FEF3C7; color: #92400E; }}
    .badge-green {{ background: #D1FAE5; color: #065F46; }}

    .alerta-titulo {{
        font-size: 1rem;
        font-weight: 700;
        color: {JALOMA_COLORS["dark"]};
        margin-bottom: 0.35rem;
    }}
    .alerta-desc {{
        font-size: 0.85rem;
        color: #4B5563;
        line-height: 1.55;
    }}
    .alerta-impacto {{
        background: linear-gradient(135deg, #F9FAFB 0%, #F3F4F6 100%);
        border-radius: 8px;
        padding: 0.7rem 1rem;
        margin-top: 0.7rem;
        font-size: 0.83rem;
        color: {JALOMA_COLORS["dark"]};
        border: 1px solid #E5E7EB;
    }}
    .impacto-num {{
        font-size: 1.25rem;
        font-weight: 800;
    }}

    /* ─── Tablas de datos ──────────────────────────────── */
    .data-table {{
        font-size: 0.83rem;
        width: 100%;
        border-collapse: separate;
        border-spacing: 0;
        border-radius: 8px;
        overflow: hidden;
        box-shadow: 0 1px 8px rgba(0,0,0,0.04);
    }}
    .data-table th {{
        background: {JALOMA_COLORS["dark"]};
        color: white;
        padding: 0.65rem 0.9rem;
        text-align: left;
        font-weight: 600;
        font-size: 0.73rem;
        text-transform: uppercase;
        letter-spacing: 0.05em;
    }}
    .data-table td {{
        padding: 0.55rem 0.9rem;
        border-bottom: 1px solid #F3F4F6;
        color: #374151;
    }}
    .data-table tr:nth-child(even) td {{ background: #FAFBFC; }}
    .data-table tr:hover td {{ background: #F3F4F6; }}

    /* ─── Streamlit dataframe override ─────────────────── */
    [data-testid="stDataFrame"] {{
        border-radius: 8px;
        overflow: hidden;
        box-shadow: 0 1px 8px rgba(0,0,0,0.04);
    }}

    /* ─── Botones enterprise ───────────────────────────── */
    .stButton > button {{
        background: {JALOMA_COLORS["primary"]};
        color: white;
        border: none;
        border-radius: 6px;
        font-weight: 600;
        padding: 0.5rem 1.2rem;
        font-size: 0.85rem;
        letter-spacing: 0.01em;
        transition: all 0.25s ease;
        box-shadow: 0 2px 8px rgba(200,16,46,0.15);
    }}
    .stButton > button:hover {{
        background: #A30D24;
        transform: translateY(-1px);
        box-shadow: 0 4px 14px rgba(200,16,46,0.25);
    }}

    /* ─── Chat input ───────────────────────────────────── */
    .stChatInput input {{
        border-radius: 8px !important;
        border: 1.5px solid #D1D5DB !important;
        transition: all 0.2s ease;
    }}
    .stChatInput input:focus {{
        border-color: {JALOMA_COLORS["primary"]} !important;
        box-shadow: 0 0 0 3px rgba(200,16,46,0.08) !important;
    }}

    /* ─── Separadores enterprise ────────────────────────── */
    hr {{
        border: none;
        height: 1px;
        background: linear-gradient(90deg, {JALOMA_COLORS["primary"]}22, #E5E7EB 30%, #E5E7EB 70%, transparent 100%);
        margin: 1.5rem 0;
    }}

    /* ─── Métricas nativas ─────────────────────────────── */
    [data-testid="metric-container"] {{
        background: white;
        border-radius: 10px;
        padding: 1rem 1.2rem;
        box-shadow: 0 2px 12px rgba(0,0,0,0.04);
        border-top: 3px solid {JALOMA_COLORS["primary"]};
        transition: all 0.25s ease;
    }}
    [data-testid="metric-container"]:hover {{
        transform: translateY(-1px);
        box-shadow: 0 4px 16px rgba(0,0,0,0.07);
    }}
    [data-testid="metric-container"] label {{
        font-size: 0.72rem !important;
        text-transform: uppercase;
        letter-spacing: 0.06em;
        font-weight: 600 !important;
        color: {JALOMA_COLORS["muted"]} !important;
    }}
    [data-testid="metric-container"] [data-testid="stMetricValue"] {{
        font-weight: 800 !important;
        color: {JALOMA_COLORS["dark"]} !important;
    }}

    /* ─── Streamlit info/error/success/warning overrides ─ */
    .stAlert {{
        border-radius: 8px;
        border-left-width: 4px;
        font-size: 0.88rem;
    }}

    /* ─── Section headers ──────────────────────────────── */
    .main h4 {{
        font-weight: 700;
        color: {JALOMA_COLORS["dark"]};
        letter-spacing: -0.01em;
        font-size: 1.1rem;
    }}
    .main h3 {{
        font-weight: 700;
        color: {JALOMA_COLORS["dark"]};
        letter-spacing: -0.01em;
    }}

    /* ─── Scrollbar sutil ──────────────────────────────── */
    ::-webkit-scrollbar {{
        width: 6px;
        height: 6px;
    }}
    ::-webkit-scrollbar-track {{
        background: transparent;
    }}
    ::-webkit-scrollbar-thumb {{
        background: #D1D5DB;
        border-radius: 3px;
    }}
    ::-webkit-scrollbar-thumb:hover {{
        background: #9CA3AF;
    }}

    /* ─── Multiselect pills ────────────────────────────── */
    [data-testid="stSidebar"] span[data-baseweb="tag"] {{
        background: rgba(200,16,46,0.15) !important;
        border: 1px solid rgba(200,16,46,0.3) !important;
        color: white !important;
        border-radius: 4px !important;
    }}
    </style>
    """, unsafe_allow_html=True)


def page_header(title: str, subtitle: str = ""):
    st.markdown(f"""
    <div class="page-header">
        <h1>{title}</h1>
        {"<p>" + subtitle + "</p>" if subtitle else ""}
    </div>
    """, unsafe_allow_html=True)


def kpi_card(label: str, value: str, delta: str = "", tipo: str = ""):
    tipo_class = {"danger": "kpi-danger", "warn": "kpi-warn", "success": "kpi-success"}.get(tipo, "")
    st.markdown(f"""
    <div class="kpi-card {tipo_class}">
        <div class="kpi-label">{label}</div>
        <div class="kpi-value">{value}</div>
        {"<div class='kpi-delta'>" + delta + "</div>" if delta else ""}
    </div>
    """, unsafe_allow_html=True)


def alerta_card(tipo: str, badge: str, titulo: str, desc: str, impacto_label: str, impacto_valor: str, badge_class: str = "badge-red"):
    clase = {"critica": "alerta-critica", "warning": "alerta-warning", "info": "alerta-info"}.get(tipo, "alerta-info")
    st.markdown(f"""
    <div class="{clase}">
        <span class="alerta-badge {badge_class}">{badge}</span>
        <div class="alerta-titulo">{titulo}</div>
        <div class="alerta-desc">{desc}</div>
        <div class="alerta-impacto">
            {impacto_label}: <span class="impacto-num">{impacto_valor}</span>
        </div>
    </div>
    """, unsafe_allow_html=True)


def fmt_mxn(valor: float, decimales: int = 0) -> str:
    if valor >= 1_000_000:
        return f"${valor/1_000_000:.1f}M MXN"
    elif valor >= 1_000:
        return f"${valor/1_000:.0f}K MXN"
    else:
        return f"${valor:,.{decimales}f} MXN"
