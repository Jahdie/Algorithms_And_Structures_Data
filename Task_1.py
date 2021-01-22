# Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.
# https://drive.google.com/file/d/1_hWWiDQgnp7z9pZPnKP7orOAnB9AbjJ3/view?usp=sharing

num = int(input("Введите трехзначное число: "))

if 100 <= num < 1000:
    digit_1 = num // 100
    digit_2 = num // 10 % 10
    digit_3 = num % 10
    print(
        f"Сумма цифр трехзначного числа: {digit_1 + digit_2 + digit_3}, "
        f"произведение цифр трехзначного числа: "f"{digit_1 * digit_2 * digit_3}")
else:
    print("Число должно быть трехзначным!")
