# 1). Проанализировать скорость и сложность одного любого алгоритма из разработанных в рамках домашнего задания первых
# трех уроков.
# Примечание. Идеальным решением будет:
# ● выбрать хорошую задачу, которую имеет смысл оценивать (укажите в комментарии какую задачу вы взяли),
# ● написать 3 варианта кода (один у вас уже есть),
# ● проанализировать 3 варианта и выбрать оптимальный,
# ● результаты анализа вставить в виде комментариев в файл с кодом (не забудьте указать, для каких N вы проводили
# замеры),
# ● написать общий вывод: какой из трёх вариантов лучше и почему.
# В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому из чисел в диапазоне от 2 до 9.

from timeit import timeit
from cProfile import run


def multiple_v1(max_item):
    n = 8
    min_item = 2
    array = [_ for _ in range(min_item, max_item)]
    multiple_array = [0] * n
    multiple_dict = {}
    for item in array:
        if item % 2 == 0:
            multiple_array[0] += 1
        if item % 3 == 0:
            multiple_array[1] += 1
        if item % 4 == 0:
            multiple_array[2] += 1
        if item % 5 == 0:
            multiple_array[3] += 1
        if item % 6 == 0:
            multiple_array[4] += 1
        if item % 7 == 0:
            multiple_array[5] += 1
        if item % 8 == 0:
            multiple_array[6] += 1
        if item % 9 == 0:
            multiple_array[7] += 1

    for i in range(len(multiple_array)):
        multiple_dict.update({i: multiple_array[i]})

    return multiple_dict


# print(multiple_v1(100))


def multiple_v2(max_item):
    min_item = 2
    min_divider = 2
    max_divider = 10
    multiple_dict = {}
    for i in range(min_divider, max_divider):
        multiples_count = 0
        for j in range(min_item, max_item):
            if j % i == 0:
                multiples_count += 1
        multiple_dict.update({i: multiples_count})
    return multiple_dict


# print(multiple_v2(100))


def multiple_v3(max_item):
    n = 8
    min_item = 2
    min_divider = 2
    max_divider = 10
    array = [_ for _ in range(min_item, max_item)]
    multiple_array = [0] * n
    multiple_dict = {}
    for i in range(len(array)):
        item = array.pop(0)
        for j in range(min_divider, max_divider):
            if item % j == 0:
                multiple_array[j - 2] += 1
    for i in range(len(multiple_array)):
        multiple_dict.update({i + 2: multiple_array[i]})

    return multiple_dict


# print(multiple_v3(100))


print(timeit('multiple_v1(100)', number=100, globals=globals()))  # 0.013693100000000007
print(timeit('multiple_v1(1_000)', number=100, globals=globals()))  # 0.09029220000000002
print(timeit('multiple_v1(10_000)', number=100, globals=globals()))  # 1.0005604000000001
print(timeit('multiple_v1(100_000)', number=100, globals=globals()))  # 12.752031299999999
run('multiple_v1(10_000)')

"""
ncalls  tottime  percall  cumtime  percall filename:lineno(function)
    1    0.000    0.000    0.009    0.009 <string>:1(<module>)
    1    0.009    0.009    0.009    0.009 Task_1.py:16(multiple_v1)
    1    0.000    0.000    0.000    0.000 Task_1.py:19(<listcomp>)
    1    0.000    0.000    0.009    0.009 {built-in method builtins.exec}
    1    0.000    0.000    0.000    0.000 {built-in method builtins.len}
    1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
    8    0.000    0.000    0.000    0.000 {method 'update' of 'dict' objects}
"""
# **********************************************************************************************************************
print(timeit('multiple_v2(100)', number=100, globals=globals()))  # 0.006999600000000328
print(timeit('multiple_v2(1_000)', number=100, globals=globals()))  # 0.10939910000000097
print(timeit('multiple_v2(10_000)', number=100, globals=globals()))  # 01.0033282000000003
print(timeit('multiple_v2(100_000)', number=100, globals=globals()))  # 12.998146299999998
run('multiple_v2(10_000)')

"""
   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.009    0.009 <string>:1(<module>)
        1    0.009    0.009    0.009    0.009 Task_1.py:49(multiple_v2)
        1    0.000    0.000    0.009    0.009 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
        8    0.000    0.000    0.000    0.000 {method 'update' of 'dict' objects}
"""
# **********************************************************************************************************************
# print(timeit('multiple_v3(100)', number=100, globals=globals()))  # 0.01657019999999676
# print(timeit('multiple_v3(1_000)', number=100, globals=globals()))  # 0.19932000000000016
# print(timeit('multiple_v3(10_000)', number=100, globals=globals()))  # 3.5033119
# print(timeit('multiple_v3(100_000)', number=100, globals=globals()))  # 212.9858012
#
# run('multiple_v3(10_000)')

"""
ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.039    0.039 <string>:1(<module>)
        1    0.020    0.020    0.039    0.039 Task_1.py:66(multiple_v3)
        1    0.000    0.000    0.000    0.000 Task_1.py:71(<listcomp>)
        1    0.000    0.000    0.039    0.039 {built-in method builtins.exec}
        2    0.000    0.000    0.000    0.000 {built-in method builtins.len}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
     9998    0.019    0.000    0.019    0.000 {method 'pop' of 'list' objects}
        8    0.000    0.000    0.000    0.000 {method 'update' of 'dict' objects}
"""
# **********************************************************************************************************************

"""
Первый и второй алгоритмы имееют линейную сложность, третий - квадратичную. Время исполнения первого и второго 
практически идентично. Хоть первый алгоритм и имеет более читаемый код, но он менее универсальный и более 
избыточен. Поэтому отдавать предпочтение стоит второму алгоритму. Третий из-за метода 'pop' значительно затратнее, 
поэтому встроенные методы и функции необходимо использовать "с умом".
"""
