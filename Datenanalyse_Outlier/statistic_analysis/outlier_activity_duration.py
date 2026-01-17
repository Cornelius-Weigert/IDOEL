import pandas as pd

def activity_duration_outliers(log_df, duration_col="Activity_Duration", lower1=0.05, upper1=0.95, factor=1.5):
    """
    Identifziert Ausreißer in den Aktivitätsdauern eines Eventlogs auf Basis der Interquartilsabstand-Methode (IQR).

    Parameter:
        log (pd.DataFrame): Dataframe mit Aktivitätsdauern.
        duration_col (str): Spaltenname der Aktivitätsdauer (in Sekunden).
        lower1 (float): Unteres Quantil zur Berechnung des IQR.
        upper1 (float): Oberes Quantil zur Berechnung des IQR.
        factor (float): Multiplikator des IQR zur Festlegung der Ausreißergrenzen.

    Rückgabewert:
        pd.DataFrame: DataFrame mit allen als Ausreißer erkannten Aktivitäten.
        tuple: Untere und obere Grenze der Ausreißererkennung.
    """
    
    df2 = log_df.copy()

    Q1 = df2[duration_col].quantile(lower1)
    Q3 = df2[duration_col].quantile(upper1)
    IQR = Q3 - Q1

    lower = Q1 - factor * IQR
    upper = Q3 + factor * IQR

    outliers = df2[(df2[duration_col] < lower) | (df2[duration_col] > upper)]
    return outliers, (lower, upper)

