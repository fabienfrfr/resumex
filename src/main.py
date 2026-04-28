import streamlit as st
import duckdb
from st_aggrid import AgGrid, GridOptionsBuilder
import pygwalker as pyg
from database import DatabaseRepository

st.set_page_config(layout="wide")
st.title("🛠️ LanceDB + DuckDB Dashboard")

# Initialize Repository
repo = DatabaseRepository()

# SQL Input
sql_query = st.text_area("SQL Query", "SELECT * FROM df", height=100)

try:
    # Load current data and execute SQL via DuckDB
    df = repo.get_dataframe()
    result_df = duckdb.query(sql_query).to_df()
    
    st.subheader("Data Viewer")
    grid = AgGrid(result_df, editable=True, fit_columns_on_grid_load=True)
    
    # Sync button
    if st.button("Save Changes"):
        repo.update_table(grid['data'])
        st.success("Table updated successfully!")
        
    # Visual Analytics
    if st.button("Open Visual Analytics"):
        pyg.walk(result_df)
        
except Exception as e:
    st.error(f"SQL Error: {e}")