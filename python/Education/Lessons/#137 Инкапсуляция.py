# Можно ли обойтись без классов и объектов? Разумеется. Можно использовать словарь для хранения данных, метод ask_for_food заменить на функцию и передавать в нее весь словарь целиком
# fil = {
#     "name": 'Филимон',
#     "is_fluffy": False,
#     "fails": []
# }

# def ask_for_food(cat):
#     print('Хозяин, кот {} требует пищу'.format(cat['name']))

# Это будет работать. Но что, если кроме котов нам понадобятся собаки, которые, как и коты, хотят поесть? Программа, скорее всего, будет выглядеть так
# den = {
#     "name": 'Дэн',
#     "is_fluffy": False,
#     "fails": []
# }

# fil = {
#     "name": 'Филимон',
#     "is_fluffy": False,
#     "fails": []
# }

# def cat_asks_for_food(cat):
#     print('Хозяин, кот {} требует пищу'.format(cat['name']))

# def dog_asks_for_food(dog):
#     print('Хозяин, пёс {} требует косточку'.format(dog['name']))

# Теперь для каждого питомца у нас своя функция. Если мы передадим в функцию dog_asks_for_food переменную fil, просьба кота будет выведена на экран по‑собачьи. А если вдруг мы «заведем» енота, придется «заводить» и третью функцию raccoon_asks_food.

# В общем, чем больше питомцев, тем больше бардак. Можно, конечно, добавить дополнительный ключ 'type' и оставить одну функцию
# def ask_for_food(pet):
#     if pet['type'] == 'cat':
#         print('Хозяин, кот {} требует пищу'.format(pet['name']))
#     elif pet['type'] == 'dog':
#         print('Хозяин, пёс {} требует косточку'.format(pet['name']))
#     # и так далее для все питомцев

# Ну вдруг нам понадобится написать еще какую‑то функцию для действий с питомцами? Все условия в ней придется писать повторно. К тому же, если мы захотим добавить в питомцы хомяка, нам нужно не забыть добавить условие уже в две функции.

# Если внимательно следить за всеми переменными и функциями, можно писать программы и таким способом. Однако, объектно-ориентированное программирование дает более подходящий инструмент для реализации подобного: класс связывает данные с методами в единое целое. Это связывание называется инкапсуляцией и это один из китов, на котором стоит объектно-ориентированное программирование.

# Для того, чтобы почувствовать прелесть инкапсуляции на практике, напишите программу, в которой будет три класса: Cat, Dog и Raccoon.

# У каждого из них должен быть определен метод инициализации __init__ с параметром name.

# Метод инициализации должен создавать поле объекта name со значением параметра, переданного при создании объекта.

# У каждого класса должен быть реализован метод ask_for_food. Он должен выводить на экран текст, в котором содержится значение поля name.

# # 1 
# class Cat:
#     def __init__(self, name):
#         self.name = name
#     def ask_for_food(self):
#         print('Cat {} asks for food!'.format(self.name))

# pirat = Cat('Pirat')
# pirat.ask_for_food()

# class Dog:
#     def __init__(self, name):
#         self.name = name
#     def ask_for_food(self):
#         print('Dog {} asks for food!'.format(self.name))

# reks = Dog('Reks')
# reks.ask_for_food()

# class Raccoon:
#     def __init__(self, name):
#         self.name = name
#     def ask_for_food(self):
#         print('Raccoon {} asks for food!'.format(self.name))

# tom = Raccoon('Tom')
# tom.ask_for_food()

# # 2 
# class Cat:
#     def __init__(self, name):
#         self.name = name

#     def ask_for_food(self):
#         print('Эй, двуногий, {} хочец кушоц'.format(self.name))

# class Dog:
#     def __init__(self, name):
#         self.name = name

#     def ask_for_food(self):
#         print(f'О, Великий, пёс {self.name} просит пищу')

# class Raccoon:
#     def __init__(self, name):
#         self.name = name

#     def ask_for_food(self):
#         print('Енот {} прополоскал всё белье и требует награду'.format(self.name))

# r = Raccoon('Евгений')
# d = Dog('Ричард')
# c = Cat("Пушок")

# zoo = r, d, c

# for i in zoo:
#     i.ask_for_food()