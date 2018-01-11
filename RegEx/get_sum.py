import re

filehand = open("regex_sum_214550.txt")

sumOfNumbers = 0
for line in filehand:
    line = line.rstrip()
    numbers = re.findall('[0-9]+',line)
    if len(numbers)>0:
        sumOfNumbers = sumOfNumbers + sum(list(map(int,numbers)))
print "Sum of numbers:", sumOfNumbers
