import streamlit as st
from style import load_css

st.set_page_config(
    layout="wide",
    initial_sidebar_state="expanded"
)

load_css()

# ---------------- SIDEBAR ---------------- #

st.sidebar.markdown("""
<style>

[data-testid="stSidebar"]{
background: linear-gradient(180deg,#1b5e20,#2e7d32,#66bb6a);
}

.sidebar-logo{
text-align:center;
padding:10px;
}

.sidebar-logo img{
border-radius:20px;
box-shadow:0 4px 15px rgba(0,0,0,0.4);
}

.sidebar-title{
color:white;
font-size:24px;
font-weight:bold;
margin-top:10px;
}

.sidebar-desc{
color:white;
font-size:14px;
opacity:0.9;
}

</style>

<div class='sidebar-logo'>

<img src="https://cdn-icons-png.flaticon.com/512/628/628283.png" width="80">

<div class='sidebar-title'>Plant AI</div>

<div class='sidebar-desc'>
Disease Detection System
</div>

</div>

<hr style="border:1px solid rgba(255,255,255,0.3);">

<h3 style='color:white;'>Navigation</h3>

""", unsafe_allow_html=True)

# ---------------- MAIN PAGE STYLE ---------------- #

st.markdown("""
<style>

.stApp{
background: linear-gradient(135deg,#e8f5e9,#ffffff);
font-family: 'Segoe UI';
}

.title{
text-align:center;
font-size:48px;
font-weight:bold;
color:#1b5e20;
margin-top:20px;
}

.subtitle{
text-align:center;
font-size:20px;
color:#555;
margin-bottom:30px;
}

.card{
background:white;
padding:35px;
border-radius:18px;
box-shadow:0 10px 25px rgba(0,0,0,0.15);
transition:0.3s;
}

.card:hover{
transform: translateY(-8px);
box-shadow:0 15px 40px rgba(0,0,0,0.2);
}

.stButton>button{
background: linear-gradient(90deg,#2e7d32,#66bb6a);
color:white;
border:none;
border-radius:12px;
height:48px;
width:220px;
font-weight:bold;
transition:0.3s;
}

.stButton>button:hover{
transform:scale(1.05);
background: linear-gradient(90deg,#1b5e20,#43a047);
}

.footer{
text-align:center;
color:#444;
font-size:14px;
padding-top:20px;
}

</style>
""", unsafe_allow_html=True)

# ---------------- HEADER ---------------- #

st.markdown('<p class="title">🌿 AI Plant Disease Detection</p>', unsafe_allow_html=True)

st.markdown('<p class="subtitle">Detect crop diseases using Deep Learning</p>', unsafe_allow_html=True)

# ---------------- FEATURE CARDS ---------------- #

col1,col2,col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="card" style="text-align:center">
    <h2>📸</h2>
    <b>Upload Leaf Images</b><br>
    <p style="color:gray">Upload crop leaf photos for AI analysis</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="card" style="text-align:center">
    <h2>🤖</h2>
    <b>AI Disease Detection</b><br>
    <p style="color:gray">Deep learning model scans diseases</p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="card" style="text-align:center">
    <h2>📊</h2>
    <b>Prediction Results</b><br>
    <p style="color:gray">Get instant disease prediction</p>
    </div>
    """, unsafe_allow_html=True)

st.write("")

# ---------------- HOW TO USE ---------------- #

st.markdown("### 📌 How to use")

st.markdown("""
<div class="card">

1️⃣ **Create an account**  
2️⃣ **Login to the system**  
3️⃣ **Upload a plant leaf image**  
4️⃣ **Get disease predictions instantly**

</div>
""", unsafe_allow_html=True)

# ---------------- USER SESSION ---------------- #

if "user" in st.session_state and st.session_state["user"]:
    st.success(f"Welcome {st.session_state['user']}")

# ---------------- FOOTER ---------------- #

st.markdown("""
<hr>

<div class="footer">

🌿 AI Powered Plant Disease Detection <br>
Built with Streamlit & Deep Learning

</div>
""", unsafe_allow_html=True)