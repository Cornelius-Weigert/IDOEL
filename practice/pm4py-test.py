import pm4py
log = pm4py.read_xes('practice/running-example.xes')

# Discover the directly follows graph
directly_follows_graph, start_activities, end_activities = pm4py.discover_dfg(log)

# Visualize the DFG
pm4py.view_dfg(directly_follows_graph, start_activities, end_activities)