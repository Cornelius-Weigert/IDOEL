import streamlit as st

def show_resources(log_df, resource_col="resource"):
    """
    Zeigt eine Analyse der Ressourcennutzung im Streamlit-Interface an.

    Parameter:
        log_df (pandas.DataFrame): Eventlog als Dataframe.
        resource_col (str): Name der Rressourcenspalte im Dataframe.
    Rückgabewert:
        Erzeugt UI-Elemente zur Analyse der Ressourcennutzung.
    """
    st.subheader("👥 Ressourcen Analyse")

    if resource_col not in log_df.columns:
        st.info("Keine Ressourcenspalte gefunden.")
        return
    
    activities = log_df["activity"].unique()
    selected = st.selectbox("Aktivität wählen", activities)

    sub = log_df[log_df["activity"] == selected]
    counts = sub["resource"].value_counts()

    st.bar_chart(counts, sort=False) 

    log_with_counts = log_df.groupby("resource").agg(activity_count=("activity", "count")).reset_index()

    st.subheader("📊 Ereignisse pro Ressource")

    st.bar_chart(log_with_counts, x="resource", y="activity_count")       