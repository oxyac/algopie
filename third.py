import pprint
from datetime import date

from numpy.random import default_rng


class Student:
    _id = 0

    def __init__(self, name, surname, date, group):
        Student._id += 1
        self.name = name
        self.surname = surname
        self.date = date
        self.group = group
        self.id = Student._id

    def __repr__(self):
        return "id:%d Nume:% s Prenume:% s" % (self.id, self.name, self.surname)



def exercice():
    print('\nExercitiu 3')
    arr = [
        Student("asd", "adsd", date.today(), "INFa221"),
        Student("dad", "adsd", date.today(), "INFa2212"),
        Student("asasdasdd", "asd", date.today(), "INFa221"),
        Student("asasdasdd", "addsd", date.today(), "INFa221")
    ]

    pprint.pp(arr, compact=True, sort_dicts=False)
    while True:
        r = int(input('Selectati index studentul: '))
        d = next(item for item in arr if item.id == r)
        v = int(input('Selectati valoarea de modificat (1 - Nume, 2 - Prenume): '))
        s = input('Selectati valoarea noua: ')
        if v == 1:
            d.name = s
        else:
            d.surname = s

        print(arr)
        break
