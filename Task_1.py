"""
Написать программу, которая будет складывать, вычитать, умножать или делить два числа. Числа и знак операции вводятся
пользователем. После выполнения вычисления программа не завершается, а запрашивает новые данные для вычислений.
Завершение программы должно выполняться при вводе символа '0' в качестве знака операции. Если пользователь вводит
неверный знак (не '0', '+', '-', '*', '/'), программа должна сообщать об ошибке и снова запрашивать знак операции.
Также она должна сообщать пользователю о невозможности деления на ноль, если он ввел его в качестве делителя.
"""
# https://drive.google.com/file/d/1X1OdbquAMqPDjb83byzE2HPYRrLHM3fC/view?usp=sharing
operation_symbol = ''

while True:
    operation_symbol = str(input("Введите знак опреации +, -, *, / или 0 если хотите завершить программу: "))
    if operation_symbol == '0':
        break
    else:
        while True:
            if operation_symbol != '+' \
                    and operation_symbol != '-' \
                    and operation_symbol != '*' \
                    and operation_symbol != '/' \
                    and operation_symbol != '0':
                print("Введен не верный знак операции.")
                operation_symbol = str(
                    input("Введите знак опреации +, -, *, / или 0 если хотите завершить программу: "))
            else:
                break
        if operation_symbol == '0':
            break
        if operation_symbol == '+':
            num_1 = float(input("Введите первое число: "))
            num_2 = float(input("Введите второе число: "))
            print(f"{num_1} + {num_2} = {num_1 + num_2}")
        elif operation_symbol == '-':
            num_1 = float(input("Введите первое число: "))
            num_2 = float(input("Введите второе число: "))
            print(f"{num_1} - {num_2} = {num_1 - num_2}")
        elif operation_symbol == '*':
            num_1 = float(input("Введите первое число: "))
            num_2 = float(input("Введите второе число: "))
            print(f"{num_1} * {num_2} = {num_1 * num_2}")
        else:
            num_1 = float(input("Введите первое число: "))
            num_2 = float(input("Введите второе число: "))
            while True:
                if num_2 == 0:
                    print("Деление на ноль невозможно!")
                    num_2 = float(input("Введите второе число: "))
                else:
                    break
            print(f"{num_1} / {num_2} = {num_1 / num_2}")
