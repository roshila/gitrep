#перенос строки в коде можно осуществить тремя способами
from sqlite3 import Row


a = "Первая строка \nВторая строка"
print(a)
#положение \n относительно текста  имеет значения 
a = "Первая строка\n Вторая строка" #в таком случае вторая строка появится с небольшим отступом
print(a)
# и тут тоже 
a = "Первая строка \n Вторая строка"
print(a)

#способ 2 и 3 
a = """first row
second row"""
print(a)
a = '''first row
second row'''
print(a)
# перенос сроки ещё раз
a = "First row \nSecond 1row""" #такой код не выдаст ошибки
print(a)

