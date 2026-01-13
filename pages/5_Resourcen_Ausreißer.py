# Abhängigkeiten importieren 
import streamlit as st
from Datenanalyse_Outlier.display_analysis.outlier_resource import show_resource_outliers


# Session State initialisieren
if st.session_state.get("df") is None:
    st.warning("⚠️ Bitte zuerst einen Eventlog auf der \"Upload Eventlog\" Seite hochladen.")
    st.stop()

df = st.session_state.get("df")

# Anzeige der ressourenbezogenen Ausreißer 
show_resource_outliers(df)