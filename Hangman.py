import numpy

words = ["dog", "cat", "chicken", "snake", "sheep"]
correctWord = numpy.random.choice(words)

space = '_ ' * len(correctWord)

def hanger():
    print'    |-----'
    print'    |    |'
    print'    |'
    print'    |'
    print'    |'
    print'    |'
    print'    |'
    print'---------'

for turn in range(1, 100):
    if turn == 1:
        print hanger()
        print space
    letter = raw_input('Guess a letter:')
    if letter is not str:
        print "This is not a letter."
        #print "You've already choose this letter"
    if letter in correctWord:
        print "Correct!"
        value = correctWord.index(letter)
        correctWord[value]
        space = space.replace(space[value], letter)
        print space
        print hanger()
    elif turn == 1:
        print "Incorrect."
        print'    |-----'
        print'    |    |'
        print'    |    O'
        print'    |'
        print'    |'
        print'    |'
        print'    |'
        print'---------'
    elif turn == 2:
        print "Incorrect."
        print'    |-----'
        print'    |    |'
        print'    |    O'
        print'    |    |'
        print'    |'
        print'    |'
        print'    |'
        print'---------'
    elif turn == 3:
        print "Incorrect."
        print'    |-----'
        print'    |    |'
        print'    |    O'
        print'    |   /|'
        print'    |'
        print'    |'
        print'    |'
        print'---------'
    elif turn == 4:
        print "Incorrect."
        print'    |-----'
        print'    |    |'
        print'    |    O'
        print'    |   /|\\'
        print'    |'
        print'    |'
        print'    |'
        print'---------'
    elif turn == 5:
        print "Incorrect."
        print'    |-----'
        print'    |    |'
        print'    |    O'
        print'    |   /|\\'
        print'    |   /'
        print'    |'
        print'    |'
        print'---------'
    elif turn == 6:
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