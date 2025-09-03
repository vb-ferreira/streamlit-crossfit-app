import streamlit as st
# import pandas as pd
from eda import load_data, clean_data_for_scatterplot, generate_scatterplot

# Page config
st.set_page_config(page_title='Crossfir Data')

def main():
    df = load_data()

    # Scatterplot
    df = clean_data_for_scatterplot(df)
    st.plotly_chart(generate_scatterplot(df))
    # Scatterplot stats
    if st.checkbox('Show Statistcs'):
        st.subheader('Averages')
        st.markdown(f'**Deadlift**: {df["deadlift"].mean():.2f} lbs')
        st.markdown(f'**Weight**: {df["weight"].mean():.2f} lbs')

    # Raw data
    with st.expander('Raw Data'):
        st.dataframe(df)

if __name__ == "__main__":
    main()
