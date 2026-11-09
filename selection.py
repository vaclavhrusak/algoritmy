cisla = [21, 95, 46, 10, 86, 57, 29]
n = len(cisla)

def selection_sort(cisla, n):
    for i in range(0, n - 1, +1):
        m = i

        for j in range(i + 1, n, +1):
            if cisla[j] < cisla[m]:
                m = j

        pomocna = cisla[i]
        cisla[i] = cisla[m]
        cisla[m] = pomocna

    print(cisla)

selection_sort(cisla, n)
