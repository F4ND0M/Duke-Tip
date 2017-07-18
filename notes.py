import numpy as np
import matplotlib.pyplot as plt

myRange = np.random.rand(10000000)
mySum = 0

#for number in myRange:
#    mySum += number

mySum = myRange.sum()
print mySum

x = [1, 2, 4, 8]
y = [10, 40, 80, 20]

result = np.polyfit(x, y, 2)
eq = np.poly1d(result)
print eq
print eq(2)

myX = 4
myY = eq(myX)

x2 = np.arange(-40, 90)
yfit = np.polyval(result, x2)
#print yfit

plt.plot(x, y, label = "Points")
plt.plot(x2, yfit, label = "Fit")
#plt.show()
plt.savefig('example.png')

myString = '60.5'
if myString.isalpha():
    print 'alpha'
elif myString.isdigit():
    print 'digit'
else:
    print 'neither'

number = 0

try:
    number = float(myString)
except ValueError:
    print('Exception Happened')

print number * 2