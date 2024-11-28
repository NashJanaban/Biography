import streamlit as st

from form.contact import contact_form

@st.dialog("Contact Me")
def show_contact_form():
    contact_form()

col1, col2 = st.columns(2, gap="small", vertical_alignment="center")
with col1:
    st.image("./assets/profile.jpg", width=230,)
with col2:
    st.title("Nash Janaban", anchor=False)
    st.write(
        "A Computer Engineering student, activity in Programming Logic and Design"
    )
    if st.button("Contact Me"):
        show_contact_form()
st.write("\n")
st.subheader("Personal Details", anchor=False)
st.write(
    """- Name is Nash Eowyn Y. Janaban
- Birthday May 11, 2006
- Age 18 years old
- Course is Bachelor of Science in Computer Engineering.
- First year college student"""
, height=150
)
st.write("\n")
st.subheader("Family Background", anchor=False)
st.text_area("",
    """Father's Name is Ian P. Janaban
Birthday: October 4, 1978

Mother's Name is Meryl Y. Janaban
Birthday: April 6, 1981

Sister's Name is Schinina Isabella Y. Janaban
Birthday: February 19, 2009""", height=230
)

st.write("\n")
st.subheader("Educational Attainment")
st.text_area("",
    """Elementary, Surigao City Pilot School
High School, Nemco
Senior High, Surigao Norte National High School
""", height=100
)


