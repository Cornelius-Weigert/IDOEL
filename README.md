# IDOEL 🔍 – Interactive Detection of Outliers in Event Logs

> **"Garbage in, Garbage out."** IDOEL schließt die Lücke zwischen automatischer Ausreißer-Erkennung und menschlichem Domänenwissen im Process Mining.

---

## 📖 Über das Projekt

In der Praxis scheitern Process-Mining-Analysen oft an mangelnder Datenqualität. Herkömmliche Algorithmen zur Ausreißer-Erkennung agieren oft als "Blackbox" und löschen Datenpunkte rein statistisch, ohne den geschäftlichen Kontext zu verstehen.

**IDOEL (Interactive Detection of Outliers in Event Logs)** ist eine interaktive Webanwendung, die einen **Human-in-the-Loop-Ansatz** verfolgt. Sie ermöglicht es Domänenexperten, potenzielle Ausreißer systematisch zu validieren und so die Qualität der Inputdaten für das Process Mining nachhaltig zu steigern.

### Kernfunktionen
* **Interaktiver Upload:** Einfacher Import von Event Logs (CSV/XES).
* **Geführte Detektion:** Automatisierte Identifikation potenzieller Anomalien.
* **Experten-Validierung:** Intuitive UI zur Entscheidung über das Vorhandensein von Ausreißern.
* **Daten-Reparatur:** Export der validierten Ausreißer.


## 🚀 Quick Start

### Voraussetzungen
Stelle sicher, dass Python 3.9+ installiert ist.

### Installation
1. Repository klonen:
   ```bash
   git clone [https://github.com/Cornelius-Weigert/SWPS.git](https://github.com/Cornelius-Weigert/IDOEL.git)
   cd IDOEL

2. Abhängigkeiten installieren:
   ```bash
   pip install pm4py pandas streamlit

3. Anwendung starten
Starte die Streamlit-App mit folgendem Befehl:
    ```bash
    streamlit run Dashboard.py

## 🧬 Workflow in IDOEL

1. **Input:** Hochladen des Event Logs.
2. **Highlighting:** Markierung von Traces/Events mit hoher Ausreißer-Wahrscheinlichkeit.
3. **Human Decision:** Der Experte kann Ausreißer bestätigen und einen Kommentar ergänzen.
4. **Output:** Download der durch den Experten validierten Ausreißer.


## 📑 Inhalt der Pages

Das Framework ist modular aufgebaut. Die einzelnen Schritte können über die Sidebar angesteuert werden:

* **[1_Eventlog_Upload.py](./pages/1_Eventlog_Upload.py):** Zentraler Einstiegspunkt für den Import von Event Logs (CSV/XES) und die initiale Datenaufbereitung.
* **[2_Deskriptive_Analyse.py](./pages/2_Deskriptive_Analyse.py):** Übersicht über grundlegende Prozesskennzahlen wie Fallanzahl, Varianten und Aktivitätsstatistiken.
* **[3_Zeitliche_Ausreißer.py](./pages/3_Zeitliche_Ausreißer.py):** Untersuchung von Durchlaufzeiten, Engpässen und zeitlichen Mustern im Prozessverlauf.
* **[4_Trace_Ausreißer.py](./pages/4_Trace_Ausreißer.py):** Identifikation und interaktive Validierung von anomalen Prozesspfaden (Varianten-Ebene).
* **[5_Resource_Ausreißer.py](./pages/5_Resource_Ausreißer.py):** Analyse von untypischem Ressourcenverhalten und unüblichen Akteur-Aktivitäts-Kombinationen.
* **[6_Bericht.py](./pages/6_Bericht.py):** Zusammenfassung der Bereinigungsergebnisse und Export des optimierten Event Logs.

## 🛠 Tech-Stack

* **Backend:** Python
* **Frontend:** [Streamlit](https://streamlit.io/) (Web-Framework)
* **Datenverarbeitung:** Pandas, PM4Py (Process Mining for Python)
