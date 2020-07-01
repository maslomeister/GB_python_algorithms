# 5. В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.
# Примечание к задаче: пожалуйста не путайте «минимальный» и «максимальный отрицательный». Это два абсолютно разных значения.


import random

numarr = [random.randint(-100, 10) for _ in range(20)]
maxnumpos = 0

print(f"\nМассив: { numarr }")


for i, j in enumerate(numarr):
    if j < numarr[maxnumpos]:
        maxnumpos = i

print(
    f"\nМаксимальное отрицательно число массива: { numarr[maxnumpos] } на позиции { maxnumpos }\n")
