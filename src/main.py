import streamlit as st
import duckdb
from st_aggrid import AgGrid, GridOptionsBuilder
from pygwalker.api.streamlit import StreamlitRenderer
from database import DatabaseRepository

st.set_page_config(
    page_title="Resumex",
    page_icon="🅾️",
    layout="wide"
)
repo = DatabaseRepository()
tables = ["consultants", "skills", "consultant_skills", "projects", "staffing"]

with st.sidebar:
    selected_table = st.selectbox("Sélectionner une table", tables)

# Chargement
df = repo.get_dataframe(selected_table)

tab1, tab2 = st.tabs(["📊 Data Viewer", "📈 Visual Analytics"])

with tab1:
    st.subheader(f"Édition : {selected_table}")
    
    # Configuration de la grille
    gb = GridOptionsBuilder.from_dataframe(df)
    gb.configure_default_column(editable=True)
    grid_options = gb.build()
    
    # Rendu de la grille
    grid_return = AgGrid(df, gridOptions=grid_options, reload_data=True)
    
    if st.button("Sauvegarder les modifications"):
        repo.update_table(selected_table, grid_return['data'])
        st.success("Données enregistrées !")
        st.rerun()

with tab2:
    sql = st.text_area("Requête SQL", f"SELECT * FROM {selected_table}", height=100)
    
    try:
        con = duckdb.connect()
        for t in tables:
            con.register(t, repo.get_dataframe(t))
            
        res = con.execute(sql).df()
        
        # Visualisation
        renderer = StreamlitRenderer(res)
        renderer.explorer()
    except Exception as e:
        st.error(f"SQL Error: {e}")