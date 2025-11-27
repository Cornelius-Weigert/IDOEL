# ==========================
# 7. Standardwerte-Vergleich
# =======================
def compare_with_standardwert(log, standard, event_col="concept:name", value_col="value"):
    if value_col not in log.columns:
        print("->>> Keine Spalte für Standardwert-Vergleich gefunden:", value_col)
        return

   #Standard Spalte hinzufügen
    log["Standardwert"] =log[event_col].map(standard)
   #Abweichung hinzufügen
    log["Abweichung"] = log[value_col] - log["Standardwert"]

    print("->>>Standardwert-Vergleich abgeschlossen")
    return log[[event_col, value_col, "Standardwert", "Abweichung"]]
