"""
2. Реализовать функцию, принимающую несколько параметров,
описывающих данные пользователя: имя, фамилия, год рождения, город проживания, email, телефон.
Функция должна принимать параметры как именованные аргументы.
Реализовать вывод данных о пользователе одной строкой.

Пример:
Иван Иванов 1846 года рождения, проживает в городе Москва,
email: jackie@gmail.com, телефон: 01005321456
"""

def user_param(name, second_name, birthday, city, email, phone):
    return print (f'{name} {second_name} {birthday} года рождения, проживает в городе {city}, email: {email}, телефон {phone}')

user_param(name = 'Ilon', second_name = 'Mask', birthday = '2100', city = 'Keyptown', email = 'supermail', phone = '‪121211212‬')
