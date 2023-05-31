import streamlit as st
import numpy as np
import pandas as pd
from utils.utils import connect_db, check_connection

if __name__ == "__main__":
    st.set_page_config(
    page_title="Sviluppo di un'applicazione web con Streamlit e MySQL",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://dbdmg.polito.it/',
        'Report a bug': "https://dbdmg.polito.it/",
        'About': "# Corso di *Basi di Dati*"
        }
    )

    col1,col2= st.columns([4,2])
    with col1: 
        st.title(":blue[Sviluppo di un'applicazione web] con :red[Streamlit e MySQL]")
        st.markdown("# Obiettivo:")
        st.markdown("### Creare un applicazione web in Python (Streamlit) in grado di interagire con un database MySQL in modo da eseguire interrogazioni in base alle interazioni dell'utente. ")
        st.markdown("##### Creato da: :red[Giuseppe Calvello S299095] ")

    with col2:
        st.image("images/polito_white.png")



    if "connection" not in st.session_state.keys():
        st.session_state["connection"] = False

    check_connection()