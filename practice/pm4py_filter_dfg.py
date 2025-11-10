import pm4py

def threshold_filtered_dfg(dfg,start_activities,end_activities):
    activities_count = pm4py.statistics.attributes.log.get.get_attribute_values(log,'Activity')
    threshold = 50000
    filtered_dfg, filtered_start_activities, filtered_end_activities, new_count = pm4py.algo.filtering.dfg.dfg_filtering.filter_dfg_keep_connected(dfg,start_activities,end_activities,activities_count,threshold)
    pm4py.view_dfg(filtered_dfg, filtered_start_activities, filtered_end_activities, format='svg',graph_title="threshold filtered DFG")

def view_dfg_limited_edges(dfg,start_activities,end_activities):
    max_edges = 45
    pm4py.view_dfg(dfg, start_activities, end_activities,max_num_edges=max_edges,format='svg',graph_title="limited edges DFG")

def path_percentage_filtered_dfg(dfg,start_activities,end_activities):
    percentage = 0.06
    activities_count = pm4py.statistics.attributes.log.get.get_attribute_values(log,'Activity')
    filtered_dfg, filtered_start_activities, filtered_end_activities = pm4py.filtering.filter_dfg_paths_percentage(dfg,start_activities,end_activities,percentage)
    pm4py.view_dfg(filtered_dfg, filtered_start_activities, filtered_end_activities, format='svg',graph_title="path percentage filtered DFG")

def activity_percentage_filtered_dfg(dfg,start_activities,end_activities):
    percentage = 0.05
    activities_count = pm4py.statistics.attributes.log.get.get_attribute_values(log,'Activity')
    filtered_dfg, filtered_start_activities, filtered_end_activities = pm4py.filtering.filter_dfg_paths_percentage(dfg,start_activities,end_activities,percentage)
    pm4py.view_dfg(filtered_dfg, filtered_start_activities, filtered_end_activities, format='svg',graph_title="activity percentage filtered DFG")


log = pm4py.read_xes('Eventlogs/BPI_Challenge_2019.xes')
log2 = pm4py.read_xes('Eventlogs/running-example.xes')

directly_follows_graph, start_activities, end_activities = pm4py.discover_dfg(log)

# pm4py.view_dfg(directly_follows_graph, start_activities, end_activities,format='svg',graph_title="Control DFG")

# try:
#     threshold_filtered_dfg(directly_follows_graph,start_activities,end_activities)
# except Exception as e1:
#     print("Threshold filtering failed:", e1)
# try:
#     view_dfg_limited_edges(directly_follows_graph,start_activities,end_activities)
# except Exception as e2:
#     print("View DFG with limited edges failed:", e2)
# try:
#     path_percentage_filtered_dfg(directly_follows_graph,start_activities,end_activities)
# except Exception as e3:
#     print("Path percentage filtering failed:", e3)
# try:
#     activity_percentage_filtered_dfg(directly_follows_graph,start_activities,end_activities)   
# except Exception as e4:
#     print("Activity percentage filtering failed:", e4)

# path_percentage_filtered_dfg(directly_follows_graph,start_activities,end_activities)
activity_percentage_filtered_dfg(directly_follows_graph,start_activities,end_activities)