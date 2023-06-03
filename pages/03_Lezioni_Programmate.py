import streamlit as st
import numpy as np
import pandas as pd
from utils.utils import *



def create_tab_lezioni_programmate(tab_Lezioni_programmate):
    A = []
    B = []
    C = []
    D = []
    n_lezioni_per_giorno= execute_query(st.session_state["connection"], "SELECT GIORNO, Count(CodC) AS 'Numero Corsi' FROM PROGRAMMA GROUP BY GIORNO;")
    n_lezioni_per_ora= execute_query(st.session_state["connection"], "SELECT ORAINIZIO, Count(CodC) AS 'Numero Corsi' FROM PROGRAMMA GROUP BY ORAINIZIO;")
    lezioni_struct= [dict(zip(n_lezioni_per_giorno.keys(),result)) for result in n_lezioni_per_giorno ]
    lezioni_struct_2= [dict(zip( n_lezioni_per_ora.keys(),result)) for result in  n_lezioni_per_ora ]
    #st.write(lezioni_struct_2)

    for i in range( len(lezioni_struct)):
        A.append(lezioni_struct[i].get("GIORNO"))
        B.append(lezioni_struct[i].get("Numero Corsi"))

    for i in range( len(lezioni_struct)):
        C.append(lezioni_struct_2[i].get("ORAINIZIO"))
        D.append(lezioni_struct_2[i].get("Numero Corsi"))

    df1 = pd.DataFrame(B,A)
    st.line_chart(df1)

    df2 = pd.DataFrame(D,C)
    st.bar_chart(df2)


 
if __name__ == "__main__":
    st.set_page_config(
    page_title="Lezioni Programmate",
    layout="wide",
    
    )
   
    st.title("Lezioni Programmate")

    tab_Lezioni_programmate =st.tabs(["Lezioni Programmate"])

    if check_connection():
        create_tab_lezioni_programmate(tab_Lezioni_programmate)
