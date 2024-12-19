import requests
import pandas as pd
from urllib.parse import quote

def request_pix_municipio(data_base_inicial='2023-01-01',data_base_final='2024-11-02',municipio='Buenópolis') -> pd.DataFrame():
    
    municipio = quote(municipio) # Padrão Esperado

    range_database = pd.interval_range(pd.to_datetime(data_base_inicial),pd.to_datetime(data_base_final),freq='MS') # intervalo_datas
    range_database = [str(database)[1:8].replace('-','') for database in  range_database] # tratamento em intervalo
    
    pahth_request = lambda municipio, database: f"https://olinda.bcb.gov.br/olinda/servico/Pix_DadosAbertos/versao/v1/odata/TransacoesPixPorMunicipio(DataBase=@DataBase)?@DataBase='{database}'&$top=100&$filter=Municipio%20eq%20'{municipio}'&$format=json&$select=AnoMes,Municipio_Ibge,Municipio,Estado_Ibge,Estado,Sigla_Regiao,Regiao,VL_PagadorPF,QT_PagadorPF,VL_PagadorPJ,QT_PagadorPJ,VL_RecebedorPF,QT_RecebedorPF,VL_RecebedorPJ,QT_RecebedorPJ,QT_PES_PagadorPF,QT_PES_PagadorPJ,QT_PES_RecebedorPF,QT_PES_RecebedorPJ"

    dados_municipio = pd.DataFrame(requests.get(pahth_request(municipio,range_database[0])).json()['value']) # request and load for DataFrame

    for database in range_database[1:]:
        print(database)

        dados_municipio_aux = pd.DataFrame(requests.get(pahth_request(municipio,database)).json()['value'])
        dados_municipio = pd.concat([dados_municipio,dados_municipio_aux],ignore_index=True)
    
    dados_municipio['AnoMes']  = dados_municipio['AnoMes'].astype(str)
    return dados_municipio
