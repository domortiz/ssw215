from flask import Flask, redirect, url_for, render_template, request
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
    
    return render_template("quiz.html", quiz = quiz)

@app.route('/quizResults', methods = ["POST"])
def quizResults():
    quiz = Quiz(questionText,questionImages,questionChoices,totalAnswerKey)
    for x in range(len(quiz.questions)):
        userAnswers[x+1] = request.form[str(x+1)]
    userResult = quiz.gradeQuiz(userAnswers,quizOutcomes)
    return render_template("quizResults.html",result=userResult)

@app.route('/contact')
def contact():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True)

