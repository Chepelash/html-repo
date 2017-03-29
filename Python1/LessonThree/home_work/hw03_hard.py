import os
from fractions import Fraction as fract

__author__ = "Чепелев Антон"

# Задание-1:
# Написать программу, выполняющую операции (сложение и вычитание) с простыми дробями.
# Дроби вводятся и выводятся в формате:
# n x/y ,где n - целая часть, x - числитель, у - знаменатель.
# Дроби могут быть отрицательные и не иметь целой части, или иметь только целую часть.
# Примеры:
# Ввод: 5/6 + 4/7 (всё выражение вводится целиком в виде строки)
# Вывод: 1 17/42  (результат обязательно упростить и выделить целую часть)
# Ввод: -2/3 - -2
# Вывод: 1 1/3
def fractions(s):
    lst = s.split()
    n1 = n2 = x1 = x2 = 0
    y1 = y2 = 1
    if "+" in lst:
        mid = lst.index("+")
        mark = "+"
    else:
        mid = lst.index("-")
        mark = "-"
    for i in range(mid):
        if len(lst[i]) == 1:
            n1 = lst[i]
        else:
            [x1, y1] = lst[i].split('/')
    for i in range(mid, len(lst)):
        if len(lst[i]) == 1:
            n2 = lst[i]
        else:
            [x2, y2] = lst[i].split('/')
    [x1, x2, y1, y2, n1, n2] = list(map(int, [x1, x2, y1, y2, n1, n2]))
    if n1:
        num1 = n1 * y1 + x1
    else:
        num1 = x1
    if n2:
        num2 = n2 * y2 + x2
    else:
        num2 = x2
    if mark == '+':
        result = fract(num1, y1) + fract(num2, y2)
    else:
        result = fract(num1, y1) - fract(num2, y2)
    n = int(result)
    dem = result - n
    if n and not float(dem):
        print('{}'.format(n))
    elif n:
        print('{} {}'.format(n, str(dem)))
    else:
        print('{}'.format(str(dem)))


# Задание-2:
# Дана ведомость расчета заработной платы (файл "data/workers").
# Рассчитайте зарплату всех работников, зная что они получат полный оклад,
# если отработают норму часов. Если же они отработали меньше нормы,
# то их ЗП уменьшается пропорционально, а за заждый час переработки
# они получают удвоенную ЗП, пропорциональную норме.
# Кол-во часов, которые были отработаны, указаны в файле "data/hours_of"
worker_path = os.path.join("data", "workers")
hours_path = os.path.join("data", "hours_of")
with open(worker_path, encoding="UTF-8") as f:
    workers = f.read()


# Задание-3:
# Дан файл ("data/fruits") со списком фруктов.
# Записать в новые файлы все фрукты, начинающиеся с определенной буквы.
# Т.е. в одном файле будут все фрукты на букву “А”, во втором на “Б” и т.д.
# Файлы назвать соответственно.
# Пример имен файлов: fruits_А, fruits_Б, fruits_В ….
# Важно! Обратите внимание, что нет фруктов, начинающихся с некоторых букв.
# Напишите универсальный код, который будет работать с любым списком фруктов
# и распределять по файлам в зависимости от первых букв, имеющихся в списке фруктов.
# Подсказка:
# Чтобы получить список больших букв русского алфавита:
# print(list(map(chr, range(ord('А'), ord('Я')+1))))
