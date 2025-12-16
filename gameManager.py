import utils
from solver import Solver
from game import Game
import time
class GameManager:

    def __init__(self,solver,feedbackEngine,wordList):
        self.solver=solver
        self.feedbackEngine=feedbackEngine
        self.wordList=wordList
        self.solver.wordlist = self.wordList
        self.results={}

    def play(self,answer):
        print(f"\n--- Starting game for answer: {answer} ---")
        game = Game(answer,self.feedbackEngine)
        self.solver.reset()
        attempts=0
        guesses=[]
        board=[[3]*5 for i in range(6)]

        while not game.is_over():
            if attempts==0:
                guess="raise"
            else:
                guess = self.solver.getNextGuess(self.wordList.answers)

            feedback=game.guess(guess)
            board[attempts]=feedback
            guesses.append(guess)
            print(utils.displayBoard(board,guesses))

            self.solver.update(guess, feedback)
            attempts+=1

            if game.is_won():
                break

        self.results[answer] = {
            "attempts": attempts,
            "won": game.is_won(),
            "guesses": guesses
        }

    def simulateAll(self,wordList):
        totalScore=0
        worstScore=0
        losses=[]
        totalTime=time.perf_counter()
        for word in wordList:
            self.play(word)

            #Average Score
            totalScore+=self.results[word]["attempts"]

            #Losses
            if not(self.results[word]["won"]):
                losses.append(word)

        print(totalScore/len(wordList))
        print(f"Average score: {(totalScore/len(wordList)):.2f} attempts")
        print(f"Losses: {len(losses)} games lost of {len(wordList)}; {losses}.")
        print(f"Total time: {time.perf_counter() - totalTime:.2f} seconds.")
        print(f"Average time: {(time.perf_counter() - totalTime)/len(wordList):.2f} seconds.")

