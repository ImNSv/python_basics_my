"""
Задание 1.

Поработайте с переменными, создайте несколько,
выведите на экран, запросите у пользователя несколько чисел и
строк и сохраните в переменные, выведите на экран.

Пример:
Ведите ваше имя: Василий
Ведите ваш пароль: vas
Введите ваш возраст: 45
Ваши данные для входа в аккаунт: имя - Василий, пароль - vas, возраст - 45
"""
x = 10
y = 20
print("У нас есть перемеенные x и y - ", x, y)
name = input("Введите вашк имя ")
age = int(input("Сколько вам лет? "))
city = input("Из какого вы города? ")
print(f'Привет! Меня зовут {name}, мне {age} лет, я из города {city}')
