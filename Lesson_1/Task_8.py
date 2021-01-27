# Определить, является ли год, который ввел пользователем, високосным или не високосным.
# https://drive.google.com/file/d/1zjCdF5ZTABUqmMwkeLk06Lg9t-LYs9AC/view?usp=sharing

year = int(input("Введите год: "))

if year % 400 == 0 or year % 100 != 0 and year % 4 == 0:
    print(f"Год {year} - високосный.")
else:
    print(f"Год {year} - не високосный.")
