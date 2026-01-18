import pm4py
import datetime
import os

def get_dfg_image(log,percentage=0.2):
    """
    Erzeugt aus einem Eventlog im PM4Py-Format ein Directly-Follows-Graph-(DFG)-Diagramm
    und gibt den SVG-Code zur Anzeige zurück.

    Parameter: 
       log: Eventlog im PM4Py-Format
       prozent: Anteil der häufigsten Pfade, die im DFG angezeigt werden sollen

    Rückgabe:
    SVG-Code des generierten DFG-Diagramm als String.
    """

    dfg,sa,ea = pm4py.discover_dfg(log)
    dfg, sa, ea = pm4py.filtering.filter_dfg_paths_percentage(dfg,sa,ea,percentage)
    image_path = 'temp_graphs/'+str(datetime.date.today())+'_dfg.svg'
    pm4py.save_vis_dfg(dfg, sa, ea,image_path)
    with open(image_path,"r",encoding="utf-8") as image_file: svg_code = image_file.read()
    svg_code = svg_code[svg_code.find("<svg"):]
    os.remove(image_path)
    return svg_code

def get_bpmn_image(log, percentage=1):
    """
    Erzeugt aus einem Eventlog im PM4Py-Format ein BPMN-Diagramm
    und gibt den SVG-Code zur Anzeige zurück.

    Parameter:
       log: Eventlog im PM4Py-Format
       prozent: Abdeckung der Varianten, die berücksichtigt werden sollen 

    Rückgabewert: 
       SVG-Code des generierten BPMN-Diagramm als String.
    """ 
    
    log = pm4py.filtering.filter_variants_by_coverage_percentage(log,1-percentage)
    bpmn = pm4py.discover_bpmn_inductive(log)
    image_path = 'temp_graphs/'+str(datetime.date.today())+'_bpmn.svg'
    pm4py.save_vis_bpmn(bpmn,image_path)
    with open(image_path,"r",encoding="utf-8") as image_file: svg_code = image_file.read()
    svg_code = svg_code[svg_code.find("<svg"):]
    os.remove(image_path)
    return svg_code