from feedback import Feedback

class WordList:
    def __init__(self):
        ogAnswers = self.loadFile("answers.txt")
        ogGuesses = self.loadFile("guesses.txt")

        self.answers = ogAnswers
        self.guesses = ogGuesses

        # save originals for reset
        self.ogAnswers = ogAnswers
        self.ogGuesses = ogGuesses

    def loadFile(self,filename="answers.txt"):
        wordList = []
        with open(filename) as file:
            for word in file:
                wordList.append(word.strip())
        return wordList

    def filter(self,guess,feedbackPattern):
        feedback=Feedback()
        filtered = []
        for word in self.answers:
            if feedback.guess(guess,word) == feedbackPattern:
                filtered.append(word)
        self.answers = filtered
        return self.answers

    def reset(self):
        self.answers=self.ogAnswers
        self.guesses=self.ogGuesses