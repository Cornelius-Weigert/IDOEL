import streamlit as st

def accept_outliers(selected_rows, category,outlier_df,comment,outlier_type):
    """
    Übernimmt vom Nutzer ausgewählte Ausreißer in den Bericht.

    Args:
        selected_rows (list[int]): Liste der Zeilenindizes, die vom Nutzer ausgewählt wurden.
        category (str): Kategorie der Ausreißer.
        outlier_df (pandas.Dataframe): Dataframe mit allen erkannten Ausreißern der Kategorie. 
        comment (str): Kommentar des Nutzers, der allen akzeptierten Ausreißern hinzugefügt wird. 
        outlier_type (str): Typ des Ausreißers.

    Rückgabewert:
        Die Funktion verändert ausschließlich den Session-State und erzeugt UI-Rückmeldungen.     
    """
    if st.session_state.get("outliers_accepted") is None:
        st.session_state["outliers_accepted"] = []
    filtered_outlier_df = outlier_df.iloc[selected_rows]
    filtered_outlier_df["Kommentar"] = comment
    st.session_state["outliers_accepted"].append([category, filtered_outlier_df, outlier_type])
    st.success(f"✅ {len(filtered_outlier_df)} Ausreißer in der Kategorie '{category}' wurden akzeptiert.")
    st.session_state["outlier_accepted"] += len(filtered_outlier_df)