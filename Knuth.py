import math


def fact(number):
    if int(number) != number:
        return None

    if number <= 0:
        return 0
    # to stop going too far
    if number > 150:
        return number

    number = int(number)
    result = 1
    for i in range(1, number + 1):
        result *= i
    return result


def sqrt(number):
    if number <= 0:
        return 0
    return math.sqrt(number)


def floor(number):
    return math.floor(number)


def ceil(number):
    return math.ceil(number)


KnuthActions = [fact, sqrt, floor, ceil]
