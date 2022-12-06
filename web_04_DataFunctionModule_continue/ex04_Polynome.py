# Задача 4. Задана натуральная степень k. Сформировать случайным образом
# список коэффициентов (значения от 0 до 100)* многочлена
# и записать в файл многочлен степени k.

import random

k = int(input('Введите число k = '))
coef = [random.randint(-100, 100) for i in range(0, k + 1)]
print(coef)


def Polynom(k, coef):
    pol = ''
    for i in range(0, k + 1):
        if coef[i] == 0:
            pol = ''
        elif k - i > 1 and coef[i] != 0:
            pol += f'{coef[i]}*x^{k - i} + '
        elif k - i == 1 and coef[i] != 0:
            pol += f'{coef[i]}*x + '
        else:
            pol += f'{coef[i]} = 0'
    return pol


with open('pol.txt', 'w') as data:
    data.write(Polynom(k, coef).replace('+ -', '- '))
