# Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого).
# https://drive.google.com/file/d/1zeBMT4P-myqya7KnZUv0QJwA8cv9y8SG/view?usp=sharing

num_1 = int(input('Введите первое число: '))
num_2 = int(input('Введите второе число: '))
num_3 = int(input('Введите третье число: '))

if num_1 == num_2 or num_1 == num_3 or num_2 == num_3:
    print("Числа должны быть разными!")
else:
    if num_2 < num_1 < num_3 or num_2 > num_1 > num_3:
        print(f"Среднее число: {num_1}.")
    elif num_1 < num_2 < num_3 or num_1 > num_2 > num_3:
        print(f"Среднее число: {num_2}.")
    else:
        print(f"Среднее число: {num_3}.")
