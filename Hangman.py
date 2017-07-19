import numpy

wrongGuess = 0

def hangman(wrong): #hangman picture
    if wrong >= 1:
        print'    |-----'
        print'    |    |'
        print'    |    O'
    else:
        print'    |-----'
        print'    |    |'
    if wrong == 2:
        print'    |    |'
    if wrong == 3:
        print'    |   /|'
    if wrong >= 4:
        print'    |   /|\\'
    else:
        print'    |'
    if wrong == 5:
        print'    |   /'
    elif wrong >= 6:
        print'    |   / \\'
    else:
        print'    |'
        print'    |'
        print'    |'
        print'---------'

def printBlanks(word): #if the word is solved
    solved = True
    for l in word:
        if l in correct:
            print l + " ",
        else:
            print "_ ",
            solved = False
    print ""
    return solved

words = ["dog", "cat", "rooster", "snake", "sheep", "monkey", "pig", "horse", "dragon", "rabbit", "cow", 'mouse', 'tiger', 'copper', 'explain', 'ill-fated', 'truck', 'neat', 'unite', 'branch', 'educated', 'tenuous', 'hum', 'decisive', 'notice']
correctWord = numpy.random.choice(words)#random word
correct = []
incorrect = []
guesses = []

while True:
    hangman(wrongGuess)
    solved = printBlanks(correctWord)
    if solved:
        print('You have won!')
        again = raw_input("Do you want to play again? ")
        if again == "yes":  # , "y", "Yes", "Y":
            wrongGuess == 0
        elif again == "no":  # , "n", "No", "N":
            print "Thank you for playing."
            exit (0)
        else:
            print "This is not a valid answer."
            exit (0)
    letter = raw_input("Guess a letter: ")
    if letter in guesses: #words chosen more than once
        print "You have already choose this letter."
    guesses.append(letter) #to make sure word isnt chosen twice
    if letter in correctWord:
        correct.append(letter)
    else:
        print "Incorrect."
        wrongGuess += 1
    if wrongGuess == 6: #when hangman is completed
        print'    |-----'
        print'    |    |'
        print'    |    O'
        print'    |   /|\\'
        print'    |   / \\'
        print'    |'
        print'---------'
        print "You have lost."
        print "The word was : " + correctWord
        while True:
            again = raw_input("Do you want to play again? ")
            if again == "yes":#, "y", "Yes", "Y":
                wrongGuess == 0
            elif again == "no":#, "n", "No", "N":
                print "Thank you for playing."
                exit(0)
            else:
                print "This is not a valid answer."
                exit(0)