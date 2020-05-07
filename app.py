from flask import Flask, redirect, url_for, render_template
from questionData import * 
from questionClass import * 

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/MeetTheTeam')
def team():
    return render_template("MeetTheTeam.html")


@app.route('/quiz')
def quiz():
    quiz = Quiz(questionText,questionImages,questionChoices,totalAnswerKey)
    
    return render_template("quiz.html", quiz = quiz, userAnswers = userAnswers)

@app.route('/quizResults')
def quizResults():

    
    
    return render_template("quizResults.html", result = userResult)

@app.route('/contact')
def contact():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True)

