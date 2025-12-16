from feedback import Feedback
from solver import Solver
from gameManager import GameManager
from wordList import WordList
import time
import utils
def main():
    feedbackEngine = Feedback()
    wordList = WordList()
    solver = Solver(feedbackEngine)

    manager = GameManager(solver, feedbackEngine, WordList())
    #manager.play("radar")
    manager.simulateAll(wordList.answers)

    #print(feedbackEngine.guess("cacao","caddy"))

if __name__ == "__main__":
    main()
