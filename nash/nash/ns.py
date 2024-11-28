import streamlit as st

about_page = st.Page(
    page="views/About_me.py",
    title="About Me",
    icon=":material/account_circle:",
    default=True,
)
project_1_page = st.Page(
    page="views/My_skills.py",
    title="My Skills",
    icon=":material/sort:",
)
project_2_page = st.Page(
    page="views/achievements.py",
    title="Achievements",
    icon=":material/sort:",
)

pg = st.navigation(
    {
        "info": [about_page],
        "other info": [project_1_page, project_2_page],
    }
)

st.logo("assets/meow.jpg")
st.sidebar.text("Made by Nash")
st.sidebar.text("""Facebook: Nash Eowyn
                Gmail Acc: nashjanaban50@gmail.com
                Contact num: 09675597126""")


pg.run()
