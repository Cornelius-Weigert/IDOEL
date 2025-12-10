import pandas as pd


def outlier_resources(log, case_col="case_id", activity_col="activity", resource_col="resource"):
    
    # Resource-Activity
    counts = log.groupby(resource_col)[activity_col].count().reset_index()
    counts.columns = [resource_col, "activity_count"]

    # count auch im log mergen
    log_with_counts = log.merge(counts, on=resource_col, how="left")

    outliers = {

    }

    #+++++++Wenn die Ressource fehlt+++++++++++++++++++++++++
    missing_resource_rows = log[log[resource_col].isnull()]
    outliers['missing-resource'] = missing_resource_rows.index.tolist() 

    
    #+++++++Wenn eine Ressource ungewöhnlich viele Aktivitäten hat+++++++++++++
    activity_counts = log[resource_col].value_counts()
    threshold = activity_counts.quantile(0.95)  # 95. Perzentil als Schwellenwert

    high_activity_resources = activity_counts[activity_counts > threshold].index
    high_activity_rows = log[log[resource_col].isin(high_activity_resources)]
    outliers['high-activity-resources'] = high_activity_rows.index.tolist()   

    #+++++++Wenn eine Ressource ungewöhnlich wenige Aktivitäten hat+++++++++++++
    threshold1 = activity_counts.quantile(0.05)  # 5. Perzentil als Schwellenwert
    low_activity_resources = activity_counts[activity_counts < threshold1].index
    low_activity_rows = log[log[resource_col].isin(low_activity_resources)]
    outliers['low-activity-resources'] = low_activity_rows.index.tolist()   



    #+++++++Wenn eine Resource viele verschiedene Aktivitäten ausführt+++++++++++++
    resource_activity_counts = log.groupby(resource_col)[activity_col].nunique()
    diverse_activity_resources = resource_activity_counts[resource_activity_counts > resource_activity_counts.quantile(0.95)].index
    diverse_activity_rows = log[log[resource_col].isin(diverse_activity_resources)]
    outliers['many-activity-resources'] = diverse_activity_rows.index.tolist()   


    
    return outliers,log_with_counts
