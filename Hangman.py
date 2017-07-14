import numpy

words = ["dog", "cat"] #"rooster", "snake", "sheep", "monkey", "pig", "horse", "dragon", "rabbit", "cow", 'mouse', 'tiger']
correctWord = numpy.random.choice(words)
guesses = []
# if letter is not str : ADJUST AND ADD ONE FOR WORDS WITH DOUBLE LETTERS, SPACING, WHEN WORD IS COMPLETED, MORE THAN ONE LETTER TYPED

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
wrongGuess = 0

for turn in range(1, 30):
    if turn == 1:
        print'    |-----'
        print'    |    |'
        print'    |'
        print'    |'
        print'    |'
        print'    |'
        print'    |'
        print'---------'
        print space
    letter = raw_input('Guess a letter:')
    if letter in guesses:
        print "You've already choose this letter."
    guesses.append(letter)
    if letter in correctWord:
        print "Correct!"
        space = bytearray(space)
        if correctWord.index(letter) == 1:
            value = correctWord.index(letter)
        else:
            value = correctWord.index(letter) + 2
        space[value] = letter
        print space
        print hanger()
    if letter not in correctWord:
        wrongGuess += 1
man(wrongGuess)
def man(wrong):
    if wrong >= 1:
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