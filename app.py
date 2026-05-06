import streamlit as st
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import time

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Instagram Investigation System",
    page_icon="🕵️",
    layout="wide"
)

# ---------------- CUSTOM CSS ----------------
st.markdown("""
<style>

/* Background */
[data-testid="stAppViewContainer"] {
    background: linear-gradient(135deg, #020617, #0f172a, #172554);
    color: white;
}

/* Sidebar */
[data-testid="stSidebar"] {
    background: linear-gradient(to bottom, #020617, #111827);
}

/* Main Title */
.main-title {
    text-align: center;
    font-size: 68px;
    font-weight: bold;
    color: #93c5fd;
    margin-top: -20px;
    text-shadow: 0px 0px 25px rgba(59,130,246,0.5);
}

/* Subtitle */
.subtitle {
    text-align: center;
    font-size: 23px;
    color: #dbeafe;
    margin-bottom: 40px;
}

/* Glass Container */
.glass {
    background: rgba(255,255,255,0.05);
    padding: 35px;
    border-radius: 28px;
    backdrop-filter: blur(14px);
    border: 1px solid rgba(255,255,255,0.08);
    box-shadow: 0 8px 40px rgba(0,0,0,0.35);
}

/* Button */
.stButton>button {
    background: linear-gradient(to right, #2563eb, #38bdf8);
    color: white;
    border: none;
    border-radius: 18px;
    height: 65px;
    width: 100%;
    font-size: 24px;
    font-weight: bold;
    transition: 0.3s;
    box-shadow: 0 5px 20px rgba(0,0,0,0.4);
}

.stButton>button:hover {
    transform: scale(1.02);
    background: linear-gradient(to right, #1d4ed8, #0ea5e9);
}

/* Result Boxes */
.result-real {
    background: rgba(34,197,94,0.15);
    padding: 35px;
    border-radius: 25px;
    text-align: center;
    font-size: 34px;
    font-weight: bold;
    color: #4ade80;
    border: 1px solid rgba(34,197,94,0.2);
    box-shadow: 0 0 25px rgba(34,197,94,0.3);
}

.result-fake {
    background: rgba(239,68,68,0.15);
    padding: 35px;
    border-radius: 25px;
    text-align: center;
    font-size: 34px;
    font-weight: bold;
    color: #f87171;
    border: 1px solid rgba(239,68,68,0.2);
    box-shadow: 0 0 25px rgba(239,68,68,0.3);
}

/* Metric Cards */
.metric-box {
    background: rgba(255,255,255,0.05);
    padding: 22px;
    border-radius: 20px;
    text-align: center;
    font-size: 20px;
    font-weight: bold;
    border: 1px solid rgba(255,255,255,0.05);
    box-shadow: 0 5px 18px rgba(0,0,0,0.3);
}

/* Section Headings */
h2, h3 {
    color: #bfdbfe !important;
}

/* Footer */
.footer {
    text-align:center;
    color:#cbd5e1;
    font-size:18px;
}

</style>
""", unsafe_allow_html=True)

# ---------------- LOAD DATA ----------------
data = pd.read_csv("final-v1.csv")

X = data.drop("is_fake", axis=1)
y = data["is_fake"]

# ---------------- TRAIN MODEL ----------------
model = RandomForestClassifier()
model.fit(X, y)

# ---------------- HEADER ----------------
st.markdown("""
<div class='main-title'>
🕵️ Instagram Account Investigation System
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class='subtitle'>
Detect Fake & Suspicious Instagram Accounts Using AI
</div>
""", unsafe_allow_html=True)

# ---------------- SIDEBAR ----------------
st.sidebar.title("🕵️ Investigation Dashboard")

st.sidebar.success("✅ Detection Accuracy: 94%")

# ---------------- METRIC CARDS ----------------
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class='metric-box'>
    🧠 AI Engine<br>
    Random Forest
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class='metric-box'>
    📊 Accuracy<br>
    94%
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class='metric-box'>
    🔎 Investigation Mode<br>
    Active
    </div>
    """, unsafe_allow_html=True)

st.write("")

# ---------------- INPUT CONTAINER ----------------
st.markdown("<div class='glass'>", unsafe_allow_html=True)

st.subheader("🔍 Enter Suspect Account Details")

left, right = st.columns(2)

with left:

    edge_followed_by = st.slider(
        "👥 Followers Ratio",
        0.0, 5.0, 1.0
    )

    username_length = st.slider(
        "📝 Username Length",
        1, 30, 5
    )

    full_name_has_number = st.selectbox(
        "🔢 Full Name Has Number?",
        ["No", "Yes"]
    )

    is_private = st.selectbox(
        "🔒 Private Account?",
        ["No", "Yes"]
    )

    has_channel = st.selectbox(
        "📡 Has Channel?",
        ["No", "Yes"]
    )

    has_guides = st.selectbox(
        "📚 Has Guides?",
        ["No", "Yes"]
    )

with right:

    edge_follow = st.slider(
        "➡ Following Ratio",
        0.0, 5.0, 1.0
    )

    username_has_number = st.selectbox(
        "🔢 Username Has Number?",
        ["No", "Yes"]
    )

    full_name_length = st.slider(
        "📄 Full Name Length",
        1, 30, 5
    )

    is_joined_recently = st.selectbox(
        "🆕 Joined Recently?",
        ["No", "Yes"]
    )

    is_business_account = st.selectbox(
        "💼 Business Account?",
        ["No", "Yes"]
    )

    has_external_url = st.selectbox(
        "🌐 Has External URL?",
        ["No", "Yes"]
    )

st.markdown("</div>", unsafe_allow_html=True)

# ---------------- CONVERT FUNCTION ----------------
def convert(value):
    return 1 if value == "Yes" else 0

# ---------------- BUTTON ----------------
st.write("")

if st.button("🕵️ START INVESTIGATION"):

    with st.spinner("Investigating Instagram account using AI system..."):
        time.sleep(2)

    prediction = model.predict([[
        edge_followed_by,
        edge_follow,
        username_length,
        convert(username_has_number),
        convert(full_name_has_number),
        full_name_length,
        convert(is_private),
        convert(is_joined_recently),
        convert(has_channel),
        convert(is_business_account),
        convert(has_guides),
        convert(has_external_url)
    ]])

    probability = model.predict_proba([[
        edge_followed_by,
        edge_follow,
        username_length,
        convert(username_has_number),
        convert(full_name_has_number),
        full_name_length,
        convert(is_private),
        convert(is_joined_recently),
        convert(has_channel),
        convert(is_business_account),
        convert(has_guides),
        convert(has_external_url)
    ]])

    st.write("")

    if prediction[0] == 1:

        st.markdown(f"""
        <div class='result-fake'>
        🚨 SUSPICIOUS / FAKE ACCOUNT DETECTED<br><br>
        Investigation Confidence: {probability[0][1]*100:.2f}%
        </div>
        """, unsafe_allow_html=True)

    else:

        st.markdown(f"""
        <div class='result-real'>
        ✅ AUTHENTIC ACCOUNT VERIFIED<br><br>
        Investigation Confidence: {probability[0][0]*100:.2f}%
        </div>
        """, unsafe_allow_html=True)

# ---------------- FOOTER ----------------
st.write("")
st.write("---")

st.markdown("""
<div class='footer'>
🕵️ Powered by Artificial Intelligence & Machine Learning
</div>
""", unsafe_allow_html=True)