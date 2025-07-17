import streamlit as st
import pandas as pd

st.title("✉️ Contact Me")

with st.form("contact_form"):
    name = st.text_input("Your Name")
    email = st.text_input("Your Email")
    message = st.text_area("Your Message")
    submitted = st.form_submit_button("Submit")

    if submitted:
        new_data = pd.DataFrame([[name, email, message]], columns=["Name", "Email", "Message"])
        new_data.to_csv("data/contacts.csv", mode="a", header=False, index=False)
        st.success("Thank you for your message!")
