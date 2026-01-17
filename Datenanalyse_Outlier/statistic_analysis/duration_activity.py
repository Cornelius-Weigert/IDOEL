import streamlit as st
from .second_to_time import second_to_time
import pandas as pd

# Zwischenspeicherung der Ergebnisse
@st.cache_data
def duration_pro_activity(log_df, case_col="case_id", event_col="activity", time_col="timestamp"):
    """
    Berechnet die Dauer einzelner Aktivitäten innerhalb eines Eventlogs.

    Parameter:
        log (pd.DataFrame): DataFrame mit dem Eventlog.
        case_col (str): Spaltenname für die Case-ID.
        event_col (str): Spaltenname für die Aktivität.
        time_col (str): Spaltenname für den Zeitstempel.

    Rückgabewert:
         pd.DataFrame: Erweiterter DataFrame mit Aktivitätsdauern in Sekunden,
                      lesbare Zeitdarstellung sowie der durchschnittlichen Aktivitätsdauer.
    """
    
    activity_df = log_df.copy()
    # Umwandlung der Zeitstempel
    activity_df[time_col] = pd.to_datetime(activity_df[time_col], errors="coerce")
    activity_df[time_col]=activity_df[time_col].dt.tz_localize(None)
    activity_df = log_df.sort_values(by=[case_col, time_col])
    # Entfernt aufeinanderfolgende doppelte Events innerhalb eines Cases
    activity_df = activity_df[
        ~(
            (activity_df[event_col] == activity_df.groupby(case_col)[event_col].shift(1)) &
            (activity_df[time_col] == activity_df.groupby(case_col)[time_col].shift(1))
        )
    ]
    # Bestimmt den Zeitstempel des nächsten Events innerhalb desselben Cases
    activity_df["next_time"] = activity_df.groupby(case_col)[time_col].shift(-1)
    activity_df["Activity_Duration"] = activity_df["next_time"] - activity_df[time_col]
    activity_df["Activity_Duration"] = activity_df["Activity_Duration"].dt.total_seconds()
    activity_df["Activity_Duration_time"] = activity_df["Activity_Duration"].apply(second_to_time)

    # Berechnung der durchschnittlichen Aktivitätsdauer pro Aktivität
    standard_activity_duration = activity_df.groupby(event_col)["Activity_Duration"].mean().reset_index()
    standard_activity_duration.columns = [event_col, "standard_activity_duration"]
    activity_df = activity_df.merge(
        standard_activity_duration,
        on=event_col,
        how="left"
    )

    return activity_df