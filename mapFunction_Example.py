
#map function example. map take function and literals as imput and run function by passing literals as inputs function in recurssive way
def squareofNum(x):
    return x**2
numList=[1,3,4,6,99,888]
print "numList:",numList
print map(squareofNum,numList)
