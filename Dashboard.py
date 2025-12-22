import streamlit as st

st.set_page_config(page_title="Dashboard", layout="wide")

# Session state auf leer setzen, wenn Seite gestartet wird 
if "uploaded_logs" not in st.session_state:
    st.session_state["uploaded_logs"] = []

if "outlier_accepted" not in st.session_state:
    st.session_state["outlier_accepted"] = 0

if "outlier_checked" not in st.session_state:
    st.session_state["outlier_checked"] = False

if "latest_upload" not in st.session_state:
    st.session_state["latest_upload"] = None

# --- Kopfzeile ---
st.title("🏠 Dashboard")
st.write("Übersicht zur interaktiven Detektion von Ausreißern in Eventlogs")

# --- Spalten ---
col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Hochgeladene Logs",
         len(st.session_state.get("uploaded_logs", [])))

with col2:
    st.metric(
        "Ausreißer gefunden",
        st.session_state["outlier_accepted"]
    )

with col3:
    st.metric("Letzter Upload", st.session_state["latest_upload"] or "Keine Uploads")

st.markdown("---")

# --- Neueste Aktivitäten ---
st.subheader("📝 Neueste Aktivitäten")

if st.session_state["uploaded_logs"]:
    for log in reversed(st.session_state["uploaded_logs"][-5:]):
        st.write(f"- 📂 {log}")
else:
    st.write("Keine Aktivitäten bisher.")