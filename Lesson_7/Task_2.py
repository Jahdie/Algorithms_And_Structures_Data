from random import uniform

array = [uniform(0, 50) for i in range(10)]


def merging_arrays(array_1, array_2):
    merged_array = []
    i = j = 0
    while i < len(array_1) and j < len(array_2):
        if array_1[i] < array_2[j]:
            merged_array.append(array_1[i])
            i += 1
        else:
            merged_array.append(array_2[j])
            j += 1
    if i < len(array_1):
        merged_array += array_1[i:]
    if j < len(array_2):
        merged_array += array_2[j:]
    return merged_array


def merge_sort(lst):
    if len(lst) == 1:
        return lst
    middle = len(lst) // 2
    left = merge_sort(lst[:middle])
    right = merge_sort(lst[middle:])
    return merging_arrays(left, right)


print(array)
print(merge_sort(array))


