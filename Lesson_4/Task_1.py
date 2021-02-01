# 1). Проанализировать скорость и сложность одного любого алгоритма из разработанных в рамках домашнего задания первых
# трех уроков.
# Примечание. Идеальным решением будет:
# ● выбрать хорошую задачу, которую имеет смысл оценивать (укажите в комментарии какую задачу вы взяли),
# ● написать 3 варианта кода (один у вас уже есть),
# ● проанализировать 3 варианта и выбрать оптимальный,
# ● результаты анализа вставить в виде комментариев в файл с кодом (не забудьте указать, для каких N вы проводили
# замеры),
# ● написать общий вывод: какой из трёх вариантов лучше и почему.
"""
Посчитать четные и нечетные цифры введенного натурального числа. Например, если введено число 34560, в нем 3 четные
цифры (4, 6 и 0) и 2 нечетные (3 и 5).
"""
from timeit import timeit
from cProfile import run


def even_odd_v1(num):
    even_digit = 0
    odd_digit = 0

    while True:
        if num > 1:
            result = num % 10
            if int(result) % 2 == 0:
                even_digit += 1
            else:
                odd_digit += 1
            num = num / 10
        else:
            break
    return even_digit, odd_digit


# print(even_odd_v1(34560))


def even_odd_v2(num):
    even_digit_array = []
    odd_digit_array = []

    while True:
        if num > 1:
            result = num % 10
            if int(result) % 2 == 0:
                even_digit_array.append(int(result))
            else:
                odd_digit_array.append(int(result))
            num = num / 10
        else:
            break
    even_digit = len(even_digit_array)
    odd_digit = len(odd_digit_array)
    return even_digit, odd_digit


# print(even_odd_v2(34560))


def even_odd_v3(num):
    odd_even_dict = {"odd": [], "even": []}
    even_digit = 0
    odd_digit = 0
    even_digit_str = ''
    odd_digit_str = ''
    while True:
        if num > 1:
            result = num % 10
            if int(result) % 2 == 0:
                even_digit_str = even_digit_str + str(int(result))
                # odd_even_dict["odd"].append(int(result))
            else:
                odd_digit_str = odd_digit_str + str(int(result))
            num = num / 10
        else:
            break
    for i in range(len(even_digit_str)):
        odd_even_dict['even'].append(int(even_digit_str[i:i+1]))
    for i in range(len(odd_digit_str)):
        odd_even_dict['odd'].append(int(odd_digit_str[i:i+1]))

    for key, value in odd_even_dict.items():
        if key == "odd":
            for digit in value:
                if digit:
                    odd_digit += 1
        if key == "even":
            for digit in value:
                if digit:
                    even_digit += 1
    return even_digit, odd_digit


# print(even_odd_v3(344556))

print(timeit('even_odd_v1(334_488)', number=10_000, globals=globals()))  # 0.048734
print(timeit('even_odd_v1(222_877_635_844)', number=10_000, globals=globals()))  # .07143970000000001
print(timeit('even_odd_v1(454_587_733_352_115_987_667_234)', number=10_000, globals=globals()))  # 0.15480280000000002
run('even_odd_v1(454_587_733_352_115_987_667_234)')

# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#     1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#     1    0.000    0.000    0.000    0.000 Task_1.py:18(even_odd_v1)
#     1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#     1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

# **************************************************************************************************************

print(timeit('even_odd_v2(334_488)', number=100, globals=globals()))  # 0.0005422000000000482
print(timeit('even_odd_v2(222_877_635_844)', number=100, globals=globals()))  # 0.0009997999999999951
print(timeit('even_odd_v2(454_587_733_352_115_987_667_234)', number=100, globals=globals()))  # 0.002196100000000034
run('even_odd_v2(454_587_733_352_115_987_667_234)')

# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#     1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#     1    0.000    0.000    0.000    0.000 Task_1.py:38(even_odd_v2)
#     1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#     2    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#     24    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#      1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

# **************************************************************************************************************

print(timeit('even_odd_v3(334_488)', number=100, globals=globals()))  # 0.0014608999999999872
print(timeit('even_odd_v3(222_877_635_844)', number=100, globals=globals()))  # 0.004096700000000009
print(timeit('even_odd_v3(454_587_733_352_115_987_667_234)', number=100, globals=globals()))  # 0.008181600000000011
run('even_odd_v3(454_587_733_352_115_987_667_234)')

# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#     1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#     1    0.000    0.000    0.000    0.000 Task_1.py:60(even_odd_v3)
#     1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#     2    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#     24   0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#     1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#     1    0.000    0.000    0.000    0.000 {method 'items' of 'dict' objects}

# **************************************************************************************************************