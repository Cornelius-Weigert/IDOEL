import pandas as pd

def case_duration_outliers(durations, lower1=0.05, upper1=0.95, factor=1.5):
    """
    Identifiziert Ausreißer in der Gesamtdurchlaufzeit von Cases auf Basis der Interquartilsabstand-Methode (IQR).

    Parameter:
        durations (pd.DataFrame): Dataframe mit Case-Dauern.
        lower1 (float): Unteres Quantil zur Berechnung des IQR.
        upper1 (float): Oberes Quantil zur Berechnung des IQR.
        factor (float): Multiplikator des IQR zur Festlegung der Ausreißergrenzen.

     Rückgabewert:
        pd.DataFrame: DataFrame mit allen als Ausreißer erkannten Cases.
        tuple: Untere und obere Grenze der Ausreißererkennung.
    """
    
    log = durations.copy()

    Q1 = log["case_duration"].quantile(lower1)
    Q3 = log["case_duration"].quantile(upper1)

    IQR = Q3 - Q1

    lower = Q1 - factor * IQR
    upper = Q3 + factor * IQR

    outliers = log[(log["case_duration"] < lower) | (log["case_duration"] > upper)]
    return outliers, (lower, upper)
