

import pandas as pd

# ---------------------------------------
# 1. Case Duration Outliers
# ---------------------------------------
def case_duration_outliers(durations, lower1=0.10, upper1=0.90, factor=1.5):
    """Detect outliers in total process duration per case."""
    log = durations.copy()

    Q1 = log["case_duration"].quantile(lower1)
    Q3 = log["case_duration"].quantile(upper1)
    IQR = Q3 - Q1

    lower = Q1 - factor * IQR
    upper = Q3 + factor * IQR

    outliers = log[(log["case_duration"] < lower) | (log["case_duration"] > upper)]
    return outliers, (lower, upper)
