import numpy

words = ["dog", "cat", "chicken", "snake", "sheep"]

correctWord = numpy.random.choice(words)

print '_ ' * len(correctWord)
print raw_input('Guess a letter:')
if
print correctWord