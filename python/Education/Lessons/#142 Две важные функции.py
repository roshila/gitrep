# Две важные функции в объектно-ориентированном программировании — это isinstance и issubclass.

# Первая из них, isinstance проверяет, является ли объект экземпляром указанного класса (одного из классов) или его подкласса

# class Pet:
#     def __init__(self, name):
#         self.name = name


# class Cat(Pet):
#     pass


# class Dog(Pet):
#     pass


# fil = Cat('Филимон')
# dan = Dog('Дэн')

# print(isinstance(fil, Cat))
# print(isinstance(dan, Cat))

# # Dog это подкласс Pet
# # поэтому isinstance вернет True
# print(isinstance(dan, Pet))

# # Вторым параметром функции может быть
# # и кортеж классов
# print(isinstance(fil, (Dog, Cat)))
# Вторая, issubclass, проверяет, является ли класс потомком класса или одного из классов

# print(issubclass(Cat, Dog))
# print(issubclass(Cat, Pet))

# Вторым аргументом этой функции также может быть кортеж из классов.