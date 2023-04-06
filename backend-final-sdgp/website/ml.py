from flask import Blueprint, render_template, request, flash , jsonify
from flask_login import login_required, current_user
import streamlit as st
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

ml = Blueprint('ml', __name__)
@ml.route('/predict', methods=['GET',['POST']])
def predict(data):
    user_input = st.text_input("Please rate our services >>:")
    nltk.download("vader_lexicon")
    s = SentimentIntensityAnalyzer()
    score = s.polarity_scores(user_input)

    if score == 0:
        st.write(" ")
    elif score["neg"] != 0:
        st.write("# Negative 😫 ")
    elif score["pos"] != 0:
        st.write("# Positive 😀 ")