import streamlit as st
from ..statistic_analysis import duration_process
from ..statistic_analysis import duration_activity

def show_process_duration(log):
    st.subheader("⏰ Prozessdauer")
    case_duration = duration_process.duration_pro_case(log)
    if case_duration is not None:
        # st.dataframe(case_duration, use_container_width=True)
        st.write("Durchschnittliche Prozessdauer:",case_duration["case_duration"].mean())
        st.write("Kürzeste Prozessdauer:", case_duration["case_duration"].min())
        st.write("Längste Prozessdauer", case_duration["case_duration"].max())