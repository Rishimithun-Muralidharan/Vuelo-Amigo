# import sqlite3
# import string
# from flask import Flask, render_template, request, Blueprint
# from flask_login import login_user, login_required, logout_user, current_user
# import json
# from .models import Note
# from nltk.tokenize import word_tokenize
# from nltk.corpus import stopwords
# from nltk.sentiment.vader import SentimentIntensityAnalyzer
# import nltk
# nltk.download('vader_lexicon')

# ml = Blueprint('ml', __name__)

# def predict(input):
#     lower_case = input.lower() 
#     cleaned_text = lower_case.translate(str.maketrans('' , '' , string.punctuation)) 
#     tokenized_words = word_tokenize(cleaned_text, "english")

#     sid = SentimentIntensityAnalyzer()
#     score = sid.polarity_scores(cleaned_text)['compound']
#     if(score > 0):
#         return "It's a postive review"
#     else:
#         return "It's a negative review"
    
# @ml.route('/input', methods=['GET', 'POST'])
# @login_required
# def input():
#     note = json.loads(request.data)
#     noteId = note['noteId']
#     note = Note.query.get(noteId)
#     print(noteId)
#     conn = sqlite3.connect('./instance/database.db')
#     cursor = conn.cursor()
#     cursor.execute("SELECT data from Note where id=?",(noteId,))
#     data = cursor.fetchall()
#     print(data)
#     # output = predict(data)
#     conn.close()
#     return 'Data printed in terminal'