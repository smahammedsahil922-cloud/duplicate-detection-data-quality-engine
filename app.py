
from collections import Counter
from io import BytesIO

import pandas as pd
import plotly.express as px
import streamlit as st


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="Member Data Quality Engine",
    page_icon="🔍",
    layout="wide",
    initial_sidebar_state="expanded",
)


# ============================================================
# CONSTANTS
# ============================================================

DEFAULT_FILE = "data/members_50000.csv"

IDENTIFIER_COLUMNS = [
    "member_id",
    "email",
    "phone",
]

DISPLAY_COLUMNS = [
    "member_id",
    "member_name",
    "email",
    "phone",
    "age",
    "gender",
    "city",
    "membership_type",
    "join_date",
    "is_active",
]


# ============================================================
# DATA LOADING
# ============================================================

@st.cache_data
def load_csv(file_path):

    return pd.read_csv(file_path)


def load_uploaded_file(uploaded_file):

    file_name = uploaded_file.name.lower()

    if file_name.endswith(".csv"):
        return pd.read_csv(uploaded_file)

    if file_name.endswith((".xlsx", ".xls")):
        return pd.read_excel(uploaded_file)

    if file_name.endswith(".json"):
        return pd.read_json(uploaded_file)

    raise ValueError("Unsupported file format.")


# ============================================================
# ANALYTICS FUNCTIONS
# ============================================================

def analyze_column(series):

    """
    Calculate duplicate statistics for one column.

    Null values are excluded from identifier analysis.
    """

    values = series.dropna()

    total_records = len(values)

    unique_values = values.nunique()

    duplicate_occurrences = total_records - unique_values

    duplicate_rate = (
        duplicate_occurrences / total_records * 100
        if total_records > 0
        else 0
    )

    frequencies = Counter(values.tolist())

    duplicate_frequency = {
        str(value): count
        for value, count in frequencies.items()
        if count > 1
    }

    return {
        "total_records": total_records,
        "unique_values": unique_values,
        "duplicate_occurrences": duplicate_occurrences,
        "duplicate_rate": duplicate_rate,
        "duplicate_frequency": duplicate_frequency,
    }


def create_duplicate_table(df, column):

    """
    Return repeated values and their frequencies.
    """

    frequency = (
        df[column]
        .dropna()
        .value_counts()
        .rename_axis(column)
        .reset_index(name="frequency")
    )

    frequency = frequency[
        frequency["frequency"] > 1
    ].copy()

    frequency = frequency.sort_values(
        by="frequency",
        ascending=False,
    )

    return frequency


def get_quality_metrics(df):

    total_cells = df.shape[0] * df.shape[1]

    missing_cells = int(
        df.isna().sum().sum()
    )

    missing_rate = (
        missing_cells / total_cells * 100
        if total_cells > 0
        else 0
    )

    complete_duplicate_rows = int(
        df.duplicated().sum()
    )

    duplicate_row_rate = (
        complete_duplicate_rows / len(df) * 100
        if len(df) > 0
        else 0
    )

    return {
        "rows": len(df),
        "columns": len(df.columns),
        "missing_cells": missing_cells,
        "missing_rate": missing_rate,
        "complete_duplicate_rows": complete_duplicate_rows,
        "duplicate_row_rate": duplicate_row_rate,
    }


def create_quality_report(df):

    metrics = get_quality_metrics(df)

    return pd.DataFrame(
        {
            "Metric": [
                "Total Rows",
                "Total Columns",
                "Missing Cells",
                "Missing Rate (%)",
                "Complete Duplicate Rows",
                "Complete Duplicate Row Rate (%)",
            ],
            "Value": [
                metrics["rows"],
                metrics["columns"],
                metrics["missing_cells"],
                round(metrics["missing_rate"], 2),
                metrics["complete_duplicate_rows"],
                round(metrics["duplicate_row_rate"], 2),
            ],
        }
    )


def create_identifier_report(df):

    report = []

    for column in IDENTIFIER_COLUMNS:

        if column not in df.columns:
            continue

        result = analyze_column(df[column])

        report.append(
            {
                "Column": column,
                "Total Records": result["total_records"],
                "Unique Values": result["unique_values"],
                "Duplicate Occurrences": (
                    result["duplicate_occurrences"]
                ),
                "Duplicate Rate (%)": round(
                    result["duplicate_rate"], 2
                ),
            }
        )

    return pd.DataFrame(report)


def dataframe_to_csv(df):

    return df.to_csv(index=False).encode("utf-8")


# ============================================================
# SIDEBAR
# ============================================================

st.sidebar.title("🔍 Member Data Quality")

st.sidebar.caption(
    "Duplicate Detection & Data Quality Analytics Engine"
)

page = st.sidebar.radio(
    "Navigation",
    [
        "Executive Overview",
        "Duplicate Analysis",
        "Data Quality",
    ],
)

st.sidebar.divider()

st.sidebar.subheader("Dataset")

uploaded_file = st.sidebar.file_uploader(
    "Upload another dataset (optional)",
    type=["csv", "xlsx", "xls", "json"],
)

if uploaded_file is None:

    try:

        df = load_csv(DEFAULT_FILE)

        st.sidebar.success(
            "Default dataset loaded"
        )

    except FileNotFoundError:

        st.error(
            f"Default dataset not found: {DEFAULT_FILE}"
        )

        st.info(
            "Place members_50000.csv inside the data folder."
        )

        st.stop()

    except Exception as error:

        st.error(
            f"Unable to load default dataset: {error}"
        )

        st.stop()

else:

    try:

        df = load_uploaded_file(uploaded_file)

        st.sidebar.success(
            "Uploaded dataset loaded"
        )

    except Exception as error:

        st.error(
            f"Unable to load uploaded file: {error}"
        )

        st.stop()


# ============================================================
# DATA VALIDATION
# ============================================================

if df.empty:

    st.warning("The dataset is empty.")

    st.stop()


if len(df.columns) == 0:

    st.error("The dataset contains no columns.")

    st.stop()


# ============================================================
# GLOBAL HEADER
# ============================================================

st.title(
    "🔍 Duplicate Detection & Data Quality Analytics Engine"
)

st.caption(
    "Member Records Analysis | Streamlit Dashboard"
)

st.markdown(
    "Analyze duplicate identifiers, data completeness, "
    "and complete duplicate rows."
)


# ============================================================
# PAGE 1 — EXECUTIVE OVERVIEW
# ============================================================

if page == "Executive Overview":

    st.header("📊 Executive Overview")

    metrics = get_quality_metrics(df)

    # --------------------------------------------------------
    # DATASET KPIs
    # --------------------------------------------------------

    col1, col2, col3, col4 = st.columns(4)

    with col1:

        st.metric(
            "Total Records",
            f"{metrics['rows']:,}",
        )

    with col2:

        st.metric(
            "Total Columns",
            f"{metrics['columns']:,}",
        )

    with col3:

        st.metric(
            "Missing Cells",
            f"{metrics['missing_cells']:,}",
        )

    with col4:

        st.metric(
            "Complete Duplicate Rows",
            f"{metrics['complete_duplicate_rows']:,}",
        )

    st.divider()

    # --------------------------------------------------------
    # IDENTIFIER SUMMARY
    # --------------------------------------------------------

    st.subheader("Identifier Duplicate Summary")

    identifier_report = create_identifier_report(df)

    if identifier_report.empty:

        st.warning(
            "No configured identifier columns found."
        )

    else:

        st.dataframe(
            identifier_report,
            use_container_width=True,
            hide_index=True,
        )

    st.divider()

    # --------------------------------------------------------
    # DATASET PREVIEW
    # --------------------------------------------------------

    st.subheader("Dataset Preview")

    st.dataframe(
        df.head(10),
        use_container_width=True,
        hide_index=True,
    )

    st.divider()

    # --------------------------------------------------------
    # COLUMN INFORMATION
    # --------------------------------------------------------

    st.subheader("Column Information")

    column_info = pd.DataFrame(
        {
            "Column": df.columns,
            "Data Type": [
                str(dtype)
                for dtype in df.dtypes
            ],
            "Missing Values": [
                int(df[column].isna().sum())
                for column in df.columns
            ],
            "Unique Values": [
                int(df[column].nunique(dropna=True))
                for column in df.columns
            ],
        }
    )

    st.dataframe(
        column_info,
        use_container_width=True,
        hide_index=True,
    )

    st.download_button(
        label="Download Identifier Summary",
        data=dataframe_to_csv(identifier_report),
        file_name="identifier_duplicate_summary.csv",
        mime="text/csv",
    )


# ============================================================
# PAGE 2 — DUPLICATE ANALYSIS
# ============================================================

elif page == "Duplicate Analysis":

    st.header("🔍 Duplicate Analysis")

    available_identifiers = [
        column
        for column in IDENTIFIER_COLUMNS
        if column in df.columns
    ]

    if not available_identifiers:

        st.warning(
            "No identifier columns available for analysis."
        )

        st.stop()

    selected_column = st.selectbox(
        "Select identifier column",
        available_identifiers,
    )

    results = analyze_column(
        df[selected_column]
    )

    # --------------------------------------------------------
    # SELECTED COLUMN KPIs
    # --------------------------------------------------------

    col1, col2, col3, col4 = st.columns(4)

    with col1:

        st.metric(
            "Total Records",
            f"{results['total_records']:,}",
        )

    with col2:

        st.metric(
            "Unique Values",
            f"{results['unique_values']:,}",
        )

    with col3:

        st.metric(
            "Duplicate Occurrences",
            f"{results['duplicate_occurrences']:,}",
        )

    with col4:

        st.metric(
            "Duplicate Rate",
            f"{results['duplicate_rate']:.2f}%",
        )

    st.divider()

    # --------------------------------------------------------
    # FREQUENCY TABLE
    # --------------------------------------------------------

    st.subheader(
        f"Repeated Values: {selected_column}"
    )

    duplicate_df = create_duplicate_table(
        df,
        selected_column,
    )

    if duplicate_df.empty:

        st.success(
            "No duplicate values detected."
        )

    else:

        st.dataframe(
            duplicate_df,
            use_container_width=True,
            hide_index=True,
        )

        st.subheader("Duplicate Frequency Chart")

        chart_df = duplicate_df.head(20).copy()

        chart_df[selected_column] = (
            chart_df[selected_column].astype(str)
        )

        fig = px.bar(
            chart_df,
            x=selected_column,
            y="frequency",
            title=f"Top 20 Duplicate {selected_column} Values",
            labels={
                selected_column: selected_column,
                "frequency": "Frequency",
            },
        )

        fig.update_layout(
            xaxis_title=selected_column,
            yaxis_title="Frequency",
        )

        st.plotly_chart(
            fig,
            use_container_width=True,
        )

        st.download_button(
            label="Download Duplicate Frequency Report",
            data=dataframe_to_csv(duplicate_df),
            file_name=(
                f"{selected_column}_duplicate_report.csv"
            ),
            mime="text/csv",
        )

    st.divider()

    # --------------------------------------------------------
    # ALL IDENTIFIER COMPARISON
    # --------------------------------------------------------

    st.subheader("All Identifier Comparison")

    identifier_report = create_identifier_report(df)

    st.dataframe(
        identifier_report,
        use_container_width=True,
        hide_index=True,
    )

    if not identifier_report.empty:

        comparison_fig = px.bar(
            identifier_report,
            x="Column",
            y="Duplicate Occurrences",
            title="Duplicate Occurrences by Identifier",
        )

        st.plotly_chart(
            comparison_fig,
            use_container_width=True,
        )


# ============================================================
# PAGE 3 — DATA QUALITY
# ============================================================

elif page == "Data Quality":

    st.header("📋 Data Quality Analytics")

    metrics = get_quality_metrics(df)

    # --------------------------------------------------------
    # QUALITY KPIs
    # --------------------------------------------------------

    col1, col2, col3, col4 = st.columns(4)

    with col1:

        st.metric(
            "Total Rows",
            f"{metrics['rows']:,}",
        )

    with col2:

        st.metric(
            "Total Columns",
            f"{metrics['columns']:,}",
        )

    with col3:

        st.metric(
            "Missing Rate",
            f"{metrics['missing_rate']:.2f}%",
        )

    with col4:

        st.metric(
            "Duplicate Row Rate",
            f"{metrics['duplicate_row_rate']:.2f}%",
        )

    st.divider()

    # --------------------------------------------------------
    # MISSING VALUES
    # --------------------------------------------------------

    st.subheader("Missing Values by Column")

    missing_df = pd.DataFrame(
        {
            "Column": df.columns,
            "Missing Values": [
                int(df[column].isna().sum())
                for column in df.columns
            ],
        }
    )

    st.dataframe(
        missing_df,
        use_container_width=True,
        hide_index=True,
    )

    missing_chart = px.bar(
        missing_df,
        x="Column",
        y="Missing Values",
        title="Missing Values by Column",
    )

    st.plotly_chart(
        missing_chart,
        use_container_width=True,
    )

    st.divider()

    # --------------------------------------------------------
    # COMPLETE DUPLICATE ROWS
    # --------------------------------------------------------

    st.subheader("Complete Duplicate Rows")

    duplicate_rows = df[
        df.duplicated(keep=False)
    ].copy()

    if duplicate_rows.empty:

        st.success(
            "No complete duplicate rows detected."
        )

    else:

        st.info(
            f"Rows involved in complete duplicate groups: "
            f"{len(duplicate_rows):,}"
        )

        st.dataframe(
            duplicate_rows,
            use_container_width=True,
            hide_index=True,
        )

        st.download_button(
            label="Download Complete Duplicate Rows",
            data=dataframe_to_csv(duplicate_rows),
            file_name="complete_duplicate_rows.csv",
            mime="text/csv",
        )

    st.divider()

    # --------------------------------------------------------
    # QUALITY REPORT
    # --------------------------------------------------------

    st.subheader("Data Quality Report")

    quality_report = create_quality_report(df)

    st.dataframe(
        quality_report,
        use_container_width=True,
        hide_index=True,
    )

    st.download_button(
        label="Download Data Quality Report",
        data=dataframe_to_csv(quality_report),
        file_name="data_quality_report.csv",
        mime="text/csv",
    )