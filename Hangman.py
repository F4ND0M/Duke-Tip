import numpy

words = ["dog", "cat", "chicken", "snake", "sheep"]
correctWord = numpy.random.choice(words)

space = '_' * len(correctWord)

def hanger():
    print'    |-----'
    print'    |    |'
    print'    |'
    print'    |'
    print'    |'
    print'    |'
    print'    |'
    print'---------'

for turn in range(1, 30):
    if turn == 1:
        print hanger()
        print space
    letter = raw_input('Guess a letter:')
    for wrong in range(1, 6):
        wrong = letter not in correctWord
    #if letter is not str :
     #   print "This is not a letter."
        #print "You've already choose this letter"
    if letter in correctWord:
        print "Correct!"
        if space <= len(correctWord):
            space = space[:-1]
        space = bytearray(space)
        value = correctWord.index(letter)
        space[value] = letter
        print space
        print hanger()
    elif wrong == 1:
        print "Incorrect."
        print'    |-----'
        print'    |    |'
        print'    |    O'
        print'    |'
        print'    |'
        print'    |'
        print'    |'
        print'---------'
    elif wrong == 2:
        print "Incorrect."
        print'    |-----'
        print'    |    |'
        print'    |    O'
        print'    |    |'
        print'    |'
        print'    |'
        print'    |'
        print'---------'
    elif wrong == 3:
        print "Incorrect."
        print'    |-----'
        print'    |    |'
        print'    |    O'
        print'    |   /|'
        print'    |'
        print'    |'
        print'    |'
        print'---------'
    elif wrong == 4:
        print "Incorrect."
        print'    |-----'
        print'    |    |'
        print'    |    O'
        print'    |   /|\\'
        print'    |'
        print'    |'
        print'    |'
        print'---------'
    elif wrong == 5:
        print "Incorrect."
        print'    |-----'
        print'    |    |'
        print'    |    O'
        print'    |   /|\\'
        print'    |   /'
        print'    |'
        print'    |'
        print'---------'
    elif wrong == 6:
        print "Incorrect."
        print'    |-----'
        print'    |    |'
        print'    |    O'
        print'    |   /|\\'
        print'    |   / \\'
        print'    |'
        print'    |'
        print'---------'
        print 'You lost.'
        print 'The word was ' + correctWord + '.'