import pandas as pd

def case_duration_outliers(durations, lower1=0.05, upper1=0.95, factor=1.5):
    """Detect outliers in total process duration per case.
    Args:
        durations (pd.DataFrame): DataFrame containing case durations.
        lower1 (float): Lower quantile threshold.
        upper1 (float): Upper quantile threshold.
        factor (float): IQR multiplier to define outlier bounds.
     Returns:
        pd.DataFrame: DataFrame containing outlier cases.
        tuple: Lower and upper bounds for outlier detection.
    """
    log = durations.copy()

    Q1 = log["case_duration"].quantile(lower1)
    Q3 = log["case_duration"].quantile(upper1)

    IQR = Q3 - Q1

    lower = Q1 - factor * IQR
    upper = Q3 + factor * IQR

    outliers = log[(log["case_duration"] < lower) | (log["case_duration"] > upper)]
    return outliers, (lower, upper)
