import streamlit as st
import numpy as np
import pandas as pd
import datetime
from utils.utils import *


def create_tab_istruttori(tab_istruttori):
    cognome = st.selectbox(
    '### Seleziona un istruttore',
    ('Johnson','Luvens', 'Diamond', 'Jevis', 'Spencer','Smith' ))
    data = st.date_input(
        "Inserisci la data di nascita dell'istruttore desiderato", 
        datetime.date(1981, 5, 30)
        
    )
    info_istruttore = info_istruttore_cognom_dn(cognome, data)

    if info_istruttore == [] : 
        st.warning("Non è presente questo istruttore ")
    else: 
        st.write(info_istruttore) 
    

if __name__ == "__main__":
    st.set_page_config(
    page_title="Istruttori",
    layout="wide",
    
    )
        
    st.title("Istruttori")

    tab_istruttori =st.tabs(["Istruttori"])

    if check_connection():
        create_tab_istruttori(tab_istruttori)