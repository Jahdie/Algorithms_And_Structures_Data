# Написать программу, которая генерирует в указанных пользователем границах случайное целое число, случайное
# вещественное число, случайный символ.
# Для каждого из трех случаев пользователь задает свои границы диапазона. Например, если надо получить случайный символ
# от 'a' до 'f', то вводятся эти символы. Программа должна вывести на экран любой символ алфавита от 'a' до 'f'
# включительно.
# https://drive.google.com/file/d/1zjCdF5ZTABUqmMwkeLk06Lg9t-LYs9AC/view?usp=sharing

from random import randint, uniform

int_start = int(input("Введите начало диапазона целых чисел: "))
int_end = int(input("Введите конец диапазона целых чисел: "))
float_start = float(input("Введите начало диапазона вещественных чисел: "))
float_end = float(input("Введите конец диапазона вещественных чисел: "))
char_start = ord(input("Введите начало диапазона символов: "))
char_end = ord(input("Введите начало диапазона символов: "))

if int_start > int_end:
    print("Неверный диапазон!")
else:
    print(f"Случайное целое число: {randint(int_start, int_end)}")
if float_start > float_end:
    print("Неверный диапазон!")
else:
    print(f"Случайное вещественное число: {uniform(int_start, int_end)}")
if char_start > char_end:
    print("Неверный диапазон!")
else:
    print(f"Случайный символ: {chr(randint(char_start, char_end))}")
