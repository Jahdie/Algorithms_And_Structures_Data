# Отсортируйте по убыванию методом пузырька одномерный целочисленный массив, заданный случайными числами на промежутке
# [-100; 100). Выведите на экран исходный и отсортированный массивы.

from random import randint, uniform

array = [randint(-100, 100) for i in range(10)]


def bubble_sort(lst):
    n = 1
    sorted_list = True
    while n < len(lst):
        for i in range(len(lst) - n):
            if lst[i] < lst[i + 1]:
                lst[i], lst[i + 1] = lst[i + 1], lst[i]
                sorted_list = False
        if sorted_list is True:
            return f"Массив уже отсортирован!"
            break
        else:
            n += 1
    return lst


print(array)
print(bubble_sort(array))
