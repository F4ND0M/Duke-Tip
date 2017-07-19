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