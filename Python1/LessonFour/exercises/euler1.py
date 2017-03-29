#!/usr/bin/python3
# coding: utf-8

__author__ = "Чепелев Антон"

# Числа

# Заполните код приведенных ниже функций. Функция main() уже настроена
# для вызова функций с несколькими различными параметрами,
# и выводит 'OK' в случае, если вызов функции корректен.
# Начальный код каждой функции содержит 'return'
# и является просто заготовкой для вашего кода.


# A. Сумма чисел кратных 3 и 5
# Если выписать все натуральные числа меньше 10, кратные 3 или 5, 
# то получим 3, 5, 6 и 9. Сумма этих чисел - 23.
# Найдите сумму всех чисел меньше 1000 кратных 3 или 5.
# Примечание: попробуйте записать решение в одну строку при помощи генератора списка
# и встроенной функции sum
def multiples():
    return sum([num for num in range(1000) if not num % 5 or not num % 3])


# B. Сумма четных чисел ряда Фибоначчи
# Каждый следующий элемент ряда Фибоначчи получается при сложении 
# двух предыдущих. Начиная с 1 и 2, первые 10 элементов будут:
# 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
# Найдите сумму всех элементов ряда Фибоначчи, каждый их которых
# является четным числом и не превышает четырех миллионов.
# Подсказка: разбейте задачу на части: сначала получите сам ряд Фибоначчи,
# зачем получите ряд четных элементов.
def fibonacci():
    def fib():
        fib1 = 0
        fib2 = 1
        while fib1 + fib2 < 4e6:
            yield fib1 + fib2
            fib1, fib2 = fib2, fib1 + fib2

    result = 0
    for num in fib():
        if not num % 2:
            result += num
    return result


# С. Самый большой палиндром
# Число-палиндром с обеих сторон (справа и слева) читается одинаково. 
# Самое большое число-палиндром, полученное произведением двух двухзначных чисел – 9009 = 91 * 99.
# Найдите самый большой палиндром, полученный произведением двух трёхзначных чисел.
def palindrome():
    return

# Простая функция test() используется в main() для вывода
# сравнения того, что возвращает с функция с тем, что она должна возвращать.
def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('%s Получено: %s | Ожидалось: %s' % (prefix, repr(got), repr(expected)))


# Вызывает функции выше с тестовыми параметрами.
def main():
    print('Сумма чисел кратных 3 и 5')
    test(multiples(), 233168)

    print()
    print('Сумма четных чисел ряда Фибоначчи')
    test(fibonacci(), 4613732)

    print()
    print('Самый большой палиндром')
    test(palindrome(), 906609)

if __name__ == '__main__':
    main()






