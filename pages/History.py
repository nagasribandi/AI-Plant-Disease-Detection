import streamlit as st
from database import cursor
from style import load_css

load_css()

# ---------------- LOGIN CHECK ---------------- #

if "user" not in st.session_state or st.session_state.user is None:

    st.warning("⚠ Please login first to view history.")

    if st.button("Go to Login"):
        st.switch_page("pages/Login.py")

    st.stop()


# ---------------- PAGE STYLE ---------------- #

st.markdown("""
<style>

.history-title{
font-size:48px;
font-weight:900;
color:#1b5e20;
text-align:center;
margin-bottom:5px;
}

.history-sub{
text-align:center;
color:#666;
font-size:18px;
margin-bottom:35px;
}

.stat-box{
background:white;
padding:20px;
border-radius:18px;
box-shadow:0 10px 25px rgba(0,0,0,0.15);
text-align:center;
}

.stat-box h4{
color:#555;
}

.user-email{
font-size:16px;
font-weight:600;
word-break:break-all;
color:#333;
margin-top:10px;
}

.history-card{
background:white;
padding:25px;
border-radius:18px;
box-shadow:0 10px 25px rgba(0,0,0,0.15);
margin-top:20px;
}

.disease{
font-size:22px;
font-weight:bold;
color:#2e7d32;
}

.conf{
font-size:16px;
color:#444;
margin-top:5px;
}

.time{
font-size:14px;
color:#777;
margin-top:8px;
}

.empty-history{
text-align:center;
padding:60px;
background:white;
border-radius:20px;
box-shadow:0 10px 30px rgba(0,0,0,0.1);
margin-top:30px;
}

.empty-icon{
font-size:60px;
margin-bottom:10px;
color:#2e7d32;
}

img{
border-radius:12px;
}

.footer{
text-align:center;
color:#444;
font-size:14px;
margin-top:40px;
}

</style>
""", unsafe_allow_html=True)


# ---------------- HEADER ---------------- #

st.markdown('<div class="history-title">📊 Prediction History</div>', unsafe_allow_html=True)

st.markdown('<div class="history-sub">View your past disease detection results</div>', unsafe_allow_html=True)


# ---------------- DATABASE QUERY ---------------- #

cursor.execute(
"SELECT image_path,disease,confidence,timestamp FROM history WHERE email=?",
(st.session_state["user"],)
)

data = cursor.fetchall()


# ---------------- STATS SECTION ---------------- #

colA,colB,colC = st.columns(3)

with colA:
    st.markdown(f"""
    <div class="stat-box">
    <h3>📁 Total Predictions</h3>
    <h4>{len(data)}</h4>
    </div>
    """, unsafe_allow_html=True)

with colB:
    st.markdown("""
    <div class="stat-box">
    <h3>🌿 AI Model</h3>
    <h4>EfficientNet</h4>
    </div>
    """, unsafe_allow_html=True)

with colC:
    st.markdown(f"""
    <div class="stat-box">
    <h3>👤 User</h3>
    <p class="user-email">{st.session_state['user']}</p>
    </div>
    """, unsafe_allow_html=True)


st.markdown("<br>", unsafe_allow_html=True)


# ---------------- EMPTY HISTORY ---------------- #

if len(data) == 0:

    st.markdown("""
    <div class="empty-history">

    <div class="empty-icon">🌿</div>

    <h3>No Prediction History Yet</h3>

    <p>
    Upload a plant leaf image and the AI model will detect diseases.
    Your predictions will appear here.
    </p>

    </div>
    """, unsafe_allow_html=True)

else:

    # ---------------- HISTORY ITEMS ---------------- #

    for img,disease,conf,time in data:

        st.markdown('<div class="history-card">', unsafe_allow_html=True)

        col1,col2 = st.columns([1,2])

        with col1:
            st.image(img,width=200)

        with col2:

            disease_name = disease.replace("_"," ").title()

            st.markdown(f'<div class="disease">🌿 {disease_name}</div>', unsafe_allow_html=True)

            st.markdown(f'<div class="conf">Confidence: {conf:.2f}%</div>', unsafe_allow_html=True)

            st.progress(conf/100)

            st.markdown(f'<div class="time">📅 {time}</div>', unsafe_allow_html=True)

        st.markdown('</div>', unsafe_allow_html=True)


# ---------------- LOGOUT ---------------- #

col1,col2 = st.columns([8,1])

with col2:
    if st.button("Logout"):
        st.session_state.user = None
        st.switch_page("Dash-Board.py")


# ---------------- FOOTER ---------------- #

st.markdown("""
<hr>

<div class="footer">

🌿 AI Powered Plant Disease Detection  
<br>
Built with Streamlit & Deep Learning

</div>
""", unsafe_allow_html=True)