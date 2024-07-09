"""
Задание №6
✔ Функция получает на вход список чисел и два индекса.
✔ Вернуть сумму чисел между между переданными индексами.
✔ Если индекс выходит за пределы списка, сумма считается
до конца и/или начала списка.
"""


def my_func(some_list: list[int | float], i_first: int,
            i_last: int) -> int | float:
    i_first, i_last = sorted([i_first, i_last])
    i_first = 0 if i_first < 0 else i_first
    i_last = len(some_list) if i_last > len(some_list) else i_last
    return sum(some_list[i_first:i_last])


lst = [3, 4, 5, 2, 3, 1, 7, 9, 3]
print(my_func(lst, -5, 3))
