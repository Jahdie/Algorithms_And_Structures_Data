"""
Посчитать, сколько раз встречается определенная цифра в введенной последовательности чисел. Количество вводимых чисел
и цифра, которую необходимо посчитать, задаются вводом с клавиатуры.
"""

amount_num = int(input("Введите количество чисел: "))
required_digit = int(input("Введите искомую цифру: "))
amount_digit = 0
while True:
    if amount_num != 0:
        num = int(input("Введите число: "))
        amount_num -= 1
        while True:
            if num != 0:
                result = num % 10
                if result == required_digit:
                    amount_digit += 1
                num = int(num / 10)
            else:
                break
    else:
        break
print(f"Количество цифр {required_digit}: {amount_digit} шт.")
