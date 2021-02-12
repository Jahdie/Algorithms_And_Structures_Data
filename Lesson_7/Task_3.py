# Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом. Найдите в массиве медиану. Медианой
# называется элемент ряда, делящий его на две равные части: в одной находятся элементы, которые не меньше медианы,
# в другой – не больше медианы.
# Задачу можно решить без сортировки исходного массива. Но если это слишком сложно, то используйте метод сортировки,
# который не рассматривался на уроках.

from random import randint

M = 10
START = 0
STOP = 100
SIZE = 2 * M + 1

array = [randint(START, STOP) for i in range(SIZE)]


def count_sort(lst, max_value):
    index = 0
    counts = [0] * (max_value + 1)

    for item in lst:
        counts[item] += 1

    for i in range(max_value + 1):
        for j in range(counts[i]):
            lst[index] = i
            index += 1
    return lst


def find_median(lst):
    count_sort(array, STOP)
    index_median = len(array) // 2
    return array[index_median]


print(f"В массиве {array} меддиана - {find_median(array)}")
