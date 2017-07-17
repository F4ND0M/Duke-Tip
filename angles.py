import numpy as np
import matplotlib.pyplot as plt

x = [-40, -29, 0, 20, 40, 60, 80]
y = [65.33333333, 130, 383.6666667, 642.6666667, 717.6666667, 626, 365.3333333]

graph = np.polyfit(x, y, 4)
eq = np.poly1d(graph)

while True:
    angle = raw_input("Type an angle: (type e to exit) ")
    if angle == 'e':
        print "You have exited."
        break
    try:
        print "The distance is " + str(eq(int(angle))) + " inches long."
    except ValueError:
        print "This is not a number. Try again."
        print ""
    print ""
    number = 0

