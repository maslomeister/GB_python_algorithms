# 4. Найти сумму n элементов следующего ряда чисел: 1, -0.5, 0.25, -0.125,… 
# Количество элементов (n) вводится с клавиатуры.


n = int(input("Введите количество элементов: "))

seq = 1

i = 2

su = 0

print(f"Последовательность: { seq }", end="")

while i <= n:
    seq = seq / -2

    su += seq

    print(f", { seq }", end="")

    i += 1

print(f"\nСумма её элементов = { su }")
