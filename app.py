import pandas as pd
import streamlit as st

st.sidebar.header("Loan Advance Calculator")
start = st.sidebar.date_input("Date of Advancement")
end = st.sidebar.date_input("Date of Deal Close")
advance = st.sidebar.number_input("Amount to be advanced", value=1000)
delta = (end - start).days
st.sidebar.write("Days until close: {}".format(delta))

fee = 0.75 * advance / 1000 * delta + 50
st.sidebar.metric("Borrow fee to be paid is", "${:,.2f}".format(fee))

