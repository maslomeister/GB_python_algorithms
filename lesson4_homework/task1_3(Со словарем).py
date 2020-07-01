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

    diction = {}

    for item in array:
        if item in diction.keys():
            diction[item] += 1
        else:
            diction[item] = 1

    val = list(diction.values())
    key = list(diction.keys())

    return key[val.index(max(val))], diction[key[val.index(max(val))]]


# cProfile.run("main(20)")
# 139 function calls in 0.000 seconds
# 1    0.000    0.000    0.000    0.000 task1_3.py:7(main)

# cProfile.run("main(50)")
# 354 function calls in 0.000 seconds
# 1    0.000    0.000    0.000    0.000 task1_3.py:7(main)

# cProfile.run("main(100)")
# 705 function calls in 0.000 seconds
# 1    0.000    0.000    0.000    0.000 task1_3.py:7(main)

# cProfile.run("main(200)")
# 1377 function calls in 0.000 seconds
# 1    0.000    0.000    0.000    0.000 task1_3.py:7(main)

# cProfile.run("main(400)")
# 2762 function calls in 0.001 seconds
# 1    0.000    0.000    0.001    0.001 task1_3.py:7(main)

# cProfile.run("main(600)")
# 3777 function calls in 0.001 seconds
# 1    0.000    0.000    0.001    0.001 task1_3.py:7(main)

# cProfile.run("main(800)")
# 5555 function calls in 0.002 seconds
# 1    0.000    0.000    0.002    0.002 task1_3.py:7(main)

# cProfile.run("main(1000)")
# 6537 function calls in 0.002 seconds
# 1    0.000    0.000    0.002    0.002 task1_3.py:7(main)

# cProfile.run("main(2000)")
# 13018 function calls in 0.004 seconds
# 1    0.000    0.000    0.004    0.004 task1_3.py:7(main)

# cProfile.run("main(10000)")
# 62317 function calls in 0.018 seconds
# 1    0.002    0.002    0.018    0.018 task1_3.py:7(main)

# cProfile.run("main(50000)")
# 348158 function calls in 0.098 seconds
# 1    0.012    0.012    0.097    0.097 task1_3.py:7(main)

# cProfile.run("main(100000)")
# 695455 function calls in 0.200 seconds
# 1    0.025    0.025    0.199    0.199 task1_3.py:7(main)

# cProfile.run("main(1000000)")
# 6572147 function calls in 1.979 seconds
# 1    0.304    0.304    1.961    1.961 task1_3.py:7(main)

# "task1_3.main(20)"
# 1000 loops, best of 5: 19.6 usec per loop

# "task1_3.main(50)"
# 1000 loops, best of 5: 46.1 usec per loop

# "task1_3.main(100)"
# 1000 loops, best of 5: 98.2 usec per loop

# "task1_3.main(200)"
# 1000 loops, best of 5: 194 usec per loop

# "task1_3.main(400)"
# 1000 loops, best of 5: 411 usec per loop

# "task1_3.main(600)"
# 1000 loops, best of 5: 605 usec per loop

# "task1_3.main(800)"
# 1000 loops, best of 5: 854 usec per loop

# "task1_3.main(1000)"
# 1000 loops, best of 5: 1.04 msec per loop

# "task1_3.main(2000)"
# 1000 loops, best of 5: 2.1 msec per loop

# "task1_3.main(10000)"
# 1000 loops, best of 5: 9.55 msec per loop
