theNumber = int(raw_input("Find divisor of:"))
numList=range(1,theNumber+1)
divisors = []

for num in numList:
    if theNumber%num == 0:
        divisors.append(num)

print divisors
