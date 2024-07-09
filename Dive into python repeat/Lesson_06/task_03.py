"""
Задание №3
� Улучшаем задачу 2.
� Добавьте возможность запуска функции “угадайки” из
модуля в командной строке терминала.
� Строка должна принимать от 1 до 3 аргументов: параметры
вызова функции.
� Для преобразования строковых аргументов командной
строки в числовые параметры используйте генераторное
выражение.
"""

import random
from sys import argv

__all__ = ['guess_number']


def guess_number(lower_limit: int, upper_limit: int, attempts: int) -> bool:
    hidden_number = random.randint(lower_limit, upper_limit)
    for item in range(1, attempts + 1):
        print(f"Attempt number: {item}")
        user_num = int(input("Enter a number of your choice:\n"))
        if user_num < hidden_number:
            print("Your number is less then the target number")
        elif user_num > hidden_number:
            print("Your number is greater then the target number")
        else:
            print("You are right")
            return True
    print("You exhausted all attempts")
    return False


if __name__ == '__main__':
    print(argv)
    # guess_number(int(argv[1]), int(argv[2]), int(argv[3]))
    # guess_number(*(int(num) for num in argv[1:]))
    name, *param = argv
    print(param)
    # guess_number(*(int(num) for num in param))
