# Задача 3. Задайте словарь из n чисел последовательности
# (1 + (1/n))^n и выведите на экран их сумму.

n = int(input('Введите целое число n = '))
dict_n = {}
sum_values = 0
for i in range(1, n + 1):
    dict_n[i] = round(((1 + 1 / i) ** i), 2)
    sum_values += dict_n[i]
print(dict_n)
print(f'Сумма значений словаря = {sum_values}')
