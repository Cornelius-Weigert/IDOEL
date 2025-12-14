
import pandas as pd
def compare_with_standardwert(log_df, standard, event_col="activity", value_col="value"):
    """
    Compare values in the log with standard values.
    Args:
        log (pd.DataFrame): DataFrame containing the event log.
        standard (dict or numeric): Standard values per event or a single standard value.
        event_col (str): Column name for events.
        value_col (str): Column name for values to compare.
    Returns:
        pd.DataFrame: DataFrame with original values, standard values, and deviations.
    """

    if value_col not in log_df.columns:
        return pd.DataFrame()

    if isinstance(standard,(int, float, pd.Timedelta)):
        log_df["Standardwert"]=standard 
    else:
        if event_col is not None:
            log_df["Standardwert"] = log_df[event_col].map(standard)
       

    log_df["Abweichung"] = log_df[value_col] - log_df["Standardwert"]

    return log_df[[value_col, "Standardwert", "Abweichung"]]


    











