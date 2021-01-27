# В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

from random import randint

SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 100

array = [randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
min_item = max_item = array[0]
max_item_index = min_item_index = 0
print(array)

for i in range(len(array)):
    if array[i] > max_item:
        max_item = array[i]
        max_item_index = i
    if array[i] < min_item:
        min_item = array[i]
        min_item_index = i
array[min_item_index], array[max_item_index] = array[max_item_index], array[min_item_index]
print(array)

