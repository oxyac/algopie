import numpy as np
from numpy.random import default_rng


def find_max(array):
    max = 0
    for i in array:
        for k in i:
            if k > max:
                max = k

    return max


def find_impair_by_col(array):
    total_imp = {}
    for idx, i in enumerate(array):
        total_imp[idx] = {}
        for k in i:
            if k % 2 != 0:
                total_imp[idx] = k
    return total_imp


def find_secondary_diagonal(array):
    seq = []
    m = len(array)
    for i in range(m):
        for j in range(m):
            if (i + j) == (m - 1):
                seq.append(array[i][j])

    return seq


def first_exercise():
    print('Exercitiu 1')
    n = int(input('Lista de elemente: '))

    arr = default_rng().integers(50, size=(n, n))
    print("Elemente: %s" % arr)
    print("Element cu valoarea maximum: %d" % find_max(arr))
    print("Elemente pare pe coloana: %s" % find_impair_by_col(arr))
    print("Elemente de diagonala secundara: %s" % find_secondary_diagonal(arr))
