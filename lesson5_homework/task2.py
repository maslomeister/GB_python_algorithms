# 2. Написать программу сложения и умножения двух шестнадцатеричных чисел. При этом каждое число представляется как массив, элементы которого — цифры числа.
# Например, пользователь ввёл A2 и C4F. Нужно сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно. Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
# Примечание: Если воспользоваться функциями hex() и/или int() для преобразования систем счисления, задача решается в несколько строк. Для прокачки алгоритмического мышления такой вариант не подходит. Поэтому использование встроенных функций для перевода из одной системы счисления в другую в данной задаче под запретом.
# Вспомните начальную школу и попробуйте написать сложение и умножение в столбик.


from collections import deque
import copy

HEX_TABLE = {"0": 0, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9,
             "A": 10, "B": 11, "C": 12, "D": 13, "E": 14, "F": 15,
             0: "0", 1: "1", 2: "2", 3: "3", 4: "4", 5: "5", 6: "6", 7: "7", 8: "8", 9: "9",
             10: "A", 11: "B", 12: "C", 13: "D", 14: "E", 15: "F"}


def my_sum(x, y):

    result = deque()
    transf = 0

    if len(x) != len(y):

        if len(x) > len(y):
            x = deque(x)
            y = deque(y)
            n = len(x) - len(y)

            y.extendleft(["0"] * n)

        else:
            y = deque(y)
            x = deque(x)
            n = len(y) - len(x)

            for _ in range(n):
                x.appendleft("0")

    for _ in range(len(x)):

        tempresult = HEX_TABLE[x.pop()] + HEX_TABLE[y.pop()] + transf

        transf = 0

        if tempresult < 16:
            result.appendleft(HEX_TABLE[tempresult])
        else:
            result.appendleft(HEX_TABLE[tempresult - 16])
            transf = 1

    if transf:
        result.appendleft("1")

    return result


def my_mul(x, y):

    results = []
    c_result = deque()
    transf = 0

    x = x[::-1]
    y = y[::-1]

    if len(x) < len(y):
        x, y = y, x

    for i in range(len(y)):

        for j in range(len(x)):

            mytempX = HEX_TABLE[x[j]]
            mytempY = HEX_TABLE[y[i]]

            tempresult = mytempX * mytempY + transf

            if tempresult < 16:
                c_result.appendleft(HEX_TABLE[tempresult])
                transf = 0
            else:
                transf = tempresult // 16
                tempresult = tempresult - 16 * transf
                c_result.appendleft(HEX_TABLE[tempresult])

        if transf:
            c_result.appendleft(HEX_TABLE[transf])

        results.append(c_result)

        tempstr = (i+1) * "0"
        c_result = deque()
        transf = 0

        for i in range(len(tempstr)):
            c_result.append("0")

    for i in range(0, len(results) - 1):

        results[i+1] = my_sum(list(results[i]), list(results[i+1]))

    return(results[len(results)-1])


x = list(input("\nВведите первое число: ").upper())
y = list(input("\nВведите второе число: ").upper())


print(f"\nСумма чисел = { list(my_sum(x, y)) }")
print(f"\nПроизведение чисел = { list(my_mul(x, y)) }\n")
