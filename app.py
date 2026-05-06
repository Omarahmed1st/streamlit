import streamlit as st
from transformers import pipeline

# Page Config
st.set_page_config(
    page_title="Sentiment Analyzer",
    page_icon="🧠",
    layout="centered"
)

# HuggingFace Model
classifier = pipeline(
    "sentiment-analysis",
    model="distilbert-base-uncased-finetuned-sst-2-english"
)

# Custom CSS
st.markdown("""
<style>

html, body, [class*="css"] {
    background-color: #050816;
    color: white;
    font-family: 'Segoe UI', sans-serif;
}

/* Main container */
.block-container {
    padding-top: 4rem;
    max-width: 850px;
}

/* Title */
.title {
    font-size: 64px;
    font-weight: 800;
    margin-bottom: 10px;
    color: white;
}

/* Subtitle */
.subtitle {
    font-size: 20px;
    color: #bfc7d5;
    margin-bottom: 35px;
}

/* Textarea */
textarea {
    background: #1d2233 !important;
    color: white !important;
    border-radius: 18px !important;
    border: 1px solid #2d3448 !important;
    padding: 20px !important;
    font-size: 18px !important;
}

/* Button */
.stButton button {
    background: linear-gradient(135deg, #ff5f6d, #ff9966);
    color: white;
    border: none;
    border-radius: 14px;
    padding: 12px 26px;
    font-size: 18px;
    font-weight: bold;
    transition: 0.3s;
}

.stButton button:hover {
    transform: scale(1.03);
    opacity: 0.95;
}

/* Result Box */
.result-box {
    margin-top: 30px;
    padding: 24px;
    border-radius: 18px;
    background: #13192b;
    border: 1px solid #283046;
}

.result-label {
    font-size: 28px;
    font-weight: bold;
    margin-bottom: 12px;
}

.result-score {
    font-size: 20px;
    color: #bfc7d5;
}

</style>
""", unsafe_allow_html=True)

# Title
st.markdown(
    '<div class="title">Sentiment Analyzer</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">Analyze sentence sentiment using a BERT model from Hugging Face.</div>',
    unsafe_allow_html=True
)

# Input
text = st.text_area(
    "Sentence",
    placeholder="Type something here...",
    height=180
)

# Analyze Button
if st.button("Analyze sentiment"):

    if text.strip() == "":
        st.warning("Please enter some text.")
    else:

        result = classifier(text)[0]

        label = result["label"]
        score = round(result["score"] * 100, 2)

        if label == "POSITIVE":
            emoji = "😊"
            color = "#22c55e"
        else:
            emoji = "😡"
            color = "#ef4444"

        st.markdown(f"""
        <div class="result-box">

            <div class="result-label" style="color:{color}">
                {emoji} {label}
            </div>

            <div class="result-score">
                Confidence Score: {score}%
            </div>

        </div>
        """, unsafe_allow_html=True)