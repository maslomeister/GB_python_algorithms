# 3. Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран. 
# Например, если введено число 3486, надо вывести 6843.


n = int(input("Введите число: "))

new_n = ""

while n != 0:

    new_n += str(n % 10)

    n = n // 10

print(f"\nОбратное число: { new_n }")