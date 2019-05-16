import random

from game import game
from stringDatabase import stringDatabase



class guess:

    gamesList = []
    quitIt = False
    choice = ''
    stringDB = stringDatabase()

    def intialize(self):
       self.stringDB.loadWords()

    def updateGamesList(self,game):
        """This method adds the game objects to a list"""
        self.gamesList.append(game)


    def calculateTotalScore(self):
        """Calculates total score"""
        totalScore = 0
        for xgame in self.gamesList:
            totalScore = totalScore + xgame.score
        return totalScore

    def runGame(self):
        while not self.quitIt:
            currentGame = game()
            currentGame.word = self.stringDB.wordList[random.randint(1, 4030)]
            currentGame.guessString = "----"
            currentGame.guessList = list(currentGame.guessString)
            currentGame.charList = list(currentGame.word)
            print("New game".center(10, '-'))
            print("Guess the word")
            while not currentGame.gameEndFlag:
                # ---------------- Uncomment below line to display the word ------------------
                print(currentGame.word)
                print("Current guess:" + ''.join(currentGame.guessList))
                choice: chr = input("g = guess, t = tell me, l for a letter, and q to quit \n")
                if choice == 'g':
                    # When guess option is selected
                    guessTry = input("Take a guess!\n")
                    if guessTry.__eq__(currentGame.word):
                        print("Son of a gun, you got that right!\n")
                        currentGame.gameEndFlag = True
                        currentGame.result = 'success'
                        currentGame.calculateScore(self.stringDB.letterScore)
                        self.updateGamesList(currentGame)
                    else:
                        print("That's not correct, but that doesn't make you a Simpleton...\n")
                        currentGame.badGuesses += 1
                elif choice == 't':
                    # When user gives up
                    print("that word that you couldn't guess is : " + currentGame.word.upper() + "\nLoser!\n")
                    currentGame.gameEndFlag = True
                    currentGame.result = 'Gave up'
                    currentGame.calculateLostScore(self.stringDB.letterScore)
                    self.updateGamesList(currentGame)
                elif choice == 'l':
                    # When user wants to turn a letter
                    l = input("Type the letter\n")
                    if l in currentGame.word:
                        print("That's one of the letters in the word!\n")
                        currentGame.updateGuessList(l)
                        if currentGame.guessList.__eq__(currentGame.charList):
                            print("You got'em all, Lucky you!\n")
                            currentGame.result = 'Success'
                            currentGame.calculateScore(self.stringDB.letterScore)
                            self.updateGamesList(currentGame)
                            currentGame.gameEndFlag = True
                    else:
                        print("Take another guess, you might get lucky ;)\n")

                elif choice == 'q':
                    # When user wants to quit
                    print("You Quitter!\n\n")
                    currentGame.gameEndFlag = True
                    self.quitIt = True
                    print("Score board")
                    print("no. " + "word " + "result " + "Bad guesses " + "Missed letters " + "score ")
                    print("-----------------------------------------")
                    for eachGame in self.gamesList:
                        print(self.gamesList.index(eachGame) + 1, eachGame.word, eachGame.result, eachGame.badGuesses,
                              eachGame.missedLetters, eachGame.score)

                    print("-------------------")
                    print("FINAL SCORE: ", round(self.calculateTotalScore(), 2))

if __name__ == '__main__':
        start = guess()
        start.intialize()
        start.runGame()