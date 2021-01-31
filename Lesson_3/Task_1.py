# В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому из чисел в диапазоне от 2 до 9.

MIN_ITEM = 2
MAX_ITEM = 100
array = [_ for _ in range(MIN_ITEM, MAX_ITEM)]
multiple_2, multiple_3, multiple_4, multiple_5, multiple_6, multiple_7, multiple_8, multiple_9 = 0, 0, 0, 0, 0, 0, 0, 0

for item in array:
    if item % 2 == 0:
        multiple_2 += 1
    if item % 3 == 0:
        multiple_3 += 1
    if item % 4 == 0:
        multiple_4 += 1
    if item % 5 == 0:
        multiple_5 += 1
    if item % 6 == 0:
        multiple_6 += 1
    if item % 7 == 0:
        multiple_7 += 1
    if item % 8 == 0:
        multiple_8 += 1
    if item % 9 == 0:
        multiple_9 += 1
print(
    f"В диапозоне от 2 до 99 кратно 2: {multiple_2} шт.\nВ диапозоне от 2 до 99 кратно 3: {multiple_3} шт.\n"
    f"В диапозоне от 2 до 99 кратно 4: {multiple_4} шт.\nВ диапозоне от 2 до 99 кратно 5: {multiple_5} шт.\n"
    f"В диапозоне от 2 до 99 кратно 6: {multiple_6} шт.\nВ диапозоне от 2 до 99 кратно 6: {multiple_6} шт.\n"
    f"В диапозоне от 2 до 99 кратно 7: {multiple_7} шт.\nВ диапозоне от 2 до 99 кратно 8: {multiple_8} шт.\n"
    f"В диапозоне от 2 до 99 кратно 9: {multiple_9} шт.\n")
