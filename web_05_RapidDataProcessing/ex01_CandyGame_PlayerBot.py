# Задача 1. Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход.
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""

import random
from random import randint


player = input('Введите имя игрока: ')
bot = 'BOT'
candy = int(input('Введите кол-во конфет на столе candy = '))
m_max = int(input('Введите максимальное кол-во конфет, возможное за один ход m_max = '))
# print(k % (m_max + 1))
fortune = random.randint(0, 2)

if fortune:
    print(f'Первым ходит {player}')
else:
    print(f'Первым ходит {bot}')


def take_candy_amount(name):
    if name == player:
        move = int(input(f'{name}, введите кол-во конфет от 1 до {m_max}: '))
        while move < 1 or move > m_max:
            move = int(input(f'{name}, введите кол-во конфет от 1 до {m_max}: '))
    else:
        move = random.randint(1, m_max)
    return move


def player_output(name, candy, count, move):
    print(f'За этот ход {name} взял {move} конфет, всего у него {count}.\n'
          f'На столе осталось {candy} конфет.')


count1 = 0
count2 = 0

while candy > 11:
    if fortune:
        move = take_candy_amount(player)
        count1 += move
        candy -= move
        fortune = False
        player_output(player, candy, count1, move)
    else:
        move = take_candy_amount(bot)
        count2 += move
        candy -= move
        fortune = True
        player_output(bot, candy, count2, move)

if fortune:
    print(f'Выиграл {player}')
else:
    print(f'Выиграл {bot}')
