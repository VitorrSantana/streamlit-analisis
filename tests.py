import pandas as pd
import streamlit as st

municipios = pd.read_csv('./municipios.csv').sort_values(['UF','Nome'])

def municipio_estado(): 

    ufs = municipios['UF'].unique()
    uf_selecionada = st.sidebar.selectbox('Escolha um estado: ',ufs)
    nome_municipios_uf = municipios[municipios['UF']==uf_selecionada]['Nome'].unique()
    municipio_selecionado = st.sidebar.selectbox('Escolha um municipio: ', nome_municipios_uf)
    return municipio_selecionado