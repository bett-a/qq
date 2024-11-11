def insertion_sort(a):
    for i in range(1, len(a)):
        tmp = a[i]
        j = i - 1
        while j >= 0 and a[j] < tmp:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = tmp
    return a

def bubble_sort(a):
    n = len(a)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
    return a

def selection_sort(a):
    for i in range(len(a) - 1):
        index_min = i
        for j in range(i + 1, len(a)):
            if a[j] < a[index_min]:
                index_min = j
        a[i], a[index_min] = a[index_min], a[i]
    return a

