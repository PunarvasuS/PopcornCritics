from flask import Flask, render_template, render_template, redirect, url_for, request
from __init__ import app

import markdown

from cruddy.app_crud import app_crud
from cruddy.app_crud_api import app_crud_api

app.register_blueprint(app_crud)
app.register_blueprint(app_crud_api)

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template("index.html")


def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'MOVIEREVIEW' or request.form['password'] != 'avengers':
            error = 'Invalid Credentials. Please try again.'
        else:
            return render_template('index.html')
    return render_template('login.html', error=error)

@app.route('/top')
def top():
    return render_template("top.html")

@app.route('/random')
def random():
    return render_template("random.html")

@app.route('/quiz')
def quiz():
    return render_template("pages/quiz.html")

@app.route('/calendar')
def calendar():
    return render_template("calendar.html")

@app.route('/clubRoster')
def clubRoster():
    return render_template("clubRoster.html")

@app.route('/join')
def join():
    return render_template("join.html")

@app.route('/notes')
def notes():
    return render_template("notes.html")

@app.route('/learn')
def learn():
    return render_template("learn.html")

if __name__ == "__main__":
    # runs the application on the repl development server
    app.run(debug=True, port="5222")