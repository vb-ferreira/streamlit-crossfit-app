import streamlit as st
from eda import load_data

# Page config
st.set_page_config(page_title='Crossfir Data')

def main():
    df = load_data()
    st.dataframe(df)

if __name__ == "__main__":
    main()
