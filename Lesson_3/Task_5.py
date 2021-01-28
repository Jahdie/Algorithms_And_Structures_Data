# В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.
# Примечание к задаче: пожалуйста не путайте «минимальный» и «максимальный отрицательный». Это два абсолютно разных
# значения.
from random import randint

SIZE = 10
MIN_ITEM = -100
MAX_ITEM = 100

array = [randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
array = [2, 3, 4, 5, -6, 7, 8]
print(array)
max_negative_num = []
negative_array = []

for list_index_value in enumerate(array):
    if list_index_value[1] < 0:
        negative_array.append(list_index_value)
        max_negative_num = negative_array[0]
    for i in range(len(negative_array)):
        if negative_array[i][1] > max_negative_num[1]:
            max_negative_num = negative_array[i]

if len(negative_array) > 0:
    print(f"Максимальное отрицательное число {max_negative_num[1]} и имеет {max_negative_num[0]} индекс ")
else:
    print("В массиве нет отрицательных чисел!")
