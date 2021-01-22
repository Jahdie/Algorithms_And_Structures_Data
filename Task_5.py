# Пользователь вводит две буквы. Определить, на каких местах алфавита они стоят, и сколько между ними находится букв.
# https://drive.google.com/file/d/1zjCdF5ZTABUqmMwkeLk06Lg9t-LYs9AC/view?usp=sharing

letter_1 = ord(input("Введите первую строчную букву латинского алфавита: ").lower())
letter_2 = ord(input("Введите вторую строчную букву латинского алфавита: ").lower())

print(f"Первая буква находится на {letter_1 - 96} месте в алфавите.")
print(f"Вторая буква находится на {letter_2 - 96} месте в алфавите.")

if letter_1 - letter_2 < 0:
    print(f"Между ними {abs((letter_1 + 1) - letter_2)} букв.")
else:
    print(f"Между ними {(letter_1 - 1) - letter_2} букв.")
