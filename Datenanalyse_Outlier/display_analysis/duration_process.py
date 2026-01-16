import streamlit as st
from ..statistic_analysis import duration_process
from ..statistic_analysis.second_to_time import second_to_time

def show_process_duration(log_df):
    """
    Zeigt Kennzahlen zur Prozessdauer im Streamlit-Interface an.

    Parameter:
        log_df (pandas.Dataframe): Eventlog als Dataframe. Erwartet ein Format, das von 'duration_pro_case' verarbeitet werden kann.

    Rückgabewert:
        Die Funktion gibt keinen Wert zurück, sondern erzeugt Ausgaben im Streamlit-UI.
    """
    st.subheader("⏰ Prozessdauer")
    # Berechnung der Prozessdauer pro Case
    case_duration = duration_process.duration_pro_case(log_df)
    if case_duration is not None:
        avg_case=case_duration["case_duration"].mean()
        st.write("Durchschnittliche Prozessdauer:",second_to_time(avg_case))
        min_case=case_duration["case_duration"].min()
        st.write("Kürzeste Prozessdauer:", second_to_time(min_case))
        max_case=case_duration["case_duration"].max()
        st.write("Längste Prozessdauer:", second_to_time(max_case))