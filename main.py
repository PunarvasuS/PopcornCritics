import markdown
from flask import Flask, render_template, render_template, redirect, url_for, request, Blueprint
from flask_login import login_required, current_user
from __init__ import app

from cruddy.app_crud import app_crud
from cruddy.app_crud_api import app_crud_api

app.register_blueprint(app_crud)
app.register_blueprint(app_crud_api)

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

@app.route('/topmoviecode')
def topmoviecode():
    return render_template("learn/topmoviecode.html")

@app.route('/random')
def random():
    return render_template("random.html")

@app.route('/randommoviegeneratorcode')
def randommoviegeneratorcode():
    return render_template("learn/randommoviegeneratorcode.html")

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
@login_required
def notes():
    return render_template("notes.html")

def calculate(ques):
    total = 0
    for i in range(7):
        total = total + int(ques[i])
    quiz1 = round((total/ 35)*100)
    return quiz1

@app.route('/personality/', methods=['GET', 'POST'])
def personality():
    msg = "FINISH THE TEST FIRST"
    ques = []
    for i in range(7):
        ques.append("")
    #    ques[6] = None
    resultpy = 0
    quiz2 = 0
    #for loop to do all the request.form.get instead of a long list
    if request.form:
        for i in range(7):
            reqformval = "ques" + str(i+1)
            ques[i] = request.form.get(reqformval)
            print(ques[i])
        #calculates quiz2
        if ques[0] != "":
            resultpy = calculate(ques)
            quiz2 = 100 - resultpy
        else:
            resultpy = 9999
            #gives message based on whether sun or moon(random item from list)
        if resultpy > quiz2:
            msg = "You are like action, comedy, or romance! Check out our movie API to find suitable movies!" + " "
        else:
            msg = "You are like thriller, horror, or scifi! Check out our movie API to find suitable movies!" + " "

    return render_template("pages/personality.html", result=resultpy, moonp=quiz2, mesg=msg)

@app.route('/moviequizcode')
def moviequizcode():
    return render_template("learn/moviequizcode.html")

@app.route('/learn')
def learn():
    return render_template("pages/learn.html")

@app.route('/login')
def login():
    return render_template("login.html")

if __name__ == "__main__":
    # runs the application on the repl development server
    app.run(debug=True, port="5222")
