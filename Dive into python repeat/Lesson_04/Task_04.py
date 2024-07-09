"""
Задание №4
✔ Функция получает на вход список чисел.
✔ Отсортируйте его элементы in place без использования
встроенных в язык сортировок.
✔ Как вариант напишите сортировку пузырьком.
Её описание есть в википедии.
"""


def my_sort(lst: list[int]) -> None:
    for i in range(len(lst)):
        for j in range(len(lst) - i - 1):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]


nums = [5, 8, 2, 7, 3, 9, 1]
print(nums)
my_sort(nums)
print(nums)


# def my_sort(lst: list[int]) -> None:
#     for i in range(len(lst)):
#         is_sorted = True
#         for j in range(len(lst) - i - 1):
#             if lst[j] > lst[j + 1]:
#                 lst[j], lst[j + 1] = lst[j + 1], lst[j]
#                 is_sorted = False
#             else:
#                 return
#
#
# nums = [5, 8, 2, 7, 3, 9, 1]
# nums = [1, 2, 3, 4, 5, 6, 7]
# print(nums)
# my_sort(nums)
# print(nums)
