import pandas as pd

def frequency1(log_df, event_col="activity"):
    """
    Berechnet die absolute Häufigkeit jeder Aktivität im Eventlog.

    Parameter:
        log_df (pd.DataFrame): DataFrame mit dem Eventlog.
        event_col (str): Spaltenname für die AKtivität.

    Rückgabewert:
        pd.DataFrame: DataFrame mit den Spalten "Event" und "Häufigkeit".
    """

    freq = log_df[event_col].value_counts().reset_index()
    freq.columns = ["Event", "Häufigkeit"]
    return freq

def frequency_unique(log_df, event_col="activity", case_col="case_id"):
    """
    Berechnet die Anzahl der Cases, in denen eine Aktivität mindestens einmal vorkommt.

    Parameter:
        log_df (pd.Dataframe): Dataframe mit dem Eventlog.
        event_col (str, optional): Spaltenname für die AKtivität. 
        case_col (str, optional): Spaltenname für die Case-ID.

    Rückgabewert:
        pd.Dataframe: Dataframe mit den Spalten "Event" und "Unique_Häufigkeit".
    """

    unique_freq = log_df.groupby(event_col)[case_col].nunique().reset_index()
    unique_freq.columns = ["Event", "Unique_Häufigkeit"]
    return unique_freq

