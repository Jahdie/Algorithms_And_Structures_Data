"""
В программе генерируется случайное целое число от 0 до 100. Пользователь должен его отгадать не более чем за 10 попыток.
После каждой неудачной попытки должно сообщаться, больше или меньше введенное пользователем число, чем то, что загадано.
Если за 10 попыток число не отгадано, вывести правильный ответ.
"""
from random import randint

secret_num = randint(1, 100)
attempts_num = 10

while True:
    if attempts_num != 0:
        user_num = int(input("Угадайте число: "))
        if user_num == secret_num:
            print("Ура! Вы угадали!")
            break
        if user_num < secret_num:
            print("Ваше число меньше загаданного!")
            attempts_num -= 1
        if user_num > secret_num:
            print("Ваше число больше загаданного!")
            attempts_num -= 1
    else:
        print(f"Вы израсходовали все свои попытки! Было загадано число {secret_num}.")
        break
