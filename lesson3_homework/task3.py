# 3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.


import random

numarr = [random.randint(-100, 100) for _ in range(25)]
minnumpos = 0
maxnumpos = 0

print(f"\nИзначальный массив: { numarr }")

for i, j in enumerate(numarr):
    if j < numarr[minnumpos]:
        minnumpos = i
    if j > numarr[maxnumpos]:
        maxnumpos = i

numarr[minnumpos], numarr[maxnumpos] = numarr[maxnumpos], numarr[minnumpos]

print(f"\nИзмененный массив: { numarr }")

print(
    f"\nМестами поменялись числа { numarr[maxnumpos] } и { numarr[minnumpos] }\n")
