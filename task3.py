import re

inp = open('input.txt', 'r')
summ = 0

numbers = inp.read()
numbers = re.findall(r'[+-]?\d+?', numbers)
numbers = [int(x) for x in numbers]

for x in numbers:
    summ += x
print(str(summ))

inp.close()
