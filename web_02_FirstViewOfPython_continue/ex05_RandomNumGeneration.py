# Задача 5. Реализуйте алгоритм нахождения(генерации) рандомного
# (случайного) числа.(Не используя библиотеки связанные с рандомом)
import datetime


def gen_random_int(lower, upper):
    curtime = str(datetime.datetime.now())[-6:]     # datetime.datetime.now().microsecond
    rand_num = int((int(curtime) / 10 ** 6 * (upper - lower) + lower))
    return rand_num


lower = int(input('Введите первое число lower = '))
upper = int(input('Введите второе число lower > upper, upper = '))
print(gen_random_int(lower, upper))
