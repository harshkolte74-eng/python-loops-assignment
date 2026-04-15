import streamlit as st

import pandas as pd

st.set_page_config(page_title="Sales Dashboard", layout="wide", initial_sidebar_state="expanded")


st.title(" Sales Summary Dashboard")
st.subheader("Interactive sales data viewer for quick insights")


data = {
    'Product': ['Laptop', 'Mouse', 'Keyboard', 'Monitor', 'Headphones', 'Webcam', 'USB Cable'],
    'Category': ['Electronics', 'Accessories', 'Accessories', 'Electronics', 'Accessories', 'Electronics', 'Accessories'],
    'Sales': [1200, 25, 75, 350, 89, 120, 15]
}

df = pd.DataFrame(data)


st.sidebar.header("Filter Options")
st.sidebar.markdown("---")

categories = ['All'] + sorted(df['Category'].unique().tolist())

selected_category = st.sidebar.selectbox(
    "Select a Category:",
    categories
)

if selected_category == 'All':
    filtered_df = df
else:
    filtered_df = df[df['Category'] == selected_category]

st.sidebar.markdown("---")
st.sidebar.metric("Total Products", len(filtered_df))
st.sidebar.metric("Total Sales", f"${filtered_df['Sales'].sum():,.2f}")

st.markdown("### Filtered Sales Data")
st.dataframe(filtered_df, use_container_width=True)

st.markdown("### Sales Trend")
if len(filtered_df) > 0:
    st.line_chart(filtered_df.set_index('Product')['Sales'])
else:
    st.info("No data available for the selected category")

st.markdown("---")
st.caption("Built with Streamlit  | Data updated: 2026")