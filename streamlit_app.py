from pathlib import Path

import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Generador de diapositivas", page_icon="📊", layout="wide")

# Quita el espacio sobrante de Streamlit para que la app ocupe toda la pantalla
st.markdown(
    "<style>.block-container{padding:0.5rem 1rem 0 1rem;max-width:100%}"
    "header,footer{visibility:hidden}</style>",
    unsafe_allow_html=True,
)

ruta = Path(__file__).parent / "index.html"

if ruta.exists():
    components.html(ruta.read_text(encoding="utf-8"), height=1100, scrolling=True)
else:
    st.error("No se encontró index.html. Súbelo al mismo repositorio, junto a streamlit_app.py.")
