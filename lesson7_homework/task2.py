# 2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив, заданный случайными числами на промежутке [0; 50). 
# Выведите на экран исходный и отсортированный массивы.


import random

def merge_sort(arr):

    if len(arr) < 2:
        return arr

    M = len(arr) // 2

    return merge(merge_sort(arr[:M]), merge_sort(arr[M:]))


def merge(L, R):

    result = []
    i = j = 0
    while i < len(L) and j < len(R):
        if L[i] < R[j]:
            result.append(L[i])
            i += 1
        else:
            result.append(R[j])
            j += 1

    result += L[i:]
    result += R[j:]

    return result


size = 50
arr = [random.uniform(0, 50) for _ in range(size)]

print(f"\nИсходный массив: \n{arr}")
print(f"\nОтсорированный массив: \n{merge_sort(arr)}\n")
