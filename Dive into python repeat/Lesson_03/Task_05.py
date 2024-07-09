"""
Задание №5
Погружение в Python | Коллекции
✔ Создайте вручную список с повторяющимися целыми числами.
✔ Сформируйте список с порядковыми номерами
нечётных элементов исходного списка.
✔ Нумерация начинается с единицы.
"""
data = [42, 73, 5, 42, 42, 2, 3, 5, 7, 73, 42]
new_data = []

for i, item in enumerate(data, 1):
    if item % 2 == 1:
        new_data.append(i)

print(f'{new_data = }')

new_data1 = [i for i, item in enumerate(data, 1) if item % 2 == 1]
print(f'{new_data1 = }')
