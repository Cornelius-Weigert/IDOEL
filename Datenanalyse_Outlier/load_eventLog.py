import pandas as pd
import pm4py

def eventLog_from_csv(path, separator=',', case_id='Case ID', activity_key='Activity', timestamp_key='Complete Timestamp'):
    """
    Lädt einen Eventlog aus einer CSV-Datei und konvertiert es in das PM4Py-Eventlog-Format. 
       
    Parameter: 
        path (str): Dateipfad zur CSV-Datei
        separator (str): Spaltentrennzeichen der CSV-Datei
        case_id (str): Spaltenname der Case-ID
        activity_key (str): Spaltenname der Aktivität
        timestamp_key (str): Spaltenname des Zeitstempels

    Rückgabewert: 
       Diese Funktion gibt den Eventlog im PM4Py Format zurück.
    """
    
    dataframe = pd.read_csv(path, sep=separator)
    dataframe = pm4py.format_dataframe(dataframe, case_id=case_id, activity_key=activity_key, timestamp_key=timestamp_key)
    log = pm4py.convert_to_event_log(dataframe)
    return log

def eventLog_from_xes(path):
    """
    Lädt einen Eventlog aus einer XES-Datei.

    Parameter: 
       path (str): Dateipfad der XES-Datei

    Rückgabe:
       Diese Funktion gibt den Eventlog im PM4Py zurück
    """
    
    log = pm4py.read_xes(path)
    return log