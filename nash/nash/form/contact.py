import streamlit as st

def contact_form():
    with st.form("Contact_form"):
        name = st.text_input("Name")
        email = st.text_input("Email Adress")
        message = st.text_input("Your Message")
        submit_button = st.form_submit_button("Submit")

    if submit_button:
        st.success("Message successfuly sent!") 