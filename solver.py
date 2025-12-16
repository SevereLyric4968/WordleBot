from wordList import WordList
import math

class Solver:
    def __init__(self,feedbackEngine):
        self.feedbackEngine=feedbackEngine
        self.wordlist=None

    def update(self, guess, feedback):
        self.wordlist.filter(guess, feedback)

    def computeEntropy(self,wordList, guess):
        feedbackBuckets={}

        for word in wordList:
            feedback=tuple(self.feedbackEngine.guess(guess,word))
            feedbackBuckets.setdefault(feedback,[]).append(word)

        total=len(wordList)

        entropy=0
        for bucket in feedbackBuckets.values():
            probability=len(bucket)/total
            entropy-=probability*math.log(probability,2)

        return entropy

    def getNextGuess(self,guessList):
        if not guessList:
            return None
        if len(self.wordlist.answers) == 1:
            return self.wordlist.answers[0]
        guess=""
        highestEntropy=0
        for word in guessList:
            entropy=self.computeEntropy(guessList, word)
            if entropy>highestEntropy:
                guess=word
                highestEntropy=entropy
        return guess

    def reset(self):
        self.wordlist.reset()