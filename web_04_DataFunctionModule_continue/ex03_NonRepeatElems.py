# Задача 3. Задайте последовательность чисел. Напишите программу, которая
# выведет список неповторяющихся элементов исходной последовательности.

nums = [1, 1, 2, 4, 5, 6, 7, 7, 8]


def non_repeat_elem(nums):
    res = []
    for i in nums:
        if nums.count(i) == 1:
            res.append(i)
    return res


print(non_repeat_elem(nums))
