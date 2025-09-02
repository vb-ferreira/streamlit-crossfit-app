import marimo

__generated_with = "0.15.2"
app = marimo.App(width="medium", app_title="EDA")

with app.setup:
    # Esta célulla roda antes de qualquer outra. Qualquer dependência usada por uma função/classe 
    # que será importada deverá ser declarada aqui. 
    import streamlit as st
    import pandas as pd
    import plotly.express as px


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
@st.cache_data(show_spinner="Carregando os dados do arquivo...")
def load_data():
    return pd.read_csv('data/athletes.csv')


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""# **Plots**""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""## **Scatterplot**""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""Relação entre peso do atleta (`weight`) e peso levantado no levantamento terra (`deadlift`). """)
    return


@app.function
def generate_scatterplot(df):
    fig = px.scatter(
        df,
        x="weight",
        y="deadlift",
        title="Weight vs Deadlift"
    )

    fig.update_layout(
        xaxis_title="Body Weight (lbs)",
        yaxis_title="Deadlift (lbs)"
    )

    return fig


if __name__ == "__main__":
    app.run()
