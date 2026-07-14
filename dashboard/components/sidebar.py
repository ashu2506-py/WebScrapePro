import streamlit as st


def show_sidebar(products):

    st.sidebar.title("📦 Product Explorer")

    search = st.sidebar.text_input(
        "🔍 Search Product",
        placeholder="Search..."
    )

    stores = sorted(set(product.site.name for product in products))

    selected_store = st.sidebar.selectbox(
        "🏪 Store",
        ["All"] + stores
    )

    filtered = []

    for product in products:

        if search and search.lower() not in product.name.lower():
            continue

        if (
            selected_store != "All"
            and product.site.name != selected_store
        ):
            continue

        filtered.append(product)

    return filtered