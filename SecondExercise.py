import numpy as np
from numpy.random import default_rng


def find_seq(arr):
    seq = []
    temp_seq = []
    for i in arr:
        if i >= 0:
            temp_seq.append(i)
            continue
        if len(temp_seq) > 1:
            last = temp_seq.pop()
            first = temp_seq[0]
            temp_seq.append(first)
            temp_seq[0] = last
            seq.append(temp_seq)
        temp_seq = []
    return seq


def second_exercise():
    print('\nExercitiu 2')

    arr = default_rng().integers(low=-50, high=50, size=100)
    print("Elemente: %s" % arr)
    print(find_seq(arr))
