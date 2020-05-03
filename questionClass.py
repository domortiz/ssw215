class Question:
    def __init__(self,questionID,questionText,questionImage,choiceText,answerKey):
        self.questionID = questionID
        self.text = questionText
        self.image = questionImage
        self.choices = choiceText
        self.answerKey = answerKey

class Quiz:
    def __init__(self,questions):
        self.questions = questions
        

    def gradeQuiz(self,answers,outcomes):
        logger = {}
        for show in outcomes:
            logger[show] = 0

        for question in self.questions:
            if question.answerKey[answers[question.questionID]] in logger:
                logger[question.answerKey[answers[question.questionID]]] += 1

        return max(logger, key=logger.get)




