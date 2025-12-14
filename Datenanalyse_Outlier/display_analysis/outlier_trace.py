import streamlit as st
from ..statistic_analysis.outlier_trace import outlier_trace
from ..statistic_analysis.duration_process import duration_pro_case

def show_trace_outliers(log):

    st.subheader("❗️ Ausreißer - Traces")

    outliers = outlier_trace(log)
    case_duration_df = duration_pro_case(log)

    for category, indices in outliers.items():
        st.write(f"### Kategorie: {category}")
        if indices:
            outlier_df = log.loc[indices]
            st.dataframe(outlier_df, use_container_width=True)
        else:
            st.write("Keine Ausreißer in dieser Kategorie gefunden.")

        
 
        
        outlier_df=outlier_df.merge(
                case_duration_df[["case_id","case_duration"]]  ,
                on="case_id",
                how="left"
        
            )
        #nach case gruppieren und anzeige
        #mit expander
        for case_id, case_df in outlier_df.groupby("case_id"):
            with st.expander(f"Details für Case ID: {case_id}"):
                st.dataframe(case_df[
                    ["activity","resource","timestamp"]
                    + (["case_duration"] if "case_duration" in case_df.columns else []
                       )
            
                ], use_container_width=True)

            


        # #nach case gruppieren und anzeige
        # # outlier_df=(
        # #     log.loc[indices]
        # #     .sort_values(by=["case_id","timestamp"])
        # #     [["case_id","activity","resource","timestamp"]]

        # # )
               
        # # #multiindex: case->activity
        # # outlier_df=outlier_df.set_index(["case_id","activity"])
        # # st.dataframe(outlier_df, use_container_width=True)

        # for case_id, group in outlier_df.reset_index().groupby("case_id"):
        #     st.markdown(f"### 🧾 Case {case_id}")

                # st.dataframe(
                #     group[
                #         ["activity", "resource", "timestamp", "case_duration"]
                #         ].sort_values("timestamp"),
                #     use_container_width=True
                # )   

