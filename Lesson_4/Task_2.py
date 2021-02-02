# 2). Написать два алгоритма нахождения i-го по счёту простого числа. Функция нахождения простого числа должна принимать
# на вход натуральное и возвращать соответствующее простое число. Проанализировать скорость и сложность алгоритмов.
#
# Первый — с помощью алгоритма «Решето Эратосфена».
# Примечание. Алгоритм «Решето Эратосфена» разбирался на одном из прошлых уроков. Используйте этот код и попробуйте его
# улучшить/оптимизировать под задачу.
#
# Второй — без использования «Решета Эратосфена».
# Примечание. Вспомните классический способ проверки числа на простоту.
# Пример работы программ:
#
# sieve(2)
# 3
# prime(4)
# 7
# sieve(5)
# 11
# prime(1)
# 2

from timeit import timeit
from cProfile import run


def sieve(index_prime_num: int) -> int:
    assert index_prime_num <= 78_498, 'Номер простого числа не может быть больше 78498'
    range_between_prime_numbers = 13
    n = index_prime_num * range_between_prime_numbers
    prime_num = 0
    array = [el for el in range(n)]
    array[1] = 0
    prime_num_counter = 0

    for i in range(2, n):
        if array[i] != 0:
            prime_num = array[i]
            prime_num_counter += 1
            if prime_num_counter == index_prime_num:
                break
            j = i + i
            while j < n:
                array[j] = 0
                j += i
    return prime_num


# print(sieve(11111))


def prime(index_prime_num: int) -> int:
    i = 0
    num = 2
    prime_num = 0
    while i != index_prime_num:
        divider = 2
        while divider * divider <= num and num % divider != 0:
            divider += 1
        if divider * divider > num:
            i += 1
            prime_num = num
        num += 1
    return prime_num


# print(prime(11111))

print(timeit('sieve(5)', number=100, globals=globals()))  # 0.0021183999999999995
print(timeit('sieve(50)', number=100, globals=globals()))  # 0.0274108
print(timeit('sieve(500)', number=100, globals=globals()))  # 0.41186680000000003
print(timeit('sieve(5_000)', number=100, globals=globals()))  # 4.5394349
print(timeit('sieve(50_000)', number=100, globals=globals()))  # 54.5439442
run('sieve(5000)')

"""
ncalls  tottime  percall  cumtime  percall filename:lineno(function)
    1    0.000    0.000    0.040    0.040 <string>:1(<module>)
    1    0.036    0.036    0.039    0.039 Task_2.py:27(sieve)
    1    0.003    0.003    0.003    0.003 Task_2.py:32(<listcomp>)
    1    0.000    0.000    0.040    0.040 {built-in method builtins.exec}
    1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
"""

# **********************************************************************************************************************

print(timeit('prime(5)', number=100, globals=globals()))  # 0.0005183999999999953
print(timeit('prime(50)', number=100, globals=globals()))  # 0.0225329
print(timeit('prime(500)', number=100, globals=globals()))  # 0.41186680000000003
print(timeit('prime(5_000)', number=100, globals=globals()))  # 0.8480367999999999
print(timeit('prime(50_000)', number=100, globals=globals()))  # 28.9086542
run('prime(5000)')

"""
ncalls  tottime  percall  cumtime  percall filename:lineno(function)
    1    0.000    0.000    0.288    0.288 <string>:1(<module>)
    1    0.288    0.288    0.288    0.288 Task_2.py:52(prime)
    1    0.000    0.000    0.288    0.288 {built-in method builtins.exec}
    1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
"""

# **********************************************************************************************************************
"""
Оба алгоритма имеют линейную сложность. Для первого алгоритма необходимо генерировать список,
который накладывает ограничения глубины поиска простого числа. Для второго - таких ограничений нет, он универсальней и 
заметно быстрее. 
"""
