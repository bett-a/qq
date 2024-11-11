import sorts
import random
import time


lst = [random.randint(0, 100) for _ in range(int(input('Кол-во элементов в списке: ')))]

print(lst)

print(sorts.insertion_sort(lst))
print(sorts.bubble_sort(lst))
print(sorts.selection_sort(lst))

def continuance(f):
    for i in range(1, 6):
        lst = [random.randint(0, 100) for _ in range(10**i)]
        start = time.time()
        f(lst)
        finish = time.time()
        result = (finish - start) * 1000

