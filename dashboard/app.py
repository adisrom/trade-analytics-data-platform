import streamlit as st
import pandas as pd

from database import get_engine


st.set_page_config(
    page_title="Trade Compliance Analytics Dashboard",
    layout="wide"
)

st.title("Trade Compliance Analytics Dashboard")


engine = get_engine()

query = """
SELECT *
FROM trade.compliance_dashboard_summary;
"""

df = pd.read_sql(query, engine)

row = df.iloc[0]

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "Total Shipments",
        f"{row['total_shipments']:,}"
    )

with col2:
    st.metric(
        "Total Trade Value",
        f"${row['total_trade_value']:,.2f}"
    )

with col3:
    st.metric(
        "Duty Exposure",
        f"${row['total_duty_exposure']:,.2f}"
    )


col4, col5, col6 = st.columns(3)

with col4:
    st.metric(
        "Total Suppliers",
        f"{row['total_suppliers']:,}"
    )

with col5:
    st.metric(
        "High Risk Suppliers",
        f"{row['high_risk_suppliers']:,}"
    )

with col6:
    st.metric(
        "Inspection Failure Rate",
        f"{row['inspection_failure_rate_percentage']:.2f}%"
    )

st.divider()

st.header("Supplier Risk Distribution")

distribution_query = """
SELECT *
FROM trade.supplier_risk_distribution;
"""

distribution_df = pd.read_sql(
    distribution_query,
    engine
)

st.bar_chart(
    distribution_df.set_index("risk_category")
)

st.divider()

st.header("Monthly Trade Performance")

monthly_query = """
SELECT *
FROM trade.monthly_trade_metrics
ORDER BY month;
"""

monthly_df = pd.read_sql(
    monthly_query,
    engine
)

st.line_chart(
    monthly_df.set_index("month")[
        ["total_declared_value", "total_duty_amount"]
    ]
)