import streamlit as st
from utils.utils import *
import pandas as pd

st.set_page_config(
        page_title= "Inserimento Corso",
        layout="wide",

        initial_sidebar_state="expanded",
    )

st.title(":grey[Inserimento Nuovo Corso]")

if check_connection():

    st.subheader('Inserisci i dati del nuovo corso:')
    col1, col2 = st.columns(2)
    codice = col1.text_input('Codice Del Corso: ')
    nome = col1.text_input('Nome Del Corso: ')
    tipo = col1.text_input('Tipo Di Corso: ')
    livello = col1.number_input('Livello Del Corso: ', 1, 4)
 
    if codice is '' or nome is '' or tipo is '':
        st.warning('Inserisci tutti i campi')
    elif len(codice) is not 5 or codice[0:2] != 'CT' or codice[-3:].isalnum() is False:
        st.warning("Il formato del codice inserito non è corretto")
    else:
        x = col1.button("Inserisci corso")
        if x:
            queryCodice = f"""SELECT CodC FROM CORSI WHERE CodC = '{codice}'"""
            
            resultCodice = execute_query(st.session_state['connection'], queryCodice)
            df = pd.DataFrame(resultCodice)

            if df.shape[0] is 0:
                query = f""" INSERT INTO CORSI VALUES ('{codice}', '{nome}', '{tipo}', '{livello}')"""
                result = execute_query(st.session_state['connection'], query)
                st.success("L'inserimento del corso è avvenuto correttamente")
            else:
                st.warning('Esiste già un corso con questo codice')
            