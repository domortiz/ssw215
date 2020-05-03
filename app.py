from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/MeetTheTeam')
def team():
    return render_template("MeetTheTeam.html")

@app.route('/quiz')
def quiz():
    return render_template("quiz.html")

@app.route('/contact')
def contact():
    return render_template("contact.html")

if __name__ == "__main__":
    app.run(debug=True)


