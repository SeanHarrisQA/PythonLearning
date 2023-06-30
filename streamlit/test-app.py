import pandas as pd
import streamlit as st

st.title('Random football data')

nrows = st.slider('Rows', 0, 23, 18)

@st.cache_data
def load_data():
    data = pd.read_csv('PL.csv', )
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    return data

# Create a text element and let the reader know the data is loading.
data_load_state = st.text('Loading data...')
# Load 10,000 rows of data into the dataframe.
data = load_data()

if st.checkbox('Show raw data'):
    st.subheader('Raw data')
    st.write(data)