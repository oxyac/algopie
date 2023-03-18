from combinatorics import custom_combinations, factorial, custom_comb, custom_arr, custom_permutations

if __name__ == '__main__':

    print('Exercitiu 1')

    print("Setatil pe n si pe m astfel incat n <= 20 iar m <=n: ")
    n = int(input("n: "))
    m = int(input("m: "))
    while m > n:
        print("Incercati inca o data")
        n = int(input("n: "))
        m = int(input("m: "))

    print("a) Numarul de permutari a elementelor multimii de lungime %d este %d" % (n, factorial(n)))
    print("b) Numarul de combinari a elementelor multimii de lungime %d a cate %d elemente este %d" % (
        n, m, custom_comb(n, m)))
    print("c) Numarul de aranjamente a elementelor multimii de lungime %d luate cate %d elemente este %d" % (
        n, m, custom_arr(n, m)))

    print('\nExercitiu 2')
    print('\nIntroduceti 4 elemente vectorul')

    arr = []
    i = 1
    while len(arr) < 4:
        arr.append(input('%d :' % i))
        i += 1

    k = 3
    print("Vector sursa: %s , Numar de elemente: %s" % (arr, k))

    print('Combinari: %s' % list(custom_combinations(arr, k)))
    print('Arranjamente: %s' % list(custom_permutations(arr, k)))
