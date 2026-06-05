
import streamlit as st
from predict import predict_disease
from database import cursor, conn
from style import load_css
import os
import json

load_css()

# ---------------- LOGIN CHECK ---------------- #

if "user" not in st.session_state or st.session_state.user is None:

    st.warning("⚠ Please login first to use this page.")

    if st.button("Go to Login"):
        st.switch_page("pages/Login.py")

    st.stop()

# ---------------- PAGE TITLE ---------------- #

st.title("Upload Plant Image")

# ---------------- IMAGE UPLOAD ---------------- #

image = st.file_uploader("Upload Leaf Image", type=["jpg", "png", "jpeg"])

if image:

    st.image(image, width=350)

    # Detect disease button
    if st.button("Detect Disease"):

        results = predict_disease(image)

        disease, confidence = results[0]

        # Store results in session state
        st.session_state["detected_disease"] = disease
        st.session_state["confidence"] = confidence
        st.session_state["results"] = results

        # Save uploaded image
        os.makedirs("uploads", exist_ok=True)
        path = f"uploads/{image.name}"

        with open(path, "wb") as f:
            f.write(image.getbuffer())

        # Save history to database
        cursor.execute(
            "INSERT INTO history(email,image_path,disease,confidence,predictions) VALUES(?,?,?,?,?)",
            (
                st.session_state["user"],
                path,
                disease,
                confidence,
                json.dumps(results)
            )
        )

        conn.commit()

# ---------------- SHOW RESULTS ---------------- #

if "detected_disease" in st.session_state:

    disease = st.session_state["detected_disease"]
    confidence = st.session_state["confidence"]
    results = st.session_state["results"]

    st.success(f"Disease: {disease}")
    st.info(f"Confidence: {confidence:.2f}%")

    st.subheader("Top 5 Predictions")

    for d, c in results:
        st.write(f"{d} — {c:.2f}%")
        st.progress(int(c))
    
    # Gemini AI button
    

# ---------------- LOGOUT BUTTON ---------------- #

col1, col2 = st.columns([8, 1])

with col2:

    if st.button("Logout"):

        st.session_state.user = None
        st.switch_page("Dash-Board.py")
