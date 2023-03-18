import numpy as np
from numpy.random import default_rng


def fibonacci_of(n):
     if n in {0, 1}:  # Base case
         return n
     return fibonacci_of(n - 1) + fibonacci_of(n - 2)

def fourth_exercise():
    print('\nExercitiu 4')
    n = 8
    print("Fibonaci al elementul 8: %s" % fibonacci_of(n))
