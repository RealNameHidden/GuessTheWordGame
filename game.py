class game:
    """This class is a model of a game, contains the data models for the different variables"""
    gameCount = 0
    word = ""
    badGuesses = 0
    missedLetters = 0
    gamesList = []
    result = ' ';
    score = 0
    guessString = "----"
    guessList = list(guessString)
    charList = []
    turnedLetters = 0
    gameEndFlag = False

    def updateGuessList(self, l):
        """This method updates the turned over letters"""
        i = 0
        for ch in self.charList:
            if ch.__eq__(l):
                self.guessList[i] = ch
            i = i + 1

    def calculateScore(self, letterScore):
        """This method calculates the score when a guess is correct"""
        i = 0
        x = None

        for ch in self.guessList:

            if ch != '-':
                # For every turned character get the frequency score
                self.score += letterScore[ch]
                self.turnedLetters += 1
            elif ch == '-':
                # For every unturned character get the frequency score
                x = self.charList[i]
                self.score = self.score + letterScore[x]
            i += 1
        if self.turnedLetters == 0:
            self.score = round(self.score - (self.badGuesses * 10), 2)
        else:
            self.score = round((self.score / self.turnedLetters) - (self.badGuesses * 10), 2)

    def calculateLostScore(self, letterScore):
        """This method calculates the minus points when a player gives up"""
        i = 0
        for ch in self.guessList:
            if ch == '-':
                # For every character that is unturned get the frequency score and subtract
                x = self.charList[i]
                self.score = round(self.score - letterScore[x], 2)
            i += 1
