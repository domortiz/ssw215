from flask import Flask, redirect, url_for, render_template, request
import sys
import spotipy
import spotipy.util as util
from questionData import *
from questionClass import *

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/aboutus')
def team():
    return render_template("aboutus.html")


@app.route('/quiz')
def quiz():
    quiz = Quiz(questionText, questionImages, questionChoices, totalAnswerKey)

    return render_template("quiz.html", quiz=quiz)


@app.route('/quizResults', methods=["POST"])
def quizResults():
    quiz = Quiz(questionText, questionImages, questionChoices, totalAnswerKey)
    for x in range(len(quiz.questions)):
        userAnswers[x+1] = request.form[str(x+1)]
    userResult = quiz.gradeQuiz(userAnswers, quizOutcomes)
    resultImage = outcomePictures[userResult]
    return render_template("quizResults.html", result=userResult, resultImage=resultImage)


@app.route('/playlistgenerator', methods=['GET', 'POST'])
def playlistgenerator():
    return render_template("playlistgen.html")


@app.route('/playlistresults', methods=['GET', 'POST'])
def playlistresults():
    '''
    Creates a playlist of recommended songs based on your top 5 Artists!
    Using Spotipy: a Python library to help work with the Spotify Web API
    https://spotipy.readthedocs.io/en/2.12.0/
    '''

    scope = 'user-library-read user-top-read playlist-read-private user-library-modify playlist-read-collaborative playlist-modify-public playlist-modify-private'
    cid = 'd77d13817b264bacb100a71642df973e'
    secret = '7d11f579e22e4b49867fdd8504fe78df'
    redirect_uri = 'http://localhost:8888'
    username = ""

    if len(sys.argv) > 1:
        username = sys.argv[1]  # take username as an argument
    else:
        print("Usage: %s username" % (sys.argv[0],))
        # sys.exit()

    # get user's permission
    token = util.prompt_for_user_token(
        username, scope, cid, secret, redirect_uri)
    if token:
        sp = spotipy.Spotify(auth=token)
        topArtists = sp.current_user_top_artists(limit=5)
        artist_seeds = []
        for artist in topArtists['items']:
            artist_seeds.append(artist['id'])
        id = sp.current_user()['id']
        playlist_id = (sp.user_playlist_create(
            id, "Quaransite Recommendations!", public=True))['id']
        track_ids = []
        rec = sp.recommendations(seed_artists=artist_seeds,
                                 seed_genres=None, seed_tracks=None, limit=20, country=None)
        for track in rec['tracks']:
            track_ids.append(track['id'])

        sp.user_playlist_add_tracks(id, playlist_id, track_ids, position=None)
    else:
        print("Can't get token for", username)

    return render_template("playlistgen.html")


if __name__ == "__main__":
    app.run(debug=True)
