# Написать программу сложения и умножения двух шестнадцатеричных чисел. При этом каждое число представляется как
# коллекция, элементы которой — цифры числа. Например, пользователь ввёл A2 и C4F. Нужно сохранить их как
# [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно. Сумма чисел из примера: [‘C’, ‘F’, ‘1’],
# произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].

from collections import deque

addition_table_hex = [['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']]
hex_num_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
A = (input("Введите щестнадцатиричное чило A: "))
A = deque([item for item in A.upper()])
A.reverse()
B = (input("Введите щестнадцатиричное чило B: "))
B = deque([item for item in B.upper()])
B.reverse()
C = deque()

diff = len(A) - len(B)
if diff < 0:
    for i in range(abs(diff)):
        A.append('0')
else:
    for i in range(abs(diff)):
        B.append('0')


def shift(n, array):
    array_mod = deque(array)
    array_mod.rotate(n)
    array_mod[n] = '1' + array_mod[n]
    return list(array_mod)


for i in range(15):
    list_temp = addition_table_hex[i]
    addition_table_hex.append(shift(15, list_temp))


def get_sum_hex(x, y):
    x = hex_num_list.index(x)
    y = hex_num_list.index(y)

    return addition_table_hex[x][y]


for i in range(len(A)):
    result = (get_sum_hex(A[i], B[i]))
    C.appendleft(result)

if len(C[0]) > 1:
    el = C[0]
    C[0] = C[0][1]
    C.appendleft(el[0])

for j in range(2):
    i = 0
    for el in C:
        if len(el) > 1:
            rank = el[0]
            C[i] = el[-1]
            C[i - 1] = get_sum_hex(C[i - 1], rank)
        i += 1
print()

print(f"{list(A)} + {list(B)} = {list(C)}")
