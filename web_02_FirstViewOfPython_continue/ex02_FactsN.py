# Задача 2. Напишите программу, которая принимает на вход число N
# и выдает набор произведений чисел от 1 до N.

n = int(input('Введите целое число n = '))

list_prod = []
prod = 1
for i in range(1, n + 1):
    prod *= i
    print(prod, end=' ')
# ----------------------

print()
list_fact = []


def fact(n):
    if n == 1:
        return 1
    else:
        return fact(n - 1) * n


for i in range(1, n + 1):
    list_fact.append(fact(i))

print(list_fact)
