# При присваивании переменным, объекты передаются по ссылке. Точно так же, как, например, списки и словари. Если взять класс одного из прошлых уроков и попробовать написать вот такую программу

# class Cat:
#     def __init__(self, name):
#         self.name = name

#     def __str__(self):
#         return 'Кот {}'.format(self.name)


# fil = Cat('Филимон')
# cat = fil
# cat.name = 'Мурлыч'

# print(fil)
# то переменные cat и fil будут ссылаться на один и тот же объект.