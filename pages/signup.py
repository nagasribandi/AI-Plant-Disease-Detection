import streamlit as st
from database import cursor, conn
import os
import re
from style import load_css

load_css()
st.title("Create Account")

# ---------- Password Strength Function ----------
def password_strength(password):

    score = 0

    if len(password) >= 8:
        score += 1

    if re.search("[A-Z]", password):
        score += 1

    if re.search("[0-9]", password):
        score += 1

    if re.search("[@#$%^&*!]", password):
        score += 1

    if score <= 1:
        return "Weak"

    elif score == 2:
        return "Medium"

    else:
        return "Strong"


# ---------- Inputs ----------
first = st.text_input("First Name")
last = st.text_input("Last Name")
email = st.text_input("Email").strip().lower()

password = st.text_input("Password", type="password")
confirm = st.text_input("Confirm Password", type="password")

pic = st.file_uploader("Upload Profile Picture")


# ---------- Password Strength Indicator ----------
if password:

    strength = password_strength(password)

    if strength == "Weak":
        st.error("Password Strength: Weak")

    elif strength == "Medium":
        st.warning("Password Strength: Medium")

    else:
        st.success("Password Strength: Strong")


# ---------- Password Match Check ----------
if confirm:

    if password == confirm:
        st.success("Passwords Matched")

    else:
        st.error("Passwords Do Not Match")


# ---------- Signup Button ----------
if st.button("Sign Up"):

    # Check empty fields
    if not first or not last or not email or not password or not confirm:
        st.error("Please fill all fields")

    elif password != confirm:
        st.error("Passwords do not match")

    else:

        # check if email already exists
        cursor.execute("SELECT * FROM users WHERE email=?", (email,))
        user = cursor.fetchone()

        if user:
            st.error("Email already registered. Please login.")

        else:

            path = None

            # save profile picture
            if pic:

                os.makedirs("profile_pics", exist_ok=True)

                path = f"profile_pics/{pic.name}"

                with open(path, "wb") as f:
                    f.write(pic.getbuffer())

            # ---------- Password Hashing ----------
            

            # insert user
            cursor.execute(
                "INSERT INTO users VALUES (?,?,?,?,?)",
                (first, last, email, password, path)
            )

            conn.commit()

            st.success("Account created successfully")

            st.success("Account created successfully!")

            st.switch_page("pages/Login.py")