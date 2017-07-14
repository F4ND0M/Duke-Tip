import numpy

words = ["dog", "cat", "rooster", "snake", "sheep", "monkey", "pig", "horse", "dragon", "rabbit", "cow", 'mouse', 'tiger']
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
        #number of times letter not in correctWord
    #if letter is not str : ADJUST AND ADD ONE FOR WORDS WITH DOUBLE LETTERS, ALREADY CHOSEN LETTERS, SPACING, WHEN WORD IS COMPLETED, MORE THAN ONE LETTER TYPED
     #   print "This is not a letter."
        #print "You've already choose this letter"
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