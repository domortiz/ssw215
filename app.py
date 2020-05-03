from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/aboutus')
def team():
    return render_template("aboutus.html")


@app.route('/quiz')
def quiz():
    return render_template("quiz.html")


@app.route('/playlistgenerator')
def playlistgenerator():
    return render_template("playlistgen.html")


if __name__ == "__main__":
    app.run(debug=True)
