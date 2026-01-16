import streamlit as st
from ..statistic_analysis.duration_activity import duration_pro_activity
from ..statistic_analysis.second_to_time import second_to_time

def show_activity_duration(log_df):
    """
    Zeigt statistische Kennzahlen zur Dauer von Aktivitäten an.

    Parameter:
        log_df (pandas.Dataframe): Eventlog als Dataframe. Erwartet mindestens die Spalten:
                                   - activity
                                   - Activity_Duration (in Sekunden)

    Rückgabewert:
    Die Funktion gibt keinen Wert zurück, sondern erzeugt UI-Komponenten in Streamlit.
    """
    st.subheader("⌚️Aktivitätsdauer")

    # Berechnung der Ausführungsdauer pro Aktivität
    act = duration_pro_activity(log_df)
   
    # Berechnung von Mittelwert, Minimum und Maximum der Aktivitätsdauer 
    act_summary = act.groupby("activity")["Activity_Duration"].agg(['mean', 'min', 'max']).reset_index()
    for col in ["mean","min","max"]:
        act_summary[col]=act_summary[col].apply(second_to_time)
    st.subheader("📈 Zusammenfassung pro Aktivität")
    st.dataframe(act_summary)

