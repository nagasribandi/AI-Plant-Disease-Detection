import streamlit as st
from database import cursor
from style import load_css

load_css()

st.title("Login")

email = st.text_input("Email")
password = st.text_input("Password", type="password")

if st.button("Login"):

    email = email.strip().lower()
    password = password.strip()

    cursor.execute(
        "SELECT * FROM users WHERE email=?",
        (email,)
    )

    user = cursor.fetchone()

    if user and user[3] == password:

        st.success("Login successful")

        st.session_state.user = email

        st.switch_page("pages/Upload-Images.py")

    else:
        st.error("Invalid email or password")


st.write("Don't have an account?")
st.page_link("pages/Signup.py", label="Sign up here")