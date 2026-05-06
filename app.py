import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Portfolio",
    layout="wide"
)

# Remove Streamlit default padding/header
st.markdown("""
    <style>
        .block-container {
            padding: 0;
        }

        header {
            visibility: hidden;
        }

        footer {
            visibility: hidden;
        }

        iframe {
            width: 100% !important;
        }
    </style>
""", unsafe_allow_html=True)

# Read HTML
with open("index.html", "r", encoding="utf-8") as f:
    html_code = f.read()

# Read CSS
with open("style.css", "r", encoding="utf-8") as f:
    css_code = f.read()

# Inject CSS into HTML
html_code = html_code.replace(
    '<link rel="stylesheet" href="style.css" />',
    f"<style>{css_code}</style>"
)

# Render website
components.html(
    html_code,
    height=5000,
    scrolling=False
)