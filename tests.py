import q
import random

lst = [random.randint(0, 100) for _ in range(int(input('Кол-во элементов в списке: ')))]

print(lst)
#print(q.insertion_sort(lst))
#print(q.bubble_sort(lst))

#print(q.selection_sort(lst))
a = lst

for i in range(len(a)):
    lst = a[i:]
    print('lst = ', lst)
    minn = min(lst)
    print('min = ', minn)
    index_min = a.index(minn)
    print('index_min = ', index_min)
    a[i], a[index_min] = a[index_min], a[i]
    print('after replace a = ', a)
    print()

    
# пока ничего не работает :'(
