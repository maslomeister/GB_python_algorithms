# 1. Проанализировать скорость и сложность одного любого алгоритма из разработанных в рамках домашнего задания первых трех уроков.
# Примечание. Идеальным решением будет:
# a. выбрать хорошую задачу, которую имеет смысл оценивать,
# b. написать 3 варианта кода (один у вас уже есть),
# c. проанализировать 3 варианта и выбрать оптимальный,
# d. результаты анализа вставить в виде комментариев в файл с кодом (не забудьте указать, для каких N вы проводили замеры),
# e. написать общий вывод: какой из трёх вариантов лучше и почему.


import random
import cProfile

# Разбор задачи 4 из урока 3
# Определить, какое число в массиве встречается чаще всего


def main(size):

    array = [random.randint(0, size // 1.5) for _ in range(size)]

    num = array[0]
    max_amount = 1

    for i in range(len(array) - 1):

        amount = 1

        for j in range(i+1, len(array)):

            if array[i] == array[j]:

                amount += 1

            if amount > max_amount:

                max_amount = amount
                num = array[i]

    if max_amount > 1:
        return num, max_amount
    else:
        return -1


# cProfile.run("main(20)")
# 128 function calls in 0.000 seconds
# 1    0.000    0.000    0.000    0.000 task1_1.py:7(main)

# cProfile.run("main(50)")
# 345 function calls in 0.000 seconds
# 1    0.000    0.000    0.000    0.000 task1_1.py:7(main)

# cProfile.run("main(100)")
# 695 function calls in 0.001 seconds
# 1    0.000    0.000    0.000    0.000 task1_1.py:7(main)

# cProfile.run("main(200)")
# 1371 function calls in 0.002 seconds
# 1    0.001    0.001    0.002    0.002 task1_1.py:7(main)

# cProfile.run("main(400)")
# 2833 function calls in 0.007 seconds
# 1    0.006    0.006    0.007    0.007 task1_1.py:7(main)

# cProfile.run("main(600)")
# 3756 function calls in 0.014 seconds
# 1    0.013    0.013    0.014    0.014 task1_1.py:7(main)

# cProfile.run("main(800)")
# 5499 function calls in 0.027 seconds
# 1    0.025    0.025    0.027    0.027 task1_1.py:7(main)


# "task1_1.main(20)"
# 1000 loops, best of 5: 33.4 usec per loop

# "task1_1.main(50)"
# 1000 loops, best of 5: 143 usec per loop

# "task1_1.main(100)"
# 1000 loops, best of 5: 451 usec per loop

# "task1_1.main(200)"
# 1000 loops, best of 5: 1.59 msec per loop

# "task1_1.main(400)"
# 1000 loops, best of 5: 6.55 msec per loop

# "task1_1.main(600)"
# 1000 loops, best of 5: 14.7 msec per loop

# "task1_1.main(800)"
# 1000 loops, best of 5: 26.4 msec per loop
