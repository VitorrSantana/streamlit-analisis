import streamlit as st
import pandas as pd

from requests_bc import request_pix_municipio
from tests import  municipio_estado
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

municipio = municipio_estado()
print(municipio)
intervalo_datas = st.sidebar.date_input("Selecione o périodo",
                                    min_value=min_value,
                                    max_value=max_value,
                                    value=(min_value,max_value),
                                    #step=(timedelta(days=32)),
                                    #format="YYYY.MM.01",
                                    )
data1 = f'{str(intervalo_datas[0])[:8]}01'
data2 = f'{str(intervalo_datas[1])[:8]}02'

print(data1,data2)
print(municipio)
if  municipio:
    st.markdown(f'Municipio: {municipio}')
    dados_municipio = request_pix_municipio(municipio=municipio,data_base_inicial=data1,data_base_final=data2)
    print(dados_municipio)
    st.bar_chart(dados_municipio,x='AnoMes',y='QT_RecebedorPF')
    st.line_chart(dados_municipio,x='AnoMes',y='VL_RecebedorPF')

    st.bar_chart(dados_municipio,x='AnoMes',y='QT_RecebedorPJ')
    st.line_chart(dados_municipio,x='AnoMes',y='VL_RecebedorPJ')
#= pd.to_datetime(f"{str(dados_municipio['AnoMes'])[:4]}-{str(dados_municipio['AnoMes'])[4:]}-01")