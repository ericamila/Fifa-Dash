import streamlit as st
from data import load_data

# Configurações iniciais do Streamlit
st.set_page_config(
    page_title="Home: FIFA World Cup 2023⚽",
    layout="wide",
)

if "data" not in st.session_state:
    load_data()

st.markdown("# FIFA World Cup 2023⚽  \n### Official dataset")

st.button('🔄 Atualizar Dados', on_click=load_data)

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