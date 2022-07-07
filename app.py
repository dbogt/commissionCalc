import pandas as pd
import streamlit as st

st.header("Loan Advance Calculator")
start = st.date_input("Date of Advancement")
end = st.date_input("Date of Deal Close")
advance = st.number_input("Amount to be advanced", value=1000)
delta = (end - start).days
st.write("Days until close: {}".format(delta))

fee = 0.75 * advance / 1000 * delta + 50
st.metric("Borrow fee to be paid is", "${:,.2f}".format(fee))

