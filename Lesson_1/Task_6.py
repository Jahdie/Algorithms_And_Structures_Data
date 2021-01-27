# Пользователь вводит номер буквы в алфавите. Определить, какая это буква.
# https://drive.google.com/file/d/1zjCdF5ZTABUqmMwkeLk06Lg9t-LYs9AC/view?usp=sharing

num = int(input("Введите номер от 1 - 26: "))

if 1 <= num <= 26:
    print(f"Буква: {chr(96 + num)}")
else:
    print("Число должно быть от 1 до 26.")
