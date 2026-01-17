import pandas as pd
import streamlit as st
from .second_to_time import second_to_time

# Zwischenspeichern der berechneten Case-Dauern
@st.cache_data
def duration_pro_case(log_df, case_col="case_id", time_col="timestamp"):
    """
    Berechnet die Gesamtdurchlaufzeit für jeden Case.

    Parameter:
        log (pd.DataFrame): Dataframe mit dem Eventlog.
        case_col (str): Spaltenname für die Case-ID.
        time_col (str): Spaltenname für den Zeitstempel.

    Rückgabewert:
        pd.DataFrame: Dataframe mit der Case-Dauer in Sekunden.
    """

    # Sortieren des Eventlogs nach Case-ID und Zeitstempel 
    df_sorted = log_df.sort_values(by=[case_col, time_col])

    # Durchlaufzeit pro Case
    case_duration = df_sorted.groupby(case_col)[time_col].agg(["first", "last"])
    case_duration["case_duration"]=(case_duration["last"]- case_duration["first"])
    # Umwandlung der Durchlaufzeit in Sekunden
    case_duration["case_duration"] = (case_duration["last"] - case_duration["first"]).dt.total_seconds()
    case_duration = case_duration.reset_index()
    case_duration["case_duration_time"]=(case_duration["case_duration"].apply(second_to_time))

    return case_duration[[case_col, "case_duration","case_duration_time"]]