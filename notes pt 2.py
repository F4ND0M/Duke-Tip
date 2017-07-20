import numpy as np

ones = np.ones(4)
print ones
onesM = np.ones((3, 4))
print onesM
onesM[0][0] = 2
print onesM
ones = ones * 4
ones[2] = 0
print ones
onesM = onesM * ones
print onesM
print onesM.sum()
print onesM.sum(axis = 1)
print onesM.sum(axis = 0)

randomM = np.random.rand(3,4) * 10
randomM[2, 3] = 11
randomM[1, :] = 2
randomM[:, 2] = 3
print randomM

print randomM.max()
print randomM.max(axis = 1)
print randomM.argmax()
print randomM.argmax(axis = 1)
print np.argwhere(randomM == randomM.max())
print randomM.mean()
print np..


print ptps[0]
for i in range[2]:
    print str(i)+ "product id" + str(producttotal purchasesorted[i][0])

while productsprinted <2:
    id = producttoalpurchasessorted[i][0]
    if productpurchadecount[id] >= 2:
        print str(i) + ".product id:" + str(id() +\ " " + productDict[id]
        productsprinted += 1)
    i += 1




maxmovie = moviedata['userID'].max()

userlike = np.zeros((4,5))

for i in range(0, 3):
    userlike[i, 2] = 1

print userlikes

ilike = [4, 2]

ilikeNP = np.zeros(5)

for id in ilike:
    ilikeNP[id] = 1

ilikeNP[3] = 40

print ilikeNP.argmax()

maxID = ilikeNP.argmax()
print maxID
ilikeNP[maxID] = 0
maxID = ilikeNP.argmax()
print maxID

list = np.argwhere(userlike[1,:]==1)
print list
print list.flatten()

maxmovie = 5
userlike = [matrix thingy]

ilike[2, 4]
ilikeNp = np.zeros(maxmovie)
for id in ilike:
    ilikeNP[id] = 1

andSum = ilikeNP *userlike
print andSum.sum(axis = 1)