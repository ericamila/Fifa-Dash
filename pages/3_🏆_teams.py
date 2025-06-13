import streamlit as st

st.set_page_config(
    page_title="Teams 🏆",
    layout="wide",
)

df_data = st.session_state["data"]
clubes = df_data["Club"].unique()
club = st.sidebar.selectbox("Selecione um clube", clubes, key="clubes")


df_filter = df_data[df_data["Club"] == club].set_index("Name")
st.image(df_filter["Club Logo"].iloc[0])
st.markdown(f"## Jogadores do {club}")

columns = ["Age", "Photo", "Flag", "Overall", 'Value(£)', 'Wage(£)', 'Joined', 
           'Height(cm.)', 'Weight(lbs.)', 'Contract Valid Until', 'Release Clause(£)']

st.dataframe(df_filter[columns],
             column_config={
                "Overall": st.column_config.ProgressColumn("Overall", format="%d"),
                "Wage(£)": st.column_config.ProgressColumn("Weekly Wage", format="£%f", min_value=0, max_value=df_filter["Wage(£)"].max()),
                "Photo": st.column_config.ImageColumn(),
                "Flag": st.column_config.ImageColumn("Country"),
             })