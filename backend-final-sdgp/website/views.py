from flask import Blueprint, render_template, request, flash , jsonify
from flask_login import login_required, current_user
from .models import Note
from . import db
import json
# from transformers import AutoTokenizer
# from transformers import AutoModelForSequenceClassification
# from scipy.special import softmax
views = Blueprint('views', __name__)


@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    return render_template("index.html", user=current_user)
@views.route('/dashboard', methods=['GET', 'POST'])
@login_required
def dashboard():
    return render_template("dashboard.html", user=current_user)

@views.route('/addreview', methods=['GET', 'POST'])
@login_required
def addreview():
    if request.method == 'POST':
        # username = request.form.get('username')
        # title = request.form.get('title')
        # rating = request.form.get('rating')
        note = request.form.get('note')

        if len(note) < 1:
            flash('Note is too short!', category='error')
        else:
            new_note = Note(data=note, user_id=current_user.id)
            db.session.add(new_note)
            db.session.commit()
            flash('Note added!', category='success')
    return render_template("career.html", user=current_user)

@views.route('/viewreview', methods=['GET', 'POST'])
def viewreview():
    return render_template("blog-1.html", user=current_user)

@views.route('/aboutus', methods=['GET', 'POST'])
def aboutus():
    return render_template("about.html", user=current_user)

@views.route('/delete-note', methods=['POST'])
def delete_note():
    note = json.loads(request.data)
    noteId = note['noteId']
    note = Note.query.get(noteId)
    if note:
        if note.user_id == current_user.id:
            db.session.delete(note)
            db.session.commit()

    return jsonify({})


@views.route('/input', methods=['GET', 'POST'])
@login_required
def input():
    note = json.loads(request.data)
    noteId = note['noteId']
    note = Note.query.get(noteId)
    if note:
        if note.user_id == current_user.id:
            result = "Positive"
            print(result)
            return jsonify(result=result)
    return jsonify(error='Note not found or user not authorized')


# @views.route('/predict', methods=['GET',['POST']])
# def predict(data):
#     text = data
#
#     MODEL = f"cardiffnlp/twitter-roberta-base-sentiment"
#     tokenizer = AutoTokenizer.from_pretrained(MODEL)
#     model = AutoModelForSequenceClassification.from_pretrained(MODEL)
#
#     encoded_text = tokenizer(text, return_tensors='pt')
#     output = model(**encoded_text)
#     scores = output[0][0].detach().numpy()
#     scores = softmax(scores)
#     scores_dict = {
#         'roberta_neg': scores[0],
#         'roberta_neu': scores[1],
#         'roberta_pos': scores[2]
#     }
#     print(scores_dict)
#     print(text)

