import streamlit as st
from Datenanalyse_Outlier import eventlog_to_image as eventlog_to_image
from Datenanalyse_Outlier import load_eventLog as load_eventLog 
from Datenanalyse_Outlier.display_analysis.outlier_trace import show_trace_outliers


# --- SESSION STATE INITIALISIEREN ---
if st.session_state.get("df") is None:
    st.warning("⚠️ Bitte zuerst einen Eventlog auf der \"Upload Eventlog\" Seite hochladen.")
    st.stop()

df = st.session_state.get("df")
log = st.session_state.get("log")

show_trace_outliers(df)