import streamlit as st
from ..statistic_analysis import frequency

def show_frequency(log_df, case_col="case_id", event_col="activity"):
    """
    Zeigt eine Häufigkeitsanalyse der Events im Streamlit-Interface an.

    Parameter:   
         log_df (pandas.Dataframe): Eventlog als Dataframe.
         case_col (str, optional): Name der Spalte, die die Case-ID enthält. 
         event_col (str, optional): Name der Spalte, die die Events/Aktivitäten enthält.
                
     Rückgabewert:
         Die Funktion gibt keinen Wert zurück, sondern erzeugt Ausgaben im Streamlit-Interface.
    """
    st.subheader("📌 Häufigkeit Analyse")
    # Berechnung der Gesamthäufigkeit je Event
    freq_total = frequency.frequency1(log_df, event_col)
    # Berechnung der ANzahl einzigartiger Cases pro Event 
    freq_unique = frequency.frequency_unique(log_df, event_col, case_col)

    # Zusammenführen der Gesamthäufigkeit und der Case-basierten Häufigkeit über den gemeinsamen Event-Namen
    freq_df = freq_total.merge(freq_unique, on="Event")

    st.write("Häufigkeit pro Event/unique Event:")
    st.dataframe(freq_df)

    st.bar_chart(freq_df, x="Event", y="Häufigkeit")
    st.bar_chart(freq_df, x="Event", y="Unique_Häufigkeit")

   