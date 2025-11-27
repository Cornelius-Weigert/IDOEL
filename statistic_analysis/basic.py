
# ===================
# 2. Basis-Analyse
# ===================
def basic_analysis(log):
    print("->>>Verfügbare Spalten:", list(log.columns))
    print("\n->>> Kopf der Daten:")
    print(log.head())
    print("\n------------------------")
