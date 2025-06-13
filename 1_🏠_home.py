import streamlit as st
import webbrowser
import pandas as pd
from datetime import datetime

# Configurações iniciais do Streamlit
st.set_page_config(
    page_title="Home: FIFA World Cup 2023⚽",
    layout="wide",
)
@st.cache_data()
def load_data():
    df_data = pd.read_csv("datasets/CLEAN_FIFA23_official_data.csv", index_col=0)
    df_data = df_data[df_data["Contract Valid Until"] >= datetime.today().year]
    df_data = df_data[df_data["Value(£)"] > 0]
    df_data = df_data.sort_values(by="Overall", ascending=False)
    st.session_state["data"] = df_data

if "data" not in st.session_state:
    load_data()

st.markdown("# FIFA World Cup 2023⚽  \n### Official dataset")

url = "https://www.kaggle.com/datasets/kevwesophia/fifa23-official-datasetclean-data"
st.markdown(f'<a href="{url}" target="_blank"><button class="st-emotion-cache-13lcgu3 eacrzsi2">Acesse os dados no Kaggle</button></a>', unsafe_allow_html=True)

st.markdown(
    """
    O conjunto de dados
    de jogadores de futebol de 2017 a 2023 fornece informações 
    abrangentes sobre jogadores de futebol profissionais.
    O conjunto de dados contém uma ampla gama de atributos, incluindo dados demográficos 
    do jogador, características físicas, estatísticas de jogo, detalhes do contrato e 
    afiliações de clubes. 
    
    Com **mais de 17.000 registros**, este conjunto de dados oferece um recurso valioso para 
    analistas de futebol, pesquisadores e entusiastas interessados em explorar vários 
    aspectos do mundo do futebol, pois permite estudar atributos de jogadores, métricas de 
    desempenho, avaliação de mercado, análise de clubes, posicionamento de jogadores e 
    desenvolvimento do jogador ao longo do tempo.
"""
)