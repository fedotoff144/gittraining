"""
Задание №3
Создайте класс с базовым исключением и дочерние классыисключения:
○ ошибка уровня,
○ ошибка доступа.
"""


class UserException(Exception):
    pass


class LevelError(UserException):
    pass


class AccessError(UserException):
    pass
