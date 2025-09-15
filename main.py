import streamlit as st
from eda import load_data, clean_data_for_scatterplot, generate_scatterplot

# Page config
st.set_page_config(page_title='Crossfir Data')

def main():
    df = load_data()

    # Sidebar
    with st.sidebar:
        st.subheader('Options')
        # Nomes das colunas numéricas (dropa tbm o id)
        numeric_columns = df.select_dtypes(include=['number']).drop(['athlete_id'], axis='columns').columns.tolist()
        # Seleciona atributo do eixo X
        x_axis = st.selectbox(
            label='X axis',
            options=numeric_columns,
            key='x_axis'
        )
        # Seleciona atributo do eixo y (diferente do x)
        y_axis = st.selectbox(
            label='Y axis',
            options=[col for col in numeric_columns if col != x_axis],
            key='y_axis'
        )
        # Seleciona modelo de regressão
        trendline_options = {
            'Ordinary Least Squares': 'ols',
            'Expanding': 'expanding',
            'Locally Weighted Scatterplot Smoothing': 'lowess'
        }
        trendline_display = st.selectbox(
            label='Trendline',
            options=trendline_options.keys(),
            key='trendlne'
        )
        trendline = trendline_options[trendline_display]

    # Scatterplot
    df = clean_data_for_scatterplot(df)
    st.plotly_chart(generate_scatterplot(df, x_axis, y_axis, trendline))
    # Scatterplot stats
    if st.checkbox('Show Statistcs'):
        st.subheader('Averages')
        st.markdown(f'**{x_axis}**: {df[x_axis].mean():.2f}')
        st.markdown(f'**{y_axis}**: {df[y_axis].mean():.2f}')

    # Raw data
    with st.expander('Raw Data'):
        st.dataframe(df)

if __name__ == "__main__":
    main()
