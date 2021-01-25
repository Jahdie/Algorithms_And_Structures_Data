"""
Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран. Например, если введено
число 3486, надо вывести 6843.
"""
num = int(input("Введите натуральное число: "))
num_temp = num
num_conclusion = num
revers_num = 0
digit_capacity = 0

while True:
    if num_temp > 1:
        num_temp = num_temp / 10
        digit_capacity += 1
    else:
        break
    if digit_capacity != 0:
        num_temp = num % 10
        num = int(num // 10)
        revers_num += num_temp * 10 ** (digit_capacity - 1)
        digit_capacity -= 1
    else:
        break
print(f"Число {num_conclusion} в реверсе: {revers_num}")
