import streamlit as st
from display_analysis.frequency import show_frequency
from display_analysis.numeric import show_numeric
from display_analysis.duration import show_duration
from display_analysis.outliers import show_outliers
from display_analysis.resources import show_resources
from display_analysis.time import show_time


def show_all_analysis(log):
    """
    show_all_analysis zeigt alls statistischen Analysen des Eventlogs in Streamlit an.

    
    :param log: das Eventlog als dataframe

    :tabs  
        Häufigkeit,
        Numerisch,
        Prozessdauer,
        Ausreißer,
        Ressourcen,
        Zeit-Analyse,
        Standardwerte-Vergleich
    """

    tab1, tab2, tab3, tab4, tab5, tab6, tab7 = st.tabs([
       "Ausreißer", 
       "Häufigkeit",
        "Numerisch",
        "Prozessdauer",
        "Ressourcen",
        
        
        "Zeit-Analyse",
        "Standardwerte-Vergleich"
    ])

    
    with tab1:
        show_outliers(log)
        
    with tab2:
        show_frequency(log)

    with tab3:
        show_numeric(log)

    with tab4:
        show_duration(log)
    with tab5:
        show_resources(log)



    with tab6:
        show_time(log)

