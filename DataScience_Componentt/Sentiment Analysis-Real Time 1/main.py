from flask import Falsk, render_template

app = flask(__name__)

@app.route('/')
def main():
    return render_template('home_html')