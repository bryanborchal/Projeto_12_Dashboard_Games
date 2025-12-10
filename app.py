import streamlit as st
import pandas as pd
import plotly.express as px

df = pd.read_csv('vgsales.csv')



# ------------------------------------------------------ SIDEBAR
st.sidebar.title('Painel de jogos')

st.sidebar.image('image_1.png')



# ----------------------------------------------------- BODY

with st.container():
    col1,col2,col3 = st.columns(3)

    with col1:
        st.metric('Plataformas distintas',df['Platform'].nunique())

    with col2:
        st.metric('Gêneros distintos',df['Genre'].nunique())

    with col3:
        st.metric('Publishers distintos',df['Publisher'].nunique())

with st.container():
    st.subheader('Top 5 Publishers por Vendas Globais')

    top_5 = df.groupby('Publisher')['Global_Sales'].sum().sort_values(ascending=False).head().reset_index()
    st.table(top_5)

with st.container():
    fig = px.bar(top_5,x='Publisher',y='Global_Sales',title='Tabela Top 5 Publishers que mais venderam')
    st.plotly_chart(fig,use_container_width=True)