from math import factorial as fact


def calc_factorial(number):
    if number < 0:
        print("Sorry I can't do it for negative numbers")
    elif number == 0:
        print("The factorial of 0 is 1")
    elif number > 1:
        print(fact(number))

