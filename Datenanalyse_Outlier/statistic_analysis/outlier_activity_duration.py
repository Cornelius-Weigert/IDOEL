import pandas as pd

# ---------------------------------------
# 2. Activity Duration Outliers
# ---------------------------------------
def activity_duration_outliers(log, duration_col="Activity_Duration", lower1=0.10, upper1=0.90, factor=1.5  ):
    """Detect outliers in activity durations."""
    df2 = log.copy()

    # # convert timedelta to minutes
    # df2["duration_col"] = df2[duration_col].dt.total_seconds() / 60.0

    Q1 = df2[duration_col].quantile(lower1)
    Q3 = df2[duration_col].quantile(upper1)
    IQR = Q3 - Q1

    lower = Q1 - factor * IQR
    upper = Q3 + factor * IQR

    outliers = df2[(df2[duration_col] < lower) | (df2[duration_col] > upper)]
    return outliers, (lower, upper)

