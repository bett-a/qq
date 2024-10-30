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
    for i in range(len(a) - 1):
        tmp = a[i]
        j = i + 1
        if tmp > a[j]:
            a[i], a[j] = a[j], a[i]

        return a

def selection_sort(a):
    for i in range(len(a)):
        lst = a[i:]
        minn = min(lst)
        index_min = a.index(minn)
        a[i], a[index_min] = a[index_min], a[i]
    return a
