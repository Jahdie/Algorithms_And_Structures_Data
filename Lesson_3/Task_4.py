# Определить, какое число в массиве встречается чаще всего.
from random import randint

SIZE = 20
MIN_ITEM = 0
MAX_ITEM = 15

array = [randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
num_amount = 0
dict_key = 0
print(array)

numbers_amount = {num: [i for i in range(len(array)) if num == array[i]] for num in array}
for key, value in numbers_amount.items():
    if len(value) > num_amount:
        num_amount = len(value)
        dict_key = key
print(f"Число {dict_key} втречается в массиве чаще всего: {num_amount} раза.")


