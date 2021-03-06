import streamlit as st
import pandas as pd
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt


st.title('Student Data')


# sidebar

#uploaded_file = st.file_uploader("Choose a file")
# if uploaded_file is not None:
df = pd.read_csv('akm_sample_new201.csv')
st.write(df)


# Filter dataframe

st.write('## Status')
fig = px.histogram(df['Status'])
st.plotly_chart(fig)

st.write('## SKS Kumulatif')
fig1 = px.histogram(df['SKS Kumulatif'])
st.plotly_chart(fig1)

st.write('## IP Kumulatif')
fig2 = px.histogram(df['IP Kumulatif'])
st.plotly_chart(fig2)

st.write('## SKS')
fig3 = px.histogram(df['SKS'])
st.plotly_chart(fig3)


# sidebar
st.sidebar.title('Info')
st.sidebar.write(df.count())

st.sidebar.write('Total Biaya Kuliah Semester : ',
                 df['Biaya Kuliah Semester'].sum())
