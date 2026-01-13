# Abhängigkeiten importieren
import streamlit as st
from Datenanalyse_Outlier.display_analysis.frequency import show_frequency
from Datenanalyse_Outlier.display_analysis.duration_process import show_process_duration
from Datenanalyse_Outlier.display_analysis.resources import show_resources
from Datenanalyse_Outlier.display_analysis.duration_activity import show_activity_duration
from Datenanalyse_Outlier.display_analysis.standard_value import show_standard_compare
from Datenanalyse_Outlier.display_analysis.duration_process import show_process_duration

# Session State initialisieren 
if st.session_state.get("df") is None:
    st.warning("⚠️ Bitte zuerst einen Eventlog auf der \"Upload Eventlog\" Seite hochladen.")
    st.stop()

df = st.session_state.get("df")

# Tabs anzeigen (von links nach rechts)
tab1, tab2, tab3, tab4,tab5 = st.tabs([
    "Häufigkeit",
    "Prozessdauer",
    "Aktivitätsdauer",
    "Standardwerte-Vergleich",
    "Ressourcen",])

with tab1:
    show_frequency(df)
    
with tab2:
    show_process_duration(df)

with tab3:
    show_activity_duration(df)

with tab4:
    show_standard_compare(df)

with tab5:
    show_resources(df)