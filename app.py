import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="My Website",
    page_icon="🚀",
    layout="wide"
)

# Read HTML file
with open("index.html", "r", encoding="utf-8") as f:
    html_code = f.read()

# Read CSS file
with open("style.css", "r", encoding="utf-8") as f:
    css_code = f.read()

# Inject CSS inside HTML
html_code = html_code.replace(
    '<link rel="stylesheet" href="style.css" />',
    f"<style>{css_code}</style>"
)

components.html(html_code, height=3000, scrolling=True)