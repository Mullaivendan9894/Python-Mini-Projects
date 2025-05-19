import streamlit as st
from datetime import datetime
import requests
import pandas as pd
import matplotlib.pyplot as plt
import altair as alt

API_URL = "http://127.0.0.1:8000"

def analytics_months_tab():
    st.title("Expense Breakdown by Months")

    response = requests.get(f"{API_URL}/analytics/monthly")
    response = response.json()
    df = pd.DataFrame(response).rename(columns = {
        "month_name": "Month Name",
        "total": "Total"
    })

    st.bar_chart(
        data=df.set_index("Month Name")["Total"],
        width=600,  # Adjust width
        height=400,  # Adjust height
        use_container_width=True  # Responsive sizing
    )
    st.table(df.style.format({"Total": "₹ {:.2f}"}))