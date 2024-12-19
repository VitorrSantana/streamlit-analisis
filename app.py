import streamlit as st
import pandas as pd

from requests_bc import request_pix_municipio
from datetime import datetime
from datetime import timedelta
from dateutil.relativedelta import relativedelta

with st.sidebar:
    
    st.title("Pix por Municipio")
    st.header('Explicação da Aplicação')

    st.write('Analise de algumas informações do Pix por Municipo')

st.title('Analise do Pix')

min_value= datetime.strptime('2020-12-01','%Y-%m-%d')
max_value= datetime.now() - relativedelta(months=1)

municipio = st.text_input(label="Digite o Municipio que deseja visualizar: ")
intervalo_datas = st.sidebar.slider("Selecione o périodo",
                                    min_value=min_value,
                                    max_value=max_value,
                                    value=(min_value,max_value),
                                    #step=(timedelta(days=32)),
                                    #format="YYYY.MM.01",
                                    )

if  municipio:
    dados_municipio = request_pix_municipio(municipio=municipio)
    print(dados_municipio)
    st.line_chart(dados_municipio,x='AnoMes',y='QT_PagadorPF')

#= pd.to_datetime(f"{str(dados_municipio['AnoMes'])[:4]}-{str(dados_municipio['AnoMes'])[4:]}-01")