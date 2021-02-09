# Пользователь вводит две буквы. Определить, на каких местах алфавита они стоят, и сколько между ними находится букв.
# Windows 10 x64, Python 3.8

from collections import namedtuple, Counter
from sys import getsizeof

ALPHABET_LIST = \
    ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'v', 'x', 'y', 'z']
ALPHABET_TUPLE = \
    ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'v', 'x', 'y', 'z')


def get_type_sizeof(obj):
    print(f'{type(obj)} {getsizeof(obj)} {obj}')
    if hasattr(obj, '__iter__'):
        if not isinstance(obj, str):
            counter_size = 0
            type_items = []
            type_count = Counter()
            for itm in obj:
                type_items.append(str(type(itm)))
                counter_size += getsizeof(itm)
            for el in type_items:
                type_count[el] += 1
            return print(type_count, counter_size)


# ********************************************************ВАРИАНТ_1*****************************************************

letter_1 = ord(input("Введите первую строчную букву латинского алфавита: ").lower())
letter_2 = ord(input("Введите вторую строчную букву латинского алфавита: ").lower())

print(f"Первая буква находится на {letter_1 - 96} месте в алфавите.")
print(f"Вторая буква находится на {letter_2 - 96} месте в алфавите.")

if letter_1 - letter_2 < 0:
    print(f"Между ними {abs((letter_1 + 1) - letter_2)} букв.")
else:
    print(f"Между ними {(letter_1 - 1) - letter_2} букв.")

# ********************************************************ВАРИАНТ_2*****************************************************

letter_first = input("Введите букву английского алфавита: ").lower()
letter_second = input("Введите букву английского алфавита: ").lower()
letter_first_pos = ALPHABET_LIST.index(letter_first) + 1
letter_second_pos = ALPHABET_LIST.index(letter_second) + 1
letters_between = abs(letter_first_pos - letter_second_pos) - 1
print(f"Между буквой {letter_first} и буквой {letter_second} находится {letters_between} букв.")

# ********************************************************ВАРИАНТ_3***************************************************
alphabet_dict = {}
for item in enumerate(ALPHABET_TUPLE, start=1):
    alphabet_dict.update({item[1]: item[0]})
all_letters = []
Letters = namedtuple('Letters', 'letter_1, letter_2, letter_pos_1, letter_pos_2, letters_between')
num = int(input('Введите количество пар букв: '))
letters = []
letters_pos = []
for i in range(num):
    letters = []
    letters_pos = []
    for j in range(1, 3):
        letter = (input(f'Введите {j} букву: ')).lower()
        letters.append(letter)
        letter_pos = alphabet_dict[letter]
        letters_pos.append(letter_pos)
    all_letters.append(Letters(*letters, *letters_pos, abs(letters_pos[0] - letters_pos[1]) - 1))

for i in range(len(all_letters)):
    print(f'Между буквой {all_letters[i].letter_1} и буквой {all_letters[i].letter_2} '
          f'находится {all_letters[i].letters_between} букв.')

# **********************************************************************************************************************

variables_v1 = (letter_1, letter_2)
variables_v2 = (ALPHABET_LIST, letter_first, letter_second, letter_first_pos, letter_second_pos, letters_between)
variables_v3 = (ALPHABET_TUPLE, letters, letters_pos, all_letters)

for var in variables_v1:
    get_type_sizeof(var)
    print("*********************")
for var in variables_v2:
    get_type_sizeof(var)
    print("*********************")
for var in variables_v3:
    get_type_sizeof(var)
    print("*********************")

# **********************************************************************************************************************

"""
В первом варианте используется 2 переменные типа INT общим объемом 56 байт.
(<class 'int'> 28 X 2)
Итого: 56 байт.
------------------------------------------------------------------------------------------------------------------------
Во втором варианте используется 3 переменные типа INT общим объемом в 100 байт, и две переменные типа STR общим 
объемом в 84 байта. А так же переменная типа LIST размеров в 248 байт, содержащая ссылки на объекты типа STR в размере 
23 шт. общим объемом 1150 байт.
(<class 'int'> 28 X 3, <class 'str'> 50 X 2, <class 'list'> 248 (Counter({"<class 'str'>": 23}) 1150)
Итого: 1_492 байт.
------------------------------------------------------------------------------------------------------------------------
Скрипт выполнялся для одной пары букв.
В третьем варианте используется 1 переменная типа TUPLE объемом в 224 байта, содержащая ссылки на объекты типа STR в 
размере 23 шт. общим объемом 1150 байт, 3 переменные типа LIST общим объемом в 264 байта. В первой содержиться ссылка
на 2 объекта типа STR общим размером 100 байт. Во второй содержиться ссылка на 2 объекта типа INT общим размером 
56 байт. В третьей содержиться ссылка на экземпляр класса NAMEDTUPLE объемом в 80 байт.
(<class 'tuple'> 224 (Counter({"<class 'str'>": 23}) 1150, <class 'list'> 88 (Counter({"<class 'str'>": 2}) 100), 
<class 'list'> 88 (Counter({"<class 'int'>": 2}) 56), <class 'list'> 88 (Counter({"<class '__main__.Letters'>": 1}) 80)
Итого: 1_874 байт.
------------------------------------------------------------------------------------------------------------------------
Вывод.
Даже на малых размерах множеств LIST и TUPLE заметна разница в объеме занимаемой ими памяти. Поэтому для констант 
необходимо выбирать именно кортежи. Также, выбор NAMEDTUPLE кроме удобства, значительно экономит опертивную 
память.  
 """