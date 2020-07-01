# 1. Определение количества различных подстрок с использованием хеш-функции. Пусть на вход функции дана строка. Требуется вернуть количество различных подстрок в этой строке.
# Примечания:
# * в сумму не включаем пустую строку и строку целиком;
# * задача считается решённой, если в коде использована функция вычисления хеша (hash(), sha1() или любая другая из модуля hashlib)

import hashlib


def subs_amount(s: str) -> [int, list]:
    assert len(s) > 0, 'Строка не может быть пустой'

    subs = set()
    h_subs = set()

    for i in range(len(s)):
        length = len(s)

        if i == 0:
            length = len(s) - 1

        for j in range(length, i, -1):
            h_subs.add(hashlib.sha1(s[i:j].encode('utf-8')).hexdigest())
            subs.add(s[i:j])

    return len(subs), sorted(subs, key=len)


s = input("Введите строку: ")

result = subs_amount(s)


print(f"\nКоличество подстрок: {result[0]}\nПодстроки: ", end="")
print(*result[1])
