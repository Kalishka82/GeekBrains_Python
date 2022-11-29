# Задача 4. Напишите программу, которая будет
# преобразовывать десятичное число в двоичное.

def decimal_to_binary(decimal):
    binary = str(decimal % 2)
    while decimal // 2 != 0:
        decimal = decimal // 2
        binary = str(decimal % 2) + binary
    return binary


print(decimal_to_binary(46))
print(decimal_to_binary(2))
