import pandas as pd

def temporal_outliers(log, case_col="case_id", activity_col="activity", timestamp_col="timestamp"):
    """
    Identifiziert zeitliche Ausreißer in einem Ereignisprotokoll basierend auf der Dauer zwischen aufeinanderfolgenden Aktivitäten.

    Parameter:
    log (pd.DataFrame): Das Ereignisprotokoll als DataFrame.
    case_col (str): Name der Spalte für Fall-IDs.
    timestamp_col (str): Name der Spalte für Zeitstempel.

    Rückgabe:
    pd.DataFrame: DataFrame mit den identifizierten zeitlichen Ausreißern.
    """
    log = log.copy()
    log[timestamp_col] = pd.to_datetime(log[timestamp_col], errors='coerce')
    
    #duration rechennen
    log = log.sort_values(by=[case_col, timestamp_col])
    log['prev_timestamp'] = log.groupby(case_col)[timestamp_col].shift(1)
    log['duration'] = (log[timestamp_col] - log['prev_timestamp']).dt.total_seconds() / 60.0  # Dauer in Minuten 

    # Durchschnittliche Dauer pro Aktivität berechnen und anzeigen
    standard = log.groupby(activity_col)['duration'].mean().reset_index()
    standard.columns = [activity_col, 'standard_activity_duration']
    log = log.merge(standard, on=activity_col, how='left')
    
    outliers = {}
    
    #+++++Wenn die timestamp in Zukunft liegt++++++++++++++
    now = pd.Timestamp.now(tz="Europe/Berlin")
    future_rows = log[log[timestamp_col] > now]
    outliers['future-timestamp'] = future_rows.index.tolist()

    
    #+++++++Wenn Timestamp fehlt+++++++++++++++++++++++++
    missing_timestamp_rows = log[log[timestamp_col].isnull()]
    outliers['missing-timestamp'] = missing_timestamp_rows.index.tolist()  



    #++++++++Wenn die Dauer zwischen Aktivitäten ungewöhnlich lang ist+++++++++++++
    #outliers = {}



    #lange Dauer
    long_duration_threshold = log['duration'].quantile(0.95)  # 95. Perzentil als Schwellenwert
    long_duration_rows = log[log['duration'] > long_duration_threshold]
    outliers['long-activity-duration'] = long_duration_rows.index.tolist()


    #++++++++Wenn die Dauer zwischen Aktivitäten ungewöhnlich kurz ist+++++++++++++
    short_duration_threshold = log['duration'].quantile(0.05)  #
    short_duration_rows = log[log['duration'] < short_duration_threshold]
    outliers['short-activity-duration'] = short_duration_rows.index.tolist() 

    #+++++++Wenn Timestamp vor dem vorherigen Timestamp liegt+++++++++++++
    negative_duration_rows = log[log['duration'] < 0]
    outliers['negative-activity-duration'] = negative_duration_rows.index.tolist()



    # Nur relevante Spalten für die Anzeige behalten
    display_cols = [case_col, activity_col, timestamp_col, 'prev_timestamp', 'duration','standard_activity_duration']
    log = log[display_cols]

    return outliers,log

