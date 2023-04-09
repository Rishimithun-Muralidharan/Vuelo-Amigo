import pickle
from scipy.special import softmax
from transformers import AutoTokenizer, AutoModelForSequenceClassification
from flask import Flask, render_template, request, Blueprint
from flask_login import login_user, login_required, logout_user, current_user

ml = Blueprint('ml', __name__)

def get_sentiment(text):
    MODEL = f"cardiffnlp/twitter-roberta-base-sentiment"
    tokenizer = AutoTokenizer.from_pretrained(MODEL)
    model = AutoModelForSequenceClassification.from_pretrained(MODEL)
    encoded_text = tokenizer(text, return_tensors='pt')
    output = model(**encoded_text)
    
    scores = output[0][0].detach().numpy()
    scores = softmax(scores)
    scores_dict = {
        'Negative' : scores[0],
        'Netural' : scores[1],
        'Positive' : scores[2]
    }
    if(scores[0] > 0.6):
        result = "It's a Negative Review 🙁👎"
    elif(scores[1] > 0.2):
        result = "It's a Neutral Review 😐👊"
    elif(scores[2] > 0.6):
        result = "It's a Positive Review 😊👍"

    return result

def prediction(text):
    result = get_sentiment(text)
    return result