import marimo

__generated_with = "0.15.2"
app = marimo.App(width="medium", app_title="EDA")

with app.setup:
    # Esta célulla roda antes de qualquer outra. Qualquer dependência usada por uma função/classe 
    # que será importada deverá ser declarada aqui. 
    import streamlit as st
    import pandas as pd


@app.cell
def _():
    # Outras dependências...
    import marimo as mo
    return (mo,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""# **Load data**""")
    return


@app.function
@st.cache_data(ttl=10800, show_spinner="Carregando dados do Google Sheets...")
def load_data():
    return pd.read_csv('data/athletes.csv')


if __name__ == "__main__":
    app.run()
