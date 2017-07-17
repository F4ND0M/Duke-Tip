import numpy as np
import matplotlib.pyplot as plt

x = [-40, -29, 0, 20, 40, 60, 80]#angles
y = [65.33333333, 130, 383.6666667, 642.6666667, 717.6666667, 626, 365.3333333]#distances

graph = np.polyfit(x, y, 4)
#to create graph and equation
eq = np.poly1d(graph)

while True:
    angle = raw_input("Type an angle (type e to exit): ")#angle input
    if angle == 'e':#to exit
        print "You have exited."
        break
    try:
        print "The distance is " + str(eq(int(angle))) + " inches long." #prints the distance of the angle
        print eq#prints the equation
    except ValueError:
        print "This is not a number. Try again."#for inputs that aren't numbers
        print ""
    print ""
    number = 0

