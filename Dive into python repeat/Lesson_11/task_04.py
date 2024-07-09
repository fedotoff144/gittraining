"""
Задание №4
Доработаем класс Архив из задачи 2.
Добавьте методы представления экземпляра для программиста
и для пользователя.
"""


class Archive:
    """Та еще задачка"""
    num_arch, string_arch = [], []

    def __init__(self, num, string):
        """Та еще функция. В той еще задаче"""

        self.num = num
        self.string = string
        self.num_arch.append(num)
        self.string_arch.append(string)

    def __str__(self):
        """Информация для юзера"""
        return f'Number: {self.num}, String: {self.string}, Archive: {list(zip(self.num_arch, self.string_arch))}'

    def __repr__(self):
        """Информация для разработчика"""
        return f'Archive: {self.num}, {self.string}'


a = Archive(5, 'gfh')
b = Archive(2, 'od')

print(a)
print(f'{a}')
print(repr(b))
print(f'{b=}')
