import pandas as pd
def activity_duration_outliers(log_df, duration_col="Activity_Duration", lower1=0.10, upper1=0.90, factor=1.5):
    """Detect outliers in activity durations.
    Args:
        log (pd.DataFrame): DataFrame containing activity durations.
        duration_col (str): Column name for activity durations.
        lower1 (float): Lower quantile threshold.
        upper1 (float): Upper quantile threshold.
        factor (float): IQR multiplier to define outlier bounds.

    Returns:
        pd.DataFrame: DataFrame containing outlier activities.
        tuple: Lower and upper bounds for outlier detection.
     """
    df2 = log_df.copy()

    Q1 = df2[duration_col].quantile(lower1)
    Q3 = df2[duration_col].quantile(upper1)
    IQR = Q3 - Q1

    lower = Q1 - factor * IQR
    upper = Q3 + factor * IQR

    outliers = df2[(df2[duration_col] < lower) | (df2[duration_col] > upper)]
    return outliers, (lower, upper)

