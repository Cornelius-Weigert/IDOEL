# ========================
# 3. Häufigkeit Analyse
# ========================
def frequency1(log, event_col="activity"):
    freq = log[event_col].value_counts().reset_index()
    freq.columns = ["Event", "Häufigkeit"]
    return freq
