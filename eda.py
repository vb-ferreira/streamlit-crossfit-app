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
    mo.md(r"""# **Cleaning Data**""")
    return


@app.function
@st.cache_data()
def clean_data_for_scatterplot(df, sample_size, x_axis, y_axis, x_thresholds, y_thresholds):
    filtered_df = df.dropna(subset=[x_axis, y_axis])
    no_outliers_df = filtered_df[
        (filtered_df[x_axis] <= x_thresholds[1]) & (filtered_df[y_axis] <= y_thresholds[1]) &
        (filtered_df[x_axis] >= x_thresholds[0]) & (filtered_df[y_axis] >= y_thresholds[0])
    ]
    return no_outliers_df.head(sample_size)


@app.cell
def _():
    # Tests
    # x = clean_data_for_scatterplot(load_data())
    return


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
    mo.md(r"""Relação entre duas variáveis com linha de tendência.""")
    return


@app.function
def generate_scatterplot(df, x_axis="weight", y_axis="deadlift", trendline="ols"):
    fig = px.scatter(
        df,
        x=x_axis,
        y=y_axis,
        title=f"{x_axis} vs {y_axis}",
        trendline=trendline,
        hover_name='name',
        hover_data=['region', 'affiliate', 'team', 'gender']
    )

    fig.update_layout(
        xaxis_title=x_axis,
        yaxis_title=y_axis
    )

    return fig


@app.function
def generate_histogram(df, column):
    fig = px.histogram(
        df,
        x=column,
        nbins=50, 
        opacity=0.7, 
        title=f'Ditribution of {column}'
    )
    
    return fig


if __name__ == "__main__":
    app.run()
