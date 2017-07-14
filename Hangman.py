import numpy

words = ["dog", "cat"] #"rooster", "snake", "sheep", "monkey", "pig", "horse", "dragon", "rabbit", "cow", 'mouse', 'tiger']
correctWord = numpy.random.choice(words)
guesses = []

space = '_' * len(correctWord)
letter = raw_input('Guess a letter:')


def hanger():
    print'    |-----'
    print'    |    |'
    print'    |'
    print'    |'
    print'    |'
    print'    |'
    print'    |'
    print'---------'

def man():
    wrong = 0
    for letter in not correctWord:
        wrong += 1
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
        print space
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
for turn in range(1, 30):
    if turn == 1:
        print hanger()
        print space
    letter = raw_input('Guess a letter:')
        #number of times letter not in correctWord
    #if letter is not str : ADJUST AND ADD ONE FOR WORDS WITH DOUBLE LETTERS, SPACING, WHEN WORD IS COMPLETED, MORE THAN ONE LETTER TYPED
     #   print "This is not a letter."
    #if correctWord
    if letter in guesses:
        print "You've already choose this letter."
    guesses.append(letter)
    if letter in correctWord:
        print "Correct!"
        if space <= len(correctWord): #ADJUST
            space = space[:-2]
        space = bytearray(space)
        value = correctWord.index(letter)
        space[value] = letter
        #if len(correctWord) =
        #if letter in correctWord
        print space
        print hanger()