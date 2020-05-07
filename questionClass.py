from questionData import userResult

class Question:
    def __init__(self,questionID,questionText,questionImage,choiceText):
        self.questionID = questionID
        self.text = questionText
        self.image = questionImage
        self.choices = choiceText
        
    def __str__(self):
        output = []
        output.append(self.questionID)
        output.append(self.text)
        output.append(self.image)
        output.append(self.choices)
        output.append(self.answerKey)
        return str(output)

class Quiz:
    def __init__(self,questionTexts,questionImages,choiceTexts,answerKey):
        self.questions = []
        self.answerKey = answerKey
        for x in range(len(questionTexts)):
            self.questions.append(Question(x+1,questionTexts[x+1],questionImages[x+1],choiceTexts[x+1]))
    def __str__(self):
        output = []
        for question in self.questions:
            output.append(str(question))
        return str(output)
    def gradeQuiz(self,answers,outcomes):
        logger = {}
        for show in outcomes:
            logger[show] = 0

        for x in range(len(answers)):
            if self.answerKey[x+1][answers[x+1]] in logger:
                self.answerKey[x+1][answers[x+1]] += 1

        return max(logger, key=logger.get)
    




