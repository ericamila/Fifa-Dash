import streamlit as st

st.set_page_config(
    page_title="Player Stats 🧑‍🦰",
    layout="wide",
)

df_data = st.session_state["data"]

clubes = df_data["Club"].unique()
club = st.sidebar.selectbox("Selecione um clube", clubes, key="clubes")

df_players = df_data[df_data["Club"] == club]
players = df_players["Name"].unique()
player = st.sidebar.selectbox("Selecione um Jogador", players, key="players")

player_stats = df_players[df_players["Name"] == player].iloc[0]

st.image(player_stats["Photo"])
st.title(player_stats["Name"])
st.markdown(f"**Clube:** {player_stats['Club']}")
st.markdown(f"**Posição:** {player_stats['Position']}")

col1, col2, col3, col4 =st.columns(4)
col1.markdown(f"**Idade:** {player_stats['Age']}")
col2.markdown(f"**Altura:** {player_stats['Height(cm.)'] / 100 } cm")
col3.markdown(f"**Peso:** {player_stats['Weight(lbs.)']*0.453:.2f} kg")

st.divider()
st.subheader(f"Overall {player_stats['Overall']}")
st.progress(int(player_stats["Overall"]))

col1, col2, col3, col4 =st.columns(4)
col1.metric("Valor de Mercado", f"£ {player_stats['Value(£)']:,.2f}")
col2.metric("Remuneração Semanal", f"£ {player_stats['Wage(£)']:,.2f}")
col3.metric("Cláulula de Recisão", f"£ {player_stats['Release Clause(£)']:,.2f}")
