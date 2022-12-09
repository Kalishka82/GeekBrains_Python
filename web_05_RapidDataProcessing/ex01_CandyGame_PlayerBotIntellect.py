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
move_max = int(input('Введите максимальное кол-во конфет, возможное за один ход move_max = '))
# print(candy % (move_max + 1))
fortune = random.randint(0, 2)


def take_candy_amount(name):
    if name == player:
        move = int(input(f'{name}, введите кол-во конфет от 1 до {move_max}: '))
        while move < 1 or move > move_max:
            move = int(input(f'{name}, введите кол-во конфет от 1 до {move_max}: '))
    else:
        move = random.randint(1, move_max)
    return move


def player_output(name, candy, count, move):
    print(f'{name} взял {move} конфет, всего у него {count}.\n'
          f'На столе осталось {candy} конфет.')


if fortune:
    print(f'Первый ход {player}')
    count2 = 0
else:
    print(f'Первый ход {bot}')
    move = candy % (move_max + 1)
    count2 = move
    candy -= move
    fortune = True
    player_output(bot, candy, count2, move)


count1 = 0

while candy > move_max:
    if fortune:
        move = take_candy_amount(player)
        count1 += move
        candy -= move
        fortune = False
        player_output(player, candy, count1, move)
    else:
        move = (move_max + 1) - move
        count2 += move
        candy -= move
        fortune = True
        player_output(bot, candy, count2, move)

if fortune:
    print(f'{player} - победитель')
else:
    print(f'{bot} - победитель')
