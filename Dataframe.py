import numpy as np
import pandas as pd
import streamlit as st
from faker import Faker

def mean_activity(activity_array):
    return np.mean(activity_array)


def detect_outliers(df, threshold=70):
    """
    Regelbasierte Outlier:
    hohe mittlere Jahresaktivität
    """
    if "activity" not in df.columns:
        return pd.DataFrame()

    mask = df["activity"].apply(mean_activity) > threshold
    return df[mask]


select_tab, visual_tab, outliers_tab = st.tabs(
    ["Select outliers", "Visualization", "Outliers"]
)

@st.cache_data
def get_profile_dataset(number_of_items: int = 20, seed: int = 0) -> pd.DataFrame:
    new_data = []

    fake = Faker()
    np.random.seed(seed)
    Faker.seed(seed)

    for i in range(number_of_items):
        new_data.append(
            {
                "outlier": f"Outlier {i + 1}",
                "daily_activity": np.random.rand(25),
                "activity": np.random.randint(2, 90, size=12),
            }
        )

    return pd.DataFrame(new_data)

column_configuration = {
    "outlier": st.column_config.TextColumn(
        "Outlier", width="medium"
    ),
    "activity": st.column_config.LineChartColumn(
        "Activity (1 year)",
        width="large",
        y_min=0,
        y_max=100,
    ),
    "daily_activity": st.column_config.BarChartColumn(
        "Activity (daily)",
        width="medium",
        y_min=0,
        y_max=1,
    ),
}

with select_tab:
    st.header("Select outliers")

    df = get_profile_dataset()

    event = st.dataframe(
        df,
        column_config=column_configuration,
        width='stretch',
        hide_index=True,
        selection_mode="multi-row",
        on_select="rerun",
    )

    selected_rows = event.selection.rows

with visual_tab: 
    st.header("Visualization")

    if selected_rows:
        st.subheader("Selected outliers - visualization")

        activity_df = {
            df.iloc[i]["outlier"]: df.iloc[i]["activity"]
            for i in selected_rows
        }
        daily_df = {
            df.iloc[i]["outlier"]: df.iloc[i]["daily_activity"]
            for i in selected_rows
        }

        st.line_chart(pd.DataFrame(activity_df))
        st.bar_chart(pd.DataFrame(daily_df))
    else:
        st.info("No outliers selected.")


with outliers_tab:
    st.header("Outliers")

    auto_outliers = detect_outliers(df)

    st.subheader("Automatically detected outliers")
    st.dataframe(
        auto_outliers,
        column_config=column_configuration,
        width='stretch',
        hide_index=True,
    )

    manual_outliers = df.iloc[selected_rows] if selected_rows else pd.DataFrame()

    st.subheader("Manually selected outliers")
    if not manual_outliers.empty:
        st.dataframe(
            manual_outliers,
            column_config=column_configuration,
            width='stretch',
            hide_index=True,
        )
    else:
        st.info("No manual outliers selected.")
