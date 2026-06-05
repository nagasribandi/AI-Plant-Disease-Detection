import streamlit as st
from database import cursor, conn
import os
import streamlit as st
from style import load_css

load_css()
# login check
if "user" not in st.session_state or st.session_state.user is None:

    st.warning("⚠ Please login first to access profile.")

    if st.button("Go to Login"):
        st.switch_page("pages/Login.py")

    st.stop()

st.title("Update Profile")

cursor.execute(
"SELECT first_name,last_name,email,password,profile_pic FROM users WHERE email=?",
(st.session_state["user"],)
)

user = cursor.fetchone()

first = st.text_input("First Name", user[0])
last = st.text_input("Last Name", user[1])
email = st.text_input("Email", user[2])
password = st.text_input("Password", user[3])

pic = st.file_uploader("Change Profile Picture")

if st.button("Update Profile"):

    path=user[4]

    if pic:
        os.makedirs("profile_pics",exist_ok=True)
        path=f"profile_pics/{pic.name}"

        with open(path,"wb") as f:
            f.write(pic.getbuffer())

    cursor.execute("""
    UPDATE users
    SET first_name=?,last_name=?,email=?,password=?,profile_pic=?
    WHERE email=?
    """,(first,last,email,password,path,st.session_state["user"]))

    conn.commit()

    st.success("Profile updated successfully")
col1,col2 = st.columns([8,1])

with col2:
    if st.button("Logout"):
        st.session_state.user = None
        st.switch_page("Dash-Board.py")