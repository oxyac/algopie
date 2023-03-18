import pprint
from datetime import date

from numpy.random import default_rng


def exercice():
    print('\nExercitiu 2')
    arr = [
        {'id': 1, 'Name': 'asd', 'Surname': '321', 'Date': date.today(), 'Group': 'INFa'},
        {'id': 2, 'Name': 'asd', 'Surname': '321', 'Date': date.today(), 'Group': 'INFa'},
        {'id': 3, 'Name': 'asd', 'Surname': '321', 'Date': date.today(), 'Group': 'INFa'},
        {'id': 4, 'Name': 'asd', 'Surname': '321', 'Date': date.today(), 'Group': 'INFa'}
    ]

    r = input('Selectati Nume: ')
    c = input('Selectati Prenume: ')
    d1 = int(input('Selectati Year: '))
    d2 = int(input('Selectati Month: '))
    d3 = int(input('Selectati Day: '))
    d = date(d1, d2, d3)
    g = input('Selectati Grupa: ')

    new_student = {'Name': r, 'Surname': c, 'Date': d, 'Group': g}
    arr.append(new_student)
    pprint.pp(arr, compact=True, sort_dicts=False)
    while True:
        r = int(input('Selectati index studentul: '))
        d = next(item for item in arr if item["id"] == r)
        v = int(input('Selectati valoarea de modificat (1 - Nume, 2 - Prenume): '))
        s = input('Selectati valoarea noua: ')
        if (v == 1):
            d["Name"] = s
        else:
            d["Surname"] = s

        print(arr)
        break
