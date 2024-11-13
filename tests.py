import sorts
import random
import time


#lst = [random.randint(0, 100) for _ in range(int(input('Кол-во элементов в списке: ')))]

#print(lst)

#print(sorts.quick_sort(lst))
#print(sorts.insertion_sort(lst))
#print(sorts.bubble_sort(lst))
#print(sorts.selection_sort(lst))



def continuance():
    times = list()
    for i in range(1, 6):
        lst = [random.randint(0, 100) for _ in range(10**i)]
        start = time.time()
        sorts.bubble_sort(lst)
        finish = time.time()
        result = (finish - start) * 1000
        times.append(result)
    return times

def T(lst):
    start = time.time()
    sorts.selection_sort(lst)
    finish = time.time()
    result = (finish - start) * 1000

    return result

l = [random.randint(0, 100) for _ in range(10**1)]
print(T(l))

l = [random.randint(0, 100) for _ in range(10**2)]
print(T(l))

l = [random.randint(0, 100) for _ in range(10**3)]
print(T(l))

l = [random.randint(0, 100) for _ in range(10**4)]
print(T(l))

l = [random.randint(0, 100) for _ in range(10**5)]
print(T(l))

