# Урок 1. Знакомство с Python

# Задача 2. Напишите программу для проверки истинности утверждения
# ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

for X in range(0, 2):
    for Y in range(0, 2):
        for Z in range(0, 2):
            print(f'X = {X}, Y = {Y}, Z = {Z}\
            {not (X or Y or Z) == (not X and not Y and not Z)}')
