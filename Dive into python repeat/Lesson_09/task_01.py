"""
Задание №1
Создайте функцию-замыкание, которая запрашивает два целых числа:
○ от 1 до 100 для загадывания,
○ от 1 до 10 для количества попыток
Функция возвращает функцию, которая через консоль просит
угадать загаданное число за указанное число попыток.
"""
from typing import Callable


def guessing_game(guessing: int, attempts: int) -> Callable:
    def wrapper():
        nonlocal attempts
        for i in range(attempts):
            print(f'Попытка №{i + 1}')
            var = int(input('Угадай число: '))
            if var == guessing:
                return 'Вы угадали, браво!!'
        return 'Количество попыток исчерпано!'

    return wrapper


if __name__ == '__main__':
    game1 = guessing_game(10, 3)
    game2 = guessing_game(3, 3)
    print(game1())
    print(game2())
