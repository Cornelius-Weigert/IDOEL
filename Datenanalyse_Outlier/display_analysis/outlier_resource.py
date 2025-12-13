import streamlit as st
from ..statistic_analysis.outlier_resource import outlier_resources


def show_resource_outliers(log):
    """
    Zeigt Ausreißer in Ressourcen im Streamlit-Interface an.

    :param log: Das Ereignisprotokoll als DataFrame.
    """

    st.subheader("❗️ Ausreißer - Ressourcen")

    display_cols=["case_id","activity","resource","timestamp"]

    outliers, log_with_counts  = outlier_resources(log)

    for category, indices in outliers.items():
        st.write(f"### Kategorie: {category}")
        if indices:
            outlier_df = log.loc[indices, display_cols]
            st.dataframe(outlier_df, use_container_width=True)
        else:
            st.write("Keine Ausreißer in dieser Kategorie gefunden.")

    st.subheader("📊 Ereignisse pro Ressource")

    st.bar_chart(log_with_counts, x="resource", y="activity_count")       


