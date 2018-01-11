#Lambda example
squareofNum = lambda x:x**2
print(squareofNum(99))

#Lambda example by combining map function.
#map function example. map take function and literals as imput and run function by passing literals as inputs function in recurssive way
numList=[1,3,4,6,99,888]
squareofNum = map(lambda x:x**2,numList)
print squareofNum
