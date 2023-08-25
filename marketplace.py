import streamlit as st
import pandas as pd

columns = ['name','kor','eng','math']
data=[
    ['teemo',100, 100, 100],
    ['jax', 90, 91, 92],
    ['jinx',80,81,82],
    ['yasuo',20,21,22]
]

df = pd.DataFrame(data, columns=columns)
st.dataframe(df)