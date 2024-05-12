import streamlit as st
import numpy as np
import pickle
from sklearn.linear_model import LinearRegression


lr_model = pickle.load(open('lr_model.pkl','rb'))

st.title("Calculate Average Yearly Expense Spent by a Customer")

form = st.form("Input Form")

s_length = form.text_input("Avg. Session Length (minuite)")
app_time = form.text_input("Time spent on App (minuite)")
web_time = form.text_input("Time spent on Website (minuite)")
membership = form.text_input("Length of Membership (in month)")


s_state = form.form_submit_button("Submit")

if s_state:
    if s_length == "" or app_time == "" or web_time == "" or membership == "":
        st.warning("Please fill all the fields !")
    else:
        arr = np.array([int(s_length), int(app_time), int(web_time), int(membership)])
        output = lr_model.predict([arr])
        st.success(f"{output}")