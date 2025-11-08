import pm4py
import pandas as pd
import matplotlib.pyplot as plt

#.xes Datei lesen （ang. Dateiname ist "event_log.xes"）
log = pm4py.read_xes("event_log.xes")

#log(.xes) -> dataframe(df)
df = pm4py.convert_to_dataframe(log)

#:welche Attribute？
print(df.head())
#z.B. case, activity, timestamp, resource,...

#1
#Häufigkeit analysieren nach event mit dem selben Namen(concept:name)
event = 'concept:name'
haeufigkeit = df[event].value_counts().reset_index()
haeufigkeit.columns = ['Event', 'Häufigkeit']
#Ausgabe Spalten: (von links nach rechts) index, event, Häufigkeit 

#2
#Nummer analysieren 
spalten_mit_nummer = df.select_dtypes(include = 'number').columns
#Durchschnitt und Standardabweichung
if len(spalten_mit_nummer)>0:
    statistik = df.groupby(event)[spalten_mit_nummer].agg(['mean','std']).reset_index()

#1&2 merge
    zusammenfassung = pd.merge(haeufigkeit, statistik, on=event)
else:
    zusammenfassung = haeufigkeit
print(zusammenfassung)

#3
#String analysieren
name = 'org:resource'
for aktivitaet in df[event].unique():
    #alle Zeile mit dieser Aktivität in Dataframe 
    sub = df[df[event]==aktivitaet]
    wieviel = sub[name].value_counts()

    #Diagram erstellen
    plt.figure(figsize=(8,4))
    wieviel.plot(kind = 'bar')

    plt.title(f"Aktivität {aktivitaet} wird von welchen Mitarbeitern durchgeführt" )
    plt.xlabel(name)
    plt.ylabel('Menge')
    
    plt.show()

