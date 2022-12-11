# Задача. Напишите программу вычисления арифметического выражения заданного строкой.
# Используйте операции +,-,/,*. приоритет операций стандартный.
# *Пример: *
# 2 + 2 = > 4;
# 1 + 2 * 3 = > 7;
# 1 - 2 * 3 = > -5;


evaluation = '12 - 6 / 3 * 6 + 5 * 2'
evaluation = evaluation.split()
print(evaluation)       # ['12', '-', '6', '/', '3', '*', '6', '+', '5', '*', '2']
print(12 - 6 / 3 * 6 + 5 * 2)   # 10.0 - необходимый результат


def calculate_eval(action, inner_str):
    for i in range(1, len(inner_str) - 1):
        if inner_str[i] == action:
            if action == '*':
                inner_str[i - 1] = float(inner_str[i - 1]) * float(inner_str[i + 1])
            elif action == '/':
                inner_str[i - 1] = float(inner_str[i - 1]) / float(inner_str[i + 1])
            elif action == '+':
                inner_str[i - 1] = float(inner_str[i - 1]) + float(inner_str[i + 1])
            elif action == '-':
                inner_str[i - 1] = float(inner_str[i - 1]) - float(inner_str[i + 1])
            inner_str.pop(i + 1)
            inner_str.pop(i)
            break
    return inner_str


"""В этом цикле while функция calculate_eval отрабатывает отлично! 
Но так задается четкая последовательность выполнения операций * / + -, которая неверна 
и, естественно, дает неверный результат расчета...см ниже пошаговую разбивку
['12', '-', '6', '/', '3', '*', '6', '+', '5', '*', '2']
['12', '-', '6', '/', 18.0, '+', '5', '*', '2']
['12', '-', '6', '/', 18.0, '+', 10.0]
['12', '-', 0.3333333333333333, '+', 10.0]
['12', '-', 10.333333333333334]
[1.666666666666666]
1.67"""

# while len(evaluation) > 1:
#     if evaluation.count('*'):
#         evaluation = calculate_eval('*', evaluation)
#     elif evaluation.count('/'):
#         evaluation = calculate_eval('/', evaluation)
#     elif evaluation.count('+'):
#         evaluation = calculate_eval('+', evaluation)
#     elif evaluation.count('-'):
#         evaluation = calculate_eval('-', evaluation)
#
# print(round(evaluation[0], 2))


"""При попытке распределить операции * и /, после + и - в порядке их появления четко видно
(специально на каждом шаге добавила print(evaluation)), что первый цикл while отрабатывается
в верной последовательности до момента, когда в выражении остаются только + и -,
но дальше он на этом месте зависает, не выходит из него! 
и почему-то в следующий цикл while для + и - не переходит!
Не могу найти причину, что не так делаю, по логике вроде все должно работать!!!
['12', '-', '6', '/', '3', '*', '6', '+', '5', '*', '2']
['12', '-', 2.0, '*', '6', '+', '5', '*', '2']
['12', '-', 12.0, '+', '5', '*', '2']
['12', '-', 12.0, '+', 10.0]
до этого момента все правильно считает, дальше зависает и ни туда, и ни сюда
Перебрала уже 100500 вариантов с брейками, но к положительному результату
так и не пришла! Помогите, плииииииз"""


while len(evaluation) > 1:
    while '*' or '/' in evaluation:
        if '*' and '/' in evaluation:
            if evaluation.index('*') < evaluation.index('/'):
                evaluation = calculate_eval('*', evaluation)
                print(evaluation)
            else:
                evaluation = calculate_eval('/', evaluation)
                print(evaluation)
        elif '*' in evaluation:
            evaluation = calculate_eval('*', evaluation)
            print(evaluation)
        elif '/' in evaluation:
            evaluation = calculate_eval('/', evaluation)
            print(evaluation)

    while '+' or '-' in evaluation:
        if '+' and '-' in evaluation:
            if evaluation.index('+') < evaluation.index('-'):
                evaluation = calculate_eval('+', evaluation)
                print(evaluation)
            elif evaluation.index('+') > evaluation.index('-'):
                evaluation = calculate_eval('-', evaluation)
                print(evaluation)
        else:
            if '+' in evaluation:
                evaluation = calculate_eval('*', evaluation)
                print(evaluation)
            elif '-' in evaluation:
                evaluation = calculate_eval('/', evaluation)
                print(evaluation)

print(round(evaluation[0], 2))
