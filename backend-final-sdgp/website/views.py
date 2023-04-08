import sqlite3
from sqlite3 import Error
from flask import Blueprint, render_template, request, flash , jsonify
from flask_login import login_required, current_user
from .models import Note
from . import db
import json
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
    print(noteId)
    conn = sqlite3.connect('./instance/database.db')
    cursor = conn.cursor()
    cursor.execute("SELECT data from Note where id=?",(noteId,))
    data = cursor.fetchall()
    print(data)
    conn.close()
    return 'Data printed in terminal'
# def input():
#     data = request.json
#     noteId = data['noteId']
#     print(noteId)
#     note = json.loads(request.data)
#     # noteId = note['noteId']
#     note = Note.query.get(noteId)
#     print(note)
#     if note:
#         if note.user_id == current_user.id:
#             result = "Positive"
#             print(result)
#             # return jsonify(result=result)
#             return render_template('career.html', result=result, user=current_user)
#     return jsonify(error='Note not found or user not authorized')
# def input():
#     data = request.json
#     noteId = data['noteId']
#     result = "result"
#     if (request.method == "GET"):
#         with sqlite3.connect("./instance/database.db") as con:

#             cursor = con.cursor()

#             try:
#                 cursor.execute( "SELECT data from Note where id=?",(noteId))
#                     # "SELECT marks.std_id,student.std_fname,student.std_lname,SUM(marks) as total_marks FROM Marks marks JOIN Student student ON marks.std_id = student.std_id WHERE date = CURRENT_DATE GROUP BY marks.std_id;")

#                 rows = cursor.fetchall()
#                 noteList = rows[0]
#                 result = "Positive"
#                 return render_template("career.html", result=result, user=current_user)
#             except Error as e:
#                 print(e)
#         return render_template("career.html", user=current_user)





