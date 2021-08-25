import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')


df = pd.read_excel('akm_sample_new201.xlsx')
st.header("template_kelulusan201")
st.write("")
st.write(df)


y = df['Status']
grade_counts = y.value_counts().sort_index()
#grade_counts.plot.bar()
st.write("")
st.write("")
st.write("Status Nilai")
st.write("")
st.bar_chart(grade_counts)

x = df['IP Kumulatif']
ips = x.value_counts().sort_index()
#grade_counts.plot.bar()
st.write("")
st.write("")
st.write("Stat IP Kumulatif")
st.write("")
st.line_chart(ips)



#st.write("")
#st.write("")
#st.write("Total")
#st.write("")
#st.write(df.count())

st.write("")
st.write("")
st.write("Summary")
st.write("")
st.write(df.describe())