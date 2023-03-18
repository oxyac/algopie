import numpy as np
from numpy.random import default_rng


def recur_factorial(n):
    if n == 1:
        return n
    else:
        return n * recur_factorial(n - 1)


def third_exercise():
    print('\nExercitiu 3')
    n = 8
    print("Factorial al elementul 8: %s" % recur_factorial(n))
