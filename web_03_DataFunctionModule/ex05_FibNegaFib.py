# Задача 5. Задайте число. Составьте список чисел Фибоначчи,
# в том числе для отрицательных индексов.

n = int(input('Введите целое число n = '))


def fib(n):
    if n in [1, 2]:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


def lst_negafib_fib(n):
    lst_fib = []
    for e in range(1, n + 1):
        lst_fib.append(fib(e))
    lst_fib.insert(0, 0)
    for e in range(1, n + 1):
        lst_fib.insert(0, (-1) ** (e + 1) * fib(e))
    return lst_fib


print(lst_negafib_fib(n))
exit()
