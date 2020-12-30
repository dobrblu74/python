from math import factorial


def fact(n):
    yield factorial(n)


for el in fact(10):
    print(el)
