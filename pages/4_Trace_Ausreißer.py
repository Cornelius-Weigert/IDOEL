# Abhängigkeiten importieren 
import streamlit as st 
from Datenanalyse_Outlier.display_analysis.outlier_trace import show_trace_outliers


# Session State initialisieren
if st.session_state.get("df") is None:
    st.warning("⚠️ Bitte zuerst einen Eventlog auf der \"Upload Eventlog\" Seite hochladen.")
    st.stop()

df = st.session_state.get("df")
log = st.session_state.get("log")

show_trace_outliers(df)