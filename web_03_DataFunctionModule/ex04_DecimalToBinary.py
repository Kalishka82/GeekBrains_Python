# Задача 4. Напишите программу, которая будет
# преобразовывать десятичное число в двоичное.


def dec_to_bin_rec(decimal):
    if decimal == 0:
        return ''
    else:
        return f'{dec_to_bin_rec(decimal // 2)}{decimal % 2}' if decimal > 0 else ''


print(dec_to_bin_rec(46))

exit()


def decimal_to_binary(decimal):
    binary = str(decimal % 2)
    while decimal // 2 != 0:
        decimal = decimal // 2
        binary = str(decimal % 2) + binary
    return binary


print(decimal_to_binary(46))
print(decimal_to_binary(2))
