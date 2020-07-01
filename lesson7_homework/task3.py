# 3. Массив размером 2m + 1, где m — натуральное число, заполнен случайным образом. Найдите в массиве медиану. 
# Медианой называется элемент ряда, делящий его на две равные части: в одной находятся элементы, которые не меньше медианы, в другой — не больше медианы.
# Примечание: задачу можно решить без сортировки исходного массива. 
# Но если это слишком сложно, используйте метод сортировки, который не рассматривался на уроках (сортировка слиянием также недопустима).


import random
from collections import Counter, deque
import statistics
import sys

def find_median(arr):
    return kthSmallest(arr, 0, len(arr) - 1, len(arr) // 2 + 1)


def kthSmallest(arr, L, R, k):

    if (k > 0 and k <= R - L + 1):

        pos = partition(arr, L, R)

        if (pos - L == k - 1):
            return arr[pos]

        if (pos - L > k - 1):
            return kthSmallest(arr, L, pos - 1, k)

        return kthSmallest(arr, pos + 1, R, k - pos + L - 1)


def partition(arr, L, R):

    i = L
    for j in range(L, R):
        if (arr[j] <= arr[R]):
            arr[i], arr[j] = arr[j], arr[i]
            i += 1

    arr[i], arr[R] = arr[R], arr[i]
    return i


def sort_according_to_median(arr, med):
    finalarr = deque([med])
    for i in arr:
        if i < med:
            finalarr.appendleft(i)
        if i > med:
            finalarr.append(i)

    return list(finalarr)


size = 2*int(input("\nРазмер массива = 2m + 1, введите m: ")) + 1
arr = [random.randint(0, size // 1.5) for _ in range(size)]
print(f"\nРазмер массива = {size}")
print(f"\nИсходный массив: \n{arr}")
print(f"\nМедиана массива = {find_median(arr)}")
print(
    f"\nМассив преобразованный относительно медианы: \n{sort_according_to_median(arr, find_median(arr))}\n")
