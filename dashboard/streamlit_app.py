import sys
from pathlib import Path

project_root = Path(__file__).resolve().parent.parent
sys.path.append(str(project_root))

import matplotlib.pyplot as plt
import streamlit as st
from sqlalchemy.orm import Session

from analysis.trends import TrendAnalyzer
from database.db import SessionLocal
from database.models import Product
from exports.csv_export import CSVExporter
import plotly.express as px
import pandas as pd

st.set_page_config(
    page_title="WebScrapePro",
    page_icon="📈",
    layout="wide"
)

st.title("📈 WebScrapePro")
st.subheader("E-Commerce Price Tracker & Alert Engine")

db: Session = SessionLocal()

products = db.query(Product).all()

if not products:
    st.warning("No products found.")
    st.stop()

# ---------------- Sidebar ---------------- #

st.sidebar.title("Navigation")
st.sidebar.success("WebScrapePro Dashboard")
st.sidebar.metric("Tracked Products", len(products))

product_names = [product.name for product in products]

selected_name = st.sidebar.selectbox(
    "Select Product",
    product_names
)

selected_product = next(
    product for product in products
    if product.name == selected_name
)

st.sidebar.write("---")
st.sidebar.write(f"**Selected Product:**")
st.sidebar.write(selected_product.name)

# ----------------------------------------- #

analyzer = TrendAnalyzer(db)
exporter = CSVExporter()

st.header(selected_product.name)

col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "Current Price",
    f"₹{selected_product.current_price:,.2f}"
)

col2.metric(
    "Lowest Price",
    f"₹{analyzer.get_lowest_price(selected_product.id):,.2f}"
)

col3.metric(
    "Highest Price",
    f"₹{analyzer.get_highest_price(selected_product.id):,.2f}"
)

average = analyzer.get_moving_average(selected_product.id, 30)

col4.metric(
    "30-Day Average",
    f"₹{average:,.2f}" if average else "N/A"
)

# ---------------- Price History ---------------- #

history = analyzer.get_price_history(selected_product.id)

history_data = []

for item in history:
    history_data.append({
        "Price": item.price,
        "Date": item.recorded_at.strftime("%d-%m-%Y")
    })

st.subheader("📋 Price History")

st.dataframe(
    history_data,
    use_container_width=True
)

# ---------------- Graph ---------------- #

chart_data = pd.DataFrame({
    "Date": [item.recorded_at for item in history],
    "Price": [item.price for item in history]
})

fig = px.line(
    chart_data,
    x="Date",
    y="Price",
    title=f"{selected_product.name} Price Trend",
    markers=True
)

fig.update_layout(
    xaxis_title="Date",
    yaxis_title="Price (₹)",
    hovermode="x unified"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

# ---------------- Statistics ---------------- #

st.subheader("📊 Price Statistics")

change = analyzer.get_price_change(selected_product.id)

trend = analyzer.get_trend(selected_product.id)

col1, col2 = st.columns(2)

if change:

    col1.metric(
        "Price Change",
        f"₹{change['difference']:.2f}",
        f"{change['percentage']}%"
    )

    col2.metric(
        "Trend",
        trend
    )

else:

    st.info("Not enough price history available.")

# ---------------- CSV Export ---------------- #

csv_file = exporter.export_price_history(
    db,
    selected_product
)

with open(csv_file, "rb") as file:

    st.download_button(
        label="📥 Download Price History CSV",
        data=file,
        file_name=Path(csv_file).name,
        mime="text/csv",
    )

db.close()