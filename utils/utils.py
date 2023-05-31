from sqlalchemy import create_engine, text
import streamlit as st

"Raccoglie le varie funzioni condivise dalle varie pagine"

def connect_db(dialect,username,password,host,dbname):
    try:
        engine= create_engine(f'{dialect}://{username}:{password}@{host}/{dbname}')
        conn=engine.connect()
        return conn
    except:
        return False
    

def execute_query(conn,query):
    return conn.execute(text(query))


def check_connection():
    if st.sidebar.button("Connetti to DB"):
        myconnection=connect_db(dialect="mysql+pymysql", username="applicazione_quaderno", password="applicazione_quaderno", host="localhost", dbname="palestra")
        if myconnection is not False:
            st.session_state["connection"] = myconnection
        else:
            st.session_state["connection"] = False
            st.sidebar.error("Errore nella connessione")

    if st.session_state['connection']:
        st.sidebar.success("Connesso")
        return True
    
def info_corso_per_tipo(option1,option2):
   

    info_corso= execute_query(st.session_state["connection"], f"SELECT * FROM CORSI WHERE TIPO = '{option1}' AND LIVELLO = {option2};")
    

    info_per_tipo_corso_struct= [dict(zip(info_corso.keys(),result)) for result in info_corso ]

        
     
    return info_per_tipo_corso_struct

def programmazione_corso(option1):
    programmazione_corso= execute_query(st.session_state["connection"], f"SELECT * FROM PROGRAMMA,CORSI WHERE PROGRAMMA.CODC = CORSI.CODC AND TIPO = '{option1}' ;")
    info_programmazione_corso= [dict(zip(programmazione_corso.keys(),result)) for result in programmazione_corso ]
    return info_programmazione_corso


def info_istruttore_cognom_dn(option1, option2):
    istruttore = execute_query(st.session_state["connection"], f"SELECT * FROM ISTRUTTORE WHERE COGNOME = '{option1}' AND DATANASCITA = '{option2}' ")
    info_istruttore= [dict(zip(istruttore.keys(),result)) for result in istruttore ]
    return info_istruttore 