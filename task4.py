import itertools


def power_of_two():
    n = 1
    while True:
        yield n
        n *= 2


def func_calculator(days):
    total = 0
    for i, n in enumerate(itertools.islice(power_of_two(), days)):
        total += n
        print('your pay for {} is {}'.format(i + 1, n))
    print('your total is {}'.format(total))


func_calculator(int(input("Enter your number: ")))
