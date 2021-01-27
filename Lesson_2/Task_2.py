"""
Посчитать четные и нечетные цифры введенного натурального числа. Например, если введено число 34560, в нем 3 четные
цифры (4, 6 и 0) и 2 нечетные (3 и 5).
"""

num_enter = int(input("Введите натуральное число: "))
even_digit = 0
odd_digit = 0
num = num_enter
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
print(f"В числе {num_enter}: {even_digit} четных цифр, {odd_digit} нечетных цифр.")
