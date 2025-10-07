def readFile(file):
    with open(file) as file:
        for words in file:
            print(words)

readFile("wordle-La.txt")
readFile("wordle-Da.txt")