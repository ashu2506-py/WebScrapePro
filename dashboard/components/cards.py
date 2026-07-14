import streamlit as st


def show_product_cards(products):

    if not products:

        st.warning("No products found.")

        return None

    cols = st.columns(3)

    selected = None

    for index, product in enumerate(products):

        with cols[index % 3]:

            with st.container(border=True):

                st.markdown(f"### {product.name}")

                st.caption(product.site.name)

                st.metric(
                    "Current Price",
                    f"₹{product.current_price:,.0f}"
                )

                if st.button(
                    "📊 View Analytics",
                    key=f"btn_{product.id}"
                ):
                    selected = product

    return selected