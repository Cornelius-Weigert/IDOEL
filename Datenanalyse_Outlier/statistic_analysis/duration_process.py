import pandas as pd
# ==========================
# 6. Zeit-Analyse
# =======================

def duration_pro_case(log, case_col="case_id", time_col="timestamp"):

    #Sortieren
    df_sorted = log.sort_values(by=[case_col, time_col])

    #Durchlaufzeit pro Case
    case_duration = df_sorted.groupby(case_col)[time_col].agg(["first", "last"])
    #!!!
    case_duration["case_duration"] = (case_duration["last"] - case_duration["first"]).dt.total_seconds() / 60.0  # (Dauer in Minuten)

    standard_case_duration = pd.DataFrame({case_col: case_duration["case_duration"].mean()}, index=[0])
    case_duration = case_duration.reset_index()



    
   

    return case_duration[[case_col, "case_duration"]]
