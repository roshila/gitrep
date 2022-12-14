# Напишите программу, которая будет делать анимацию кругов в случайных координатах. Цвета могут быть не такие, как в примере, но в целом должно быть похоже на это
# В этом уроке нужно создать холст с размерами 400 на 400 пикселей. Для изменения размеров холста нужно передать именованные аргументы width и height в вызов Canvas. То есть, вместо привычного

# canvas = tkinter.Canvas(window)
# используйте код
# canvas = tkinter.Canvas(window, width=400, height=400)
# Первым делом присвойте переменной colors кортеж из названий семи цветов. Каждый цвет — это строка. Цвета можно выбрать из списка на этой странице нашего справочника. Неважно, "Red" это или "White" — главное, чтобы цвета существовали и были разные.

# Потом в программе должен начаться бесконечный цикл, в каждой итерации которого должна быть анимация появления семи концентрических кругов с цветами из кортежа colors и радиусами 150, 155, 160, 165, 170, 175 и 180 пикселей. Для того чтобы сгенерировать последовательность из радиусов, используйте функцию range с шагом 5. Убедитесь, что последний радиус именно 180. Для получения индекса цвета, который будет совпадать с индексом радиуса, используйте функцию enumerate.

# Создавать круги нужно в цикле for. После создания круга не забудьте вызвать метод update, чтобы созданный круг отобразился на холсте. Если круги появляются слишком быстро, после рисования каждого из кругов делайте паузу в пять сотых секунды. Для того чтобы сделать паузу, импортируйте модуль time в начале программы, а после создания круга и обновления содержимого окна вызовите time.sleep(0.05)

# Перед циклом for нужно получить случайные координаты центра кругов. Сделать это нужно с помощью модуля random. Обе координаты можно получить с помощью одинаковой функции randint — она вернет случайное число от 0 до 400.
# random.randint(0, 400)

# Не забудьте импортировать модули random, tkinter и time в начале программы.

# P.S. Разумеется, холст не должен очищаться. Наш пример — это зацикленная gif‑ка и поэтому все время начинается с начала.
# import tkinter
# import time
# import random

# def random_oval():
#     x = random.randint(0, 400)
#     y = random.randint(0, 400)

#     for i, color in enumerate(colors):
#         r = radius[i]
#         canvas.create_oval(x-r ,y-r, x+r, y+r, outline=color)
#         canvas.update()
#         time.sleep(0.3)

# window = tkinter.Tk()
# canvas = tkinter.Canvas(window, width=400, height=400)
# canvas.pack()

# radius = (150, 155, 160, 165, 170, 175, 180)
# colors = ('red', 'green', 'blue', 'orange', 'purple', 'yellow', 'brown')

# while True:
#     random_oval()

# window.mainloop()