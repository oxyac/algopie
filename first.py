from numpy.random import default_rng


def exercice():
    print('Exercitiu 1')
    n = int(input('Lista de elemente: '))

    arr = default_rng().integers(50, size=(n, n))

    print(arr)
    while True:
        r = int(input('Selectati rand: ')) - 1
        c = int(input('Selectati coloana: ')) - 1
        v = int(input('Valoarea noua elementul: '))
        arr[r][c] = v
        print(arr)
        break

