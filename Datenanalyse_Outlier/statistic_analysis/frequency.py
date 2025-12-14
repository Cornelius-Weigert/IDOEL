def frequency1(log_df, event_col="activity"):
    """
    Calculate the frequency of each event in the log.
    Args:
        log_df (pd.DataFrame): DataFrame containing the event log.
        event_col (str): Column name for events.
    Returns:
        pd.DataFrame: DataFrame with event frequencies.
    """
    freq = log_df[event_col].value_counts().reset_index()
    freq.columns = ["Event", "Häufigkeit"]
    return freq