"""
 Найти сумму n элементов следующего ряда чисел: 1, -0.5, 0.25, -0.125,… Количество элементов (n) вводится с клавиатуры.
"""

def sum_series(n, first_num) -> float:
    _sum = 0
    if n != 0:
        if first_num == 1:
            _sum = 1
            _sum = _sum + sum_series(n - 1, first_num / 2 * -1)
            return _sum
        else:
            _sum = _sum + sum_series(n - 1, first_num / 2 * -1)
            return _sum + first_num
    else:
        return 0


_n = int(input('Введите количество элементов: '))

print(f'Сумма ряда c {_n} элементамми: {sum_series(_n, 1)}')
