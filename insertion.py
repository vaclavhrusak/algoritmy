cisla = [21, 95, 46, 10, 86, 57, 29]

n = len(cisla)
 
def insertion_sort(cisla, n):

    for i in range(1, n):

        klic = cisla[i]

        pozice = i

        for j in range(i - 1, -1, -1):

            if cisla[j] > klic:

                cisla[j + 1] = cisla[j]

                pozice = j

            else:

                break
 
        cisla[pozice] = klic
 
insertion_sort(cisla, n)

print(cisla)

 