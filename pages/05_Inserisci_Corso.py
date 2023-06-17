import streamlit as st
from utils.utils import *
import pandas as pd
from datetime import time

def get_list(attributo, tabella):
    query = f"""SELECT DISTINCT {attributo} FROM {tabella} ORDER BY {attributo}"""
    result = execute_query(st.session_state["connection"], query)
    result_list = []
    for row in result.mappings():
        result_list.append(row[attributo])
    return result_list

st.set_page_config(
        page_title= "Inserimento Lezione",
        layout="wide",

        initial_sidebar_state="expanded",
    )

st.title(":grey[Inserimento Nuova Lezione]")


if check_connection():
        st.subheader('Inserisci i dati della nuova lezione:')
        col1, col2 = st.columns(2)
        cfList = get_list('CodFisc', 'ISTRUTTORE')
        corsoList = get_list('CodC', 'CORSI')
        with col1:
            cf = st.selectbox("Codice Fiscale Dell'Istruttore", cfList)
            giorno = st.selectbox("Giorno Della Settimana", ["Lunedì", "Martedì", "Mercoledì", "Giovedì", "Venerdì"])
            oraInizio = st.slider("Ora Di Inizio", time(), time(23,59), time(12))
            durata = st.slider("Durate Del Corso", 0, 60, 30)
            corso = st.selectbox("Codice Del Corso", corsoList)
            sala = st.number_input('Sala: ', 0)
            oraInizio = str(oraInizio)[:-3]

            query = f"""SELECT COUNT(*) as N FROM PROGRAMMA WHERE CodFisc = '{cf}' AND Giorno = '{giorno}' AND CodC = '{corso}' """
            result = execute_query(st.session_state["connection"], query)

            if result.mappings().first()['N'] is not 0:
                  st.warning("Questa lezione esiste già")
            else:
                if st.button("Inserisci Lezione"):
            
                    query = f""" INSERT INTO PROGRAMMA VALUES ('{cf}', '{giorno}', '{oraInizio}', '{durata}',  '{sala}', '{corso}') """
                    result = execute_query(st.session_state["connection"], query)
                    st.success("L'inserimento della lezione è avvenuto correttamente")
