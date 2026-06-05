import streamlit as st

def load_css():
    st.markdown("""
    <style>
   /* Hide deploy button only */
    header {visibility: hidden;}
    [data-testid="stToolbar"] {visibility: hidden;}

    /* Import modern font */
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600&display=swap');

    html, body, [class*="css"] {
        font-family: 'Poppins', sans-serif;
    }

    /* ---------- MAIN BACKGROUND ---------- */
    .stApp {
        background: linear-gradient(120deg,#e8f5e9,#ffffff,#e3f2fd);
        background-size: cover;
    }

    /* ---------- SIDEBAR ---------- */
    section[data-testid="stSidebar"] {
        background: linear-gradient(180deg,#1b5e20,#2e7d32,#66bb6a);
        color: white;
    }

    section[data-testid="stSidebar"] * {
        color: white;
    }


    /* ---------- TITLES ---------- */
    h1 {
        text-align: center;
        color: #1b5e20;
        font-weight: 600;
        font-size: 60px;
    }

    h2, h3 {
        color: #2e7d32;
        font-weight: 500;
    }

    /* ---------- CARD CONTAINER ---------- */
    .card {

        background: white;
        padding: 25px;
        border-radius: 15px;

        box-shadow: 0px 8px 25px rgba(0,0,0,0.08);

        transition: 0.3s;

        margin-top: 20px;
    }

    .card:hover {
        transform: translateY(-5px);
        box-shadow: 0px 12px 35px rgba(0,0,0,0.15);
    }

    /* ---------- BUTTONS ---------- */

    div.stButton > button {

        background: linear-gradient(90deg,#2e7d32,#43a047);

        color: white;

        font-size: 18px;

        border-radius: 10px;

        height: 45px;

        width: 100%;

        border: none;

        transition: 0.3s;
    }

    div.stButton > button:hover {

        background: linear-gradient(90deg,#1b5e20,#2e7d32);

        transform: scale(1.03);

        box-shadow: 0px 5px 15px rgba(0,0,0,0.2);
    }

    /* ---------- INPUT BOXES ---------- */

    .stTextInput input {

        border-radius: 10px;

        border: 2px solid #a5d6a7;

        padding: 8px;
    }

    .stTextInput input:focus {

        border: 2px solid #2e7d32;

        box-shadow: 0 0 8px rgba(46,125,50,0.3);
    }

    /* ---------- FILE UPLOADER ---------- */

    .stFileUploader {

        border-radius: 10px;

        border: 2px dashed #66bb6a;

        padding: 15px;
    }

    /* ---------- SUCCESS / ERROR ---------- */

    .stSuccess {
        border-radius: 8px;
    }

    .stError {
        border-radius: 8px;
    }

    /* ---------- IMAGE STYLE ---------- */

    img {

        border-radius: 12px;

        box-shadow: 0px 6px 20px rgba(0,0,0,0.2);

    }

    /* ---------- METRIC CARDS ---------- */

    .metric-card {

        background: linear-gradient(135deg,#66bb6a,#43a047);

        color: white;

        padding: 20px;

        border-radius: 12px;

        text-align: center;

        font-size: 20px;

        font-weight: 500;

        box-shadow: 0px 5px 15px rgba(0,0,0,0.15);
    }
    .stButton > button {
    white-space: nowrap;
    width: 140px;
	div:has(> br:only-child) {
    display:none;
    }

/* Hide large empty rounded bars */
    .block-container > div:empty {
    display:none;
    }

/* Fix spacing under title */
.history-title{
margin-bottom:10px;
}
}

    </style>
    """, unsafe_allow_html=True)
st.markdown("""
<style>

/* Sidebar background */
[data-testid="stSidebar"] {
    background: linear-gradient(180deg,#1b5e20,#43a047);
}

/* Sidebar text color */
[data-testid="stSidebar"] * {
    color: white;
}

/* Navigation page links */
[data-testid="stSidebarNav"] a {
    font-size: 16px;
    font-weight: 500;
    padding: 8px 10px;
    border-radius: 8px;
}

/* Hover effect */
[data-testid="stSidebarNav"] a:hover {
    background-color: rgba(255,255,255,0.15);
}

/* Active page highlight */
[data-testid="stSidebarNav"] a[aria-current="page"] {
    background-color: rgba(255,255,255,0.25);
    font-weight: 600;
}


</style>
""", unsafe_allow_html=True)