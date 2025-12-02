import pandas as pd

# ---------------------------------------
# 3. Numeric Outliers
# ---------------------------------------
def numeric_outliers(log, value_col,lowerq=0.10, upperq=0.90, factor= 1.5):
    """Detect outliers in any numeric column."""
    Q1 = log[value_col].quantile(lowerq)
    Q3 = log[value_col].quantile(upperq)
    IQR = Q3 - Q1

    lower = Q1 - factor* IQR
    upper = Q3 + factor*IQR

    outliers = log[(log[value_col] < lower) | (log[value_col] > upper)]
    return outliers, (lower, upper)
