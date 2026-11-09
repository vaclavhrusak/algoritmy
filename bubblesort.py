cisla = [21, 95, 46, 10, 86, 57, 29]

n = len(cisla)
 
def bubble_sort(cisla, n):
    for i in range(0, n - 2, +1):
        for j in range(0, n - i - 1, +1):
            if cisla[j] > cisla[j + 1]:
                pomocna = cisla[j]
                cisla[j] = cisla[j + 1]
                cisla[j + 1] = pomocna

    print(cisla)

bubble_sort(cisla, n)