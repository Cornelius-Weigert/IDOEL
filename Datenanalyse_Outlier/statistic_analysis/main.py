# ###################################
# #diese main-Methode ist nicht benötigt
# ######################################

# # from reader import read_event_log
# # from basic import basic_analysis
# # import numeric
# import resources
# import Datenanalyse_Outlier.statistic_analysis.duration_process as duration_process
# from Datenanalyse_Outlier.statistic_analysis.duration_activity import duration_pro_activity
# from standard_compare import compare_with_standardwert
# from outlier_activity_duration import activity_duration_outliers
# from outlier_case_duration import case_duration_outliers
# # from outlier_numeric import numeric_outliers
# import pandas as pd
# from frequency import frequency1 as frequency


# def full_log_analysis(path):
#     #Datei einlesen
#     df = read_event_log(path)

#     #basisanalyse
#     basic_analysis(df)

#     #Häufigkeit
#     freq = frequency(df)
#     print("\n->>>Häufigkeit der Events:")
#     print(freq)

#     #Nummer analyse
#     numeric_stats = numeric(df)
#     if numeric_stats is not None:
#         print("\n->>> Numerische Statistik:")
#         print(numeric_stats)
#         merged = pd.merge(freq, numeric_stats, left_on="Event", right_on="concept:name", how="left")
#     else:
#         merged = freq

#     print("\n->>> Zusammenfassung:")
#     print(merged)

#     # Ressourcenanalyse (mit Plot)
#     print("\n->>> Erstelle Ressourcen-Diagramme…")
#     if "org:resource" in df.columns:
#         resources(df)
#     else:
#         print("->>> Keine Ressourcenspalte (`org:resource`) gefunden.")

#     # Zeit-Analyse
#     duration_process(df)

#     #Aktivitätdauer
#     activity_durations = duration_pro_activity(df)

#     #Outlier Analyse
#     # -------- Outlier Detection --------
#     print("\n==== OUTLIER ANALYSIS ====")

#     # 1. Case Duration Outliers
#     case_outliers, case_bounds = case_duration_outliers(duration_process(df))
#     print("\n->>> Case Duration Outliers:")
#     print(case_outliers)

#     # 2. Activity Duration Outliers
#     activity_outliers, activity_bounds = activity_duration_outliers(activity_durations)
#     print("\n->>> Activity Duration Outliers:")
#     print(activity_outliers)

#     # 3. Numeric Outliers (if value column exists)
#     if "value" in df.columns:
#         value_outliers, value_bounds = numeric_outliers(df, "value")
#         print("\n->>> Numeric Outliers (value):")
#         print(value_outliers)


#     #Standardwer-Vergleich
    


# #++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# df = full_log_analysis("Eventlogs/event_log.xes")  # oder CSV
