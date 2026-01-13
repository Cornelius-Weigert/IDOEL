# Abhängigkeiten importieren
import streamlit as st
from Datenanalyse_Outlier.display_analysis.outlier_temporal import show_temporal_outliers

# Sicherheitscheck falls noch kein Eventlog geladen wurde
if st.session_state.get("df") is None:
    st.warning("⚠️ Bitte zuerst einen Eventlog auf der \"Upload Eventlog\" Seite hochladen.")
    st.stop()

# Laden des Eventlogs aus dem Session State
df = st.session_state.get("df")

# Sonstige Session States für Ausreißer
outlier_total = st.session_state.get("outlier_total")
outlier_checked = st.session_state.get("outlier_checked")  
outliers_accepted = st.session_state.get("outliers_accepted")

# Anzeige der zeitlichen Ausreißer
show_temporal_outliers(df)