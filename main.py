import streamlit as st
from eda import load_data, generate_scatterplot

# Page config
st.set_page_config(page_title='Crossfir Data')

def main():
    df = load_data()
    st.plotly_chart(generate_scatterplot(df))
    with st.expander('Raw Data'):
        st.dataframe(df)

if __name__ == "__main__":
    main()
