# 4. Определить, какое число в массиве встречается чаще всего.


import random

numarr = [random.randint(2, 10) for _ in range(15)]

num = numarr[0]
amount = 1
max_amount = 0

print(f"\nМассив: { numarr }")

for i in range(len(numarr) - 1):
    for j in range(i+1, len(numarr)):
        if numarr[i] == numarr[j]:
            amount += 1
        if amount > max_amount:
            max_amount = amount
            num = numarr[i]


if max_amount > 1:
    print(f"\n{ num } встретилось { max_amount } раз(а)\n")
else:
    print(f"\nЧисла не повторялись\n")
