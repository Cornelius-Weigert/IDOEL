import streamlit as st
from ..statistic_analysis.outlier_resource import outlier_resources
from.description import OUTLIER_DESCRIPTIONS
import pandas as pd

if "resource_outliers_accepted" not in st.session_state or not isinstance(
    st.session_state["resource_outliers_accepted"], dict):
    st.session_state["resource_outliers_accepted"] = {}

if "outlier_accepted" not in st.session_state:
    st.session_state["outlier_accepted"] = 0
if "refresh_bericht" not in st.session_state:
     st.session_state["refresh_bericht"]=[]        

@st.fragment
def render_single_resource(category, resource, resource_df,label, value):
    """
    Rendert einen einzelnen Ressourcen-Ausreißer als Streamlit-Fragment.

    Parameter:
        category (str): Kategorie des Ressourcen-Ausreißers.
        resource (str): Name der Ressource.  
        resource_df (pandas.Dataframe): Alle Events der Ressource, die als Ausreißer identifiziert wurden. 
        label (str): Beschreibung des angezeigten Kernwerts.
        value (int): Kennwert der Ressource.

    Rückgabewert:
        Die Funktion erzeugt UI-Elemente und verändert den Session-State. 
    """

    with st.expander(f"👤 Ressource:{resource} | {label} {value}"):
        st.dataframe(resource_df[
                ["case_id","activity","resource"]]
            , width="stretch",hide_index=True)
        # Ressource-Aktivität Verteilung Visualisierung, wenn ein Button geklickt wird
        activity_counts = (resource_df.groupby("activity").size().reset_index(name="count"))
        st.caption("📊 Aktivitätsverteilung dieser Ressource")
        st.bar_chart(activity_counts.set_index("activity")["count"])
        # Akzeptieren Button für Ausreißer
        comment = st.text_area("(Optional) Kommentar zu diesem Ausreißer eingeben",key=f"comment_resource_{category}_{resource}")
        accept_comment = st.button("Kommentar bestätigen & Ausreißer akzeptieren", key=f"confirm_accept_resource_{category}_{resource}")
        if accept_comment:
            
            df_copy=resource_df.copy()
            df_copy["Kommentar"] = comment
        
            if category in st.session_state["resource_outliers_accepted"]:
                st.session_state["resource_outliers_accepted"][category] = pd.concat(
                    [st.session_state["resource_outliers_accepted"][category], df_copy],
                    ignore_index=True
                )
            else:
                st.session_state["resource_outliers_accepted"][category] = df_copy


            st.session_state["outlier_accepted"] += 1
            st.success(f"✅ Ausreißer für Ressource '{resource}' in der Kategorie '{category}' wurde akzeptiert.")
            st.session_state["refresh_bericht"]=not st.session_state.get("refresh_bericht",False)

def show_resource_outliers(log_df):
    """
    Zeigt eine Ressourcen-basierte Ausreißeranalyse im Streamlit-Interface an.

    Parameter: 
        log_df (pd.DataFrame): Eventlog als Dataframe. Erwartet mindestens die Spalten
        'case_id', 'activity', 'resource' und 'timestamp'.

    Rückgabewert:
        Die Funktion erzeugt UI-Elemente und verändert den Session-State.
    """
    
    st.subheader("🌟 Filter - Resource_Activity Value")
    show_res_slider = st.checkbox("Perzentilebasierte Grenzwerte anzeigen ", value = False,key="resource_slider")
    lower_res = st.session_state.get('lower_res') #= 0.05
    upper_res = st.session_state.get('upper_res') #= 0.95
    upper_res_diverse=st.session_state.get('upper_res_diverse')
    factor_res = st.session_state.get('factor_res') #= 1.5

    if show_res_slider:   
        st.write("Perzentilebasierte Grenzenwerte(Anzahl durchgefürten Aktivitäten pro Resource) ")
        lower_res = st.slider("Untere Grenze (Ressource-wenig-aktiv)", 0.0, 0.5, lower_res, 0.01,help="Bestimmt das untere Perzentil der Anzahl ausgeführter Aktivitäten pro Ressource. Ressourcen unterhalb dieses Werts werden als potenzielle Ausreißer mit ungewöhnlich geringer Aktivitätsauslastung betrachtet.")
        upper_res = st.slider("Obere Grenze (Ressource-sehr-aktiv)", 0.5, 1.0, upper_res, 0.01,help="Bestimmt das obere Perzentil der Anzahl ausgeführter Aktivitäten pro Ressource. Ressourcen oberhalb dieses Werts werden als potenzielle Ausreißer mit ungewöhnlich hoher Aktivitätsauslastung betrachtet.")
        upper_res_diverse=st.slider("Obere Grenze (Ressource-vielfältige-Aktivitäten)",0.5,1.0,upper_res_diverse,0.01,help="Legt das Perzentil fest, ab dem Ressourcen als Ausreißer gelten, weil sie eine ungewöhnlich große Anzahl unterschiedlicher Aktivitäten ausführen. Beispiel: 0,95 bedeutet, dass nur die 5 % der Ressourcen mit der höchsten Aktivitätsvielfalt als Ausreißer markiert werden.")
        factor_res = st.slider("Faktor (Ressource)", 1.0, 5.0,factor_res, 0.1,help="Multiplikativer Faktor zur Feinjustierung der Ausreißererkennung. Höhere Werte führen zu einer strengeren, niedrigere Werte zu einer sensibleren Identifikation von Ausreißern. (Ein häufig verwendeter Faktor ist 1,5)")
        
        st.session_state['lower_res'] = lower_res
        st.session_state['upper_res'] = upper_res
        st.session_state['factor_res'] = factor_res
        st.session_state['upper_res_diverse']=upper_res_diverse

    display_cols=["case_id","activity","resource","timestamp"]

    outliers,log_with_counts = outlier_resources(log_df)

    resource_activity_count = log_df.groupby("resource").size().reset_index(name="resource_activity_count")
    resource_unique_activity_counts = log_df.groupby("resource")["activity"].nunique().reset_index(name="unique_activity_count")

    for category, indices in outliers.items():
        st.write(f"### Kategorie: {category}")

        if category in OUTLIER_DESCRIPTIONS:
            st.caption(OUTLIER_DESCRIPTIONS[category]["description"])

        if not indices:
            st.write("Keine Ausreißer in dieser Kategorie gefunden.")
            continue

        if category == "Ressource_vielfältige_Aktivitäten":
            temp_df= log_df.loc[indices, display_cols]
            outlier_df= temp_df.merge(resource_unique_activity_counts,on="resource", how="left")
            temp_col="unique_activity_count"
            label="Anzahl unterschiedlicher Aktivitäten:"
        else:
            temp_df=log_df.loc[indices, display_cols]
            outlier_df= temp_df.merge(resource_activity_count,on="resource", how="left")
            temp_col="resource_activity_count"
            label="Anzahl ausgeführter Aktivitäten:"

        for resource, res_df in outlier_df.groupby("resource"):
            value = res_df[temp_col].iloc[0]
            render_single_resource(category,resource,res_df,label,value)

        
          
                

    

