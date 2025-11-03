import pm4py
log = pm4py.read_xes('C:/Users/Corne/Dokumente/studium/Semester 5/SWPS/practice/running-example.xes')

# Discover the directly follows graph
directly_follows_graph, start_activities, end_activities = pm4py.discover_dfg(log)
bpmn= pm4py.discover_bpmn_inductive(log)
# Visualize the DFG
pm4py.view_dfg(directly_follows_graph, start_activities, end_activities,format='svg',graph_title="Directly Follows Graph")
pm4py.view_bpmn(bpmn,format='svg',graph_title="Hello World BPMN")