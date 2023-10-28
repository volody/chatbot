# https://ff27908.canada-central.azure.snowflakecomputing.com
# UDFFXOE.QI56807

import streamlit as st

conn = st.experimental_connection("snowpark")
df = conn.query("select current_warehouse()")
st.write(df)