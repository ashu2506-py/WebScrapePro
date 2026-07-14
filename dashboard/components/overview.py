import streamlit as st


def show_overview(products, analyzer):

    total_products = len(products)

    current_prices = [
        p.current_price
        for p in products
    ]

    average_price = sum(current_prices) / total_products

    lowest_price = min(current_prices)

    col1, col2, col3, col4 = st.columns(4)

    col1.metric(
        "📦 Products",
        total_products
    )

    col2.metric(
        "💰 Avg Price",
        f"₹{average_price:,.0f}"
    )

    col3.metric(
        "📉 Lowest Price",
        f"₹{lowest_price:,.0f}"
    )

    col4.metric(
        "🔔 Active Alerts",
        "5"
    )