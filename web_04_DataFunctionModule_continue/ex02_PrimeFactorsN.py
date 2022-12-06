# Задача 2. Задайте натуральное число N. Напишите программу, которая
# составит список простых множителей числа N.

n = int(input('Введите число n = '))


def prime_factors(n):
    res = []
    d = 2
    while d ** 2 <= n:
        if n % d == 0:
            res.append(d)
            n //= d
        else:
            d += 1
    if n > 1:
        res.append(n)
    return res


print(prime_factors(n))
