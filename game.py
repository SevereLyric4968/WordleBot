class Game:
    def __init__(self,answer,FeedbackEngine):
        self.feedbackEngine = FeedbackEngine

        self.answer=answer
        self.guesses=[]
        self.score=0
        self.feedback=[]

    def guess(self,word):
        self.guesses.append(word)
        feedback = self.feedbackEngine.guess(word, self.answer)
        self.feedback=feedback
        self.score+=1

        return feedback

    def is_won(self):
        return self.feedback == [2, 2, 2, 2, 2]

    def is_over(self):
        return len(self.guesses) == 6 or self.is_won()

    def reset(self,word):
        self.guesses=[]
        self.answer=word
        self.score = 0
        self.feedback = []
