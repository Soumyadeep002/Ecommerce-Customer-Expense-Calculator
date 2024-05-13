import streamlit as st
import numpy as np
import pickle
from sklearn.linear_model import LinearRegression


lr_model = pickle.load(open('lr_model.pkl','rb'))

st.title("Calculate Average Yearly Expense Spent by a Customer")

col1, col2 = st.columns(2)

s_length = col1.number_input("Avg. Session Length (minuite)")
app_time = col2.number_input("Time spent on App (minuite)")
web_time = st.number_input("Time spent on Website (minuite)")
membership = st.number_input("Length of Membership (in month)")


s_state = st.button("Submit")

if s_state:
    if s_length < 0 or app_time < 0 or web_time < 0 or membership < 0:
        st.warning("Please fill all the fields with valid numbers !")
    else:
        arr = np.array([int(s_length), int(app_time), int(web_time), int(membership)])
        output = lr_model.predict([arr])

        st.header("Approximate Expense spent by the Customer:")
        st.subheader(f"$ {round(output[0], 2)}")