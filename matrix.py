import numpy as np

fivefour = np.ones((5, 4))
print fivefour

fourone = np.zeros((4))
fourone[0] = 1
print fourone

fives = fivefour * fourone
print fives

fives[1, 2] = 10
print fives * 2

print fives.sum()
print fives.max(axis = 1)
print fives.mean(axis = 0)