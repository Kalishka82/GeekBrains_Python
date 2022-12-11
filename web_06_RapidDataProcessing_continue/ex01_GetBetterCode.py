# Задача: предложить улучшения кода(3-5задач) для уже решённых задач:
# С помощью использования **лямбд, filter, map, zip, enumerate, list comprehension

# 1. Напишите программу, которая принимает на вход координаты
# двух точек и находит расстояние между ними в 2D пространстве.
# point_A = [7, -5]
# point_B = [1, -1]
point_A = input('Введите координаты точки А x,y = ')
point_B = input('Введите координаты точки В x,y = ')
A = list(map(int, point_A.split(',')))
B = list(map(int, point_B.split(',')))

distance = ((B[0] - A[0]) ** 2 + (B[1] - A[1]) ** 2) ** 0.5
print(f'distance = {round(distance, 2)}')
# -----------------------------------------

# 2. Задайте словарь из n чисел последовательности
# (1 + (1/n))^n и выведите на экран их сумму.
#
n = int(input('Введите целое число n = '))

list_n = [i for i in range(1, n + 1)]
list_eval = list(map(lambda n: round((1 + (1/n)) ** n, 2), list_n))
dict_n = dict(zip(list_n, list_eval))
print(dict_n)
sum_values = sum(dict_n.values())
print(f'Сумма значений словаря = {sum_values}')
# -----------------------------------------------

# 3. Напишите программу, которая принимает на вход число N
# и выдает набор произведений чисел от 1 до N.
#
n = int(input('Введите целое число n = '))


def fact(n):
    if n == 1:
        return 1
    else:
        return fact(n - 1) * n


list_fact = [fact(n) for n in range(1, n + 1)]
print(list_fact)
# ----------------

# 4. Задайте список из нескольких чисел. Напишите программу,
# # которая найдёт сумму элементов списка, стоящих на нечётной позиции.
#
nums = [22, 39, 10, 8, 56, 12, 2, 291]
nums_odd_index = list(filter(lambda i: nums.index(i) % 2, nums))
sum_odd = sum(nums_odd_index)
print(f'Сумма элементов списка, стоящих на нечетных позициях = {sum_odd}')
# --------------------------------------------------------------------------
