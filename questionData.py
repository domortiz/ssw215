quizOutcomes = ["Altered Carbon", "Parks and Recreation", "The Good Place", "Tiger King",
                "You", "Black Mirror", "The Witcher", "Castlevania", "Our Planet", "Glee"]

questionText = {1: "Do you like science fiction?", 2: "Do you relish comedy?", 3: "Are characters more important than action?", 4: "How important is realism to you?", 5: "Does peculiarity draw your attention more than anything else?",
                6: "Do you think shows these days lacking in music?", 7: "Do you believe in the power of a curse?", 8: "Do you watch TV to escape the world or to apprecite it?", 9: "Fun?, Fearful?, Freaky?, or Frazzled?", 10: "What is your gut reaction to \"This will be on the test\""}

questionChoices = {1: ["Very Much So", "Only the realistic kind", "Not in the slightest", "Sci Fi? You mean like with swords and magic"], 2: ["Make me laugh until I can't feel my sides", "Jokes are good in moderation", "The more serious the better", "I'm physically incapable of laughter"], 3: ["I'm here to watch people on screen", "In it for the characters, but don't mind some action", "In it for the action, but don't mind some characters", "I only tolerate people cause somebody has to hold the gun"], 4: ["\"Based on a true story\"", "Please keep it believable", "I dunno, I can imagine quite a bit", "Disbelief: Suspended"], 5: ["The weirder the better",
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            "It does catch my eye now and again", "Let's try to be normal everyone", "I am a default human"], 6: ["In fact, I usually only watch musicals", "I would kill for some decent tunes", "Can't hurt", "Only the score"], 7: ["I'm kinda superstitous", "Generally more afraid of those who do", "What a bunch of bologna", "You mean like **** right?"], 8: ["If I wanted the world I'd go outside", "Why is that a binary choice?", "Definitly interested in seeing more of what I know", "Netflix is less expensive than travel"], 9: ["Fun", "Fearful", "Freaky", "Frazzled"], 10: ["I hope so, thats what I'm paying for", "I expected as much", "Great, another thing to not understand", "There's a test!?"]}

userAnswers = {}

totalAnswerKey = {1: {"A": "Altered Carbon", "B": "Black Mirror", "C": "Our Planet", "D": "The Witcher"}, 2: {"A": "Parks and Recreation", "B": "The Good Place", "C": "Tiger King", "D": "You"}, 3: {"A": "Glee", "B": "Black Mirror", "C": "Castlevania", "D": "Altered Carbon"}, 4: {"A": "Tiger King", "B": "Glee", "C": "You", "D": "The Witcher"}, 5: {"A": "You", "B": "Black Mirror", "C": "Parks and Recreation", "D": "Glee"}, 6: {
    "A": "Glee", "B": "Our Planet", "C": "The Witcher", "D": "Altered Carbon"}, 7: {"A": "The Good Place", "B": "Castlevania", "C": "Black Mirror", "D": "Parks and Recreation"}, 8: {"A": "Black Mirror", "B": "The Witcher", "C": "Parks and Recreation", "D": "Our Planet"}, 9: {"A": "Parks and Recreation", "B": "Black Mirror", "C": "Tiger King", "D": "Glee"}, 10: {"A": "Our Planet", "B": "Black Mirror", "C": "The Good Place", "D": "Castlevania"}}

questionImages = {1: "static/images/Question1picture.png", 2: "static/images/Question2picture.png", 3: "static/images/Question3picture.png", 4: "static/images/Question4picture.png", 5: "static/images/Question5picture.png",
                  6: "static/images/Question6picture.png", 7: "static/images/Question7picture.png", 8: "static/images/Question8picture.png", 9: "static/images/Question9picture.png", 10: "static/images/Question10picture.png"}

quizOutcomes = {"Altered Carbon", "Parks and Recreation", "The Good Place", "Tiger King",
                "You", "Black Mirror", "The Witcher", "Castlevania", "Our Planet", "Glee"}

userResult = ""

outcomePictures = {"Altered Carbon": "static/images/carbon.png", "Parks and Recreation": "static/images/parksnrec.png", "The Good Place": "static/images/thegoodplace.png", "Tiger King": "static/images/tigerking.png", "You": "static/images/you.png",
                   "Black Mirror": "static/images/blackmirror.png", "The Witcher": "static/images/witcher.png", "Castlevania": "static/images/castlevania.png", "Our Planet": "static/images/ourplanet.png", "Glee": "static/images/glee.png"}
