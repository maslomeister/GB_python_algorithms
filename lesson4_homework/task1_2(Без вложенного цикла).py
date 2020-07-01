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

    max_amount = 0
    num = 0

    for i in array:
        amount = array.count(i)
        if(amount > max_amount):
            max_amount = amount
            num = i

    return num, max_amount


# cProfile.run("main(20)")
# 131 function calls in 0.000 seconds
# 1    0.000    0.000    0.000    0.000 task1_2.py: 11( < listcomp > )

# cProfile.run("main(100)")
# 700 function calls in 0.000 seconds
# 1    0.000    0.000    0.000    0.000 task1_2.py:9(main)

# cProfile.run("main(400)")
# 2764 function calls in 0.003 seconds
# 1    0.000    0.000    0.003    0.003 task1_2.py:9(main)

# cProfile.run("main(600)")
# 3774 function calls in 0.005 seconds
# 1    0.000    0.000    0.005    0.005 task1_2.py:9(main)

# cProfile.run("main(800)")
# 5532 function calls in 0.008 seconds
# 1    0.000    0.000    0.008    0.008 task1_2.py:9(main)

# cProfile.run("main(1000)")
# 6568 function calls in 0.012 seconds
# 1    0.000    0.000    0.012    0.012 task1_2.py:9(main)

# cProfile.run("main(2000)")
# 13033 function calls in 0.046 seconds
# 1    0.000    0.000    0.046    0.046 task1_2.py:9(main)

# cProfile.run("main(10000)")
# 62300 function calls in 1.042 seconds
# 1    0.003    0.003    1.042    1.042 task1_2.py:9(main)

# cProfile.run("main(50000)")
# 348319 function calls in 25.360 seconds
# 1    0.015    0.015   25.360   25.360 task1_2.py:9(main)


# "task1_2.main(20)"
# 1000 loops, best of 5: 20.4 usec per loop

# "task1_2.main(50)"
# 1000 loops, best of 5: 68.7 usec per loop

# "task1_2.main(100)"
# 1000 loops, best of 5: 186 usec per loop

# "task1_2.main(200)"
# 1000 loops, best of 5: 573 usec per loop

# "task1_2.main(400)"
# 1000 loops, best of 5: 1.96 msec per loop

# "task1_2.main(600)"
# 1000 loops, best of 5: 4.11 msec per loop

# "task1_2.main(800)"
# 1000 loops, best of 5: 7.16 msec per loop

# "task1_2.main(1000)"
# 1000 loops, best of 5: 11 msec per loop
