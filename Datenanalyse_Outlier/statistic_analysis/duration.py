#=======================
#Benötige Zeit pro Aktivität
#========================

def duration_pro_activity(log, case_col="case_id", event_col="activity", time_col="timestamp"):
    if time_col not in log.columns:
        print("->>>Keine Timestamp - Aktivitätsdauer Analyse übersprungen.")
        return None

    df_sorted = log.sort_values(by=[case_col, time_col]).copy()

    #next timestamp
    df_sorted["next_time"] = df_sorted.groupby(case_col)[time_col].shift(-1)
    #duration
    df_sorted["Activity_Duration"] = df_sorted["next_time"] - df_sorted[time_col]
    #durchschnitt
    durations = df_sorted.groupby(event_col)["Activity_Duration"].mean().reset_index()
    print("\n->>> Durchschnittliche Dauer pro Aktivität:")
    print(durations)

    result = df_sorted[[event_col, "Activity_Duration"]].dropna()

    return result
