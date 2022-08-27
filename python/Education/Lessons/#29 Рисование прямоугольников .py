# Перед тем, как мы начнем рисовать, нужно сказать несколько слов о координатах. Координаты нужны для того, чтобы точно указать место, где мы хотим что‑то нарисовать.

# Весь холст состоит из точек и у каждой из этих точек есть две координаты: x и y. В левом верхнем углу находится точка с координатами (0, 0). Эта точка — начало нашей системы координат. То есть, координата x любой точки на холсте показывает, сколько точек надо отступить от начала координат вправо, а координата y — сколько точек нужно отступить от начала координат вниз.
# По умолчанию размеры холста равны 300 точек по горизонтали на 200 точек по вертикали. То есть, координата точки в нижнем правом углу (300, 200). Такие небольшие размеры выбраны для того, чтобы окно с холстом помещалось даже на экране смартфона. В одном из следующих уроков я обязательно расскажу, как изменять размеры холста, а пока что оставим все так, как есть.

# Нарисовать прямоугольник на холсте можно с помощью метода create_rectangle. Первые два аргумента этого метода — это координаты левого верхнего угла прямоугольника. Вторые два — координаты нижнего правого угла.
# Запустите вот такую программу и посмотрите на результат ее работы

# import tkinter
# window = tkinter.Tk()
# canvas = tkinter.Canvas(window)
# canvas.pack()
# canvas.create_rectangle(20, 40, 200, 150)
# window.mainloop()
# Обратите внимание, что вызов метода создания прямоугольника написан между вызовами pack() и mainloop()

# Чтобы пройти этот урок, нарисуйте два прямоугольника с любыми координатами. Главное, чтобы эти координаты не выходили за границы холста.
# # импортируем tkinter
# import tkinter
# # создаем окно
# window = tkinter.Tk()
# # создаем холст
# canvas = tkinter.Canvas(window)
# # размещаем в окне
# canvas.pack()
# # рисуем прямоугольники верхний ряд
# canvas.create_rectangle(10, 10, 60, 40)
# canvas.create_rectangle(70, 10, 120, 40)
# canvas.create_rectangle(130, 10, 180, 40)
# canvas.create_rectangle(190, 10, 240, 40)
# canvas.create_rectangle(250, 10, 300, 40)
# # второй ряд сверху
# canvas.create_rectangle(10, 50, 60, 80)
# canvas.create_rectangle(70, 50, 120, 80)
# canvas.create_rectangle(130, 50, 180, 80)
# canvas.create_rectangle(190, 50, 240, 80)
# canvas.create_rectangle(250, 50, 300, 80)
# # третий ряд сверху
# canvas.create_rectangle(10, 90, 60, 120)
# canvas.create_rectangle(70, 90, 120, 120)
# canvas.create_rectangle(130, 90, 180, 120)
# canvas.create_rectangle(190, 90, 240, 120)
# canvas.create_rectangle(250, 90, 300, 120)
# # четвертый ряд сверху
# canvas.create_rectangle(10, 130, 60, 160)
# canvas.create_rectangle(70, 130, 120, 160)
# canvas.create_rectangle(130, 130, 180, 160)
# canvas.create_rectangle(190, 130, 240, 160)
# canvas.create_rectangle(250, 130, 300, 160)
# # пятый ряд
# canvas.create_rectangle(10, 170, 60, 200)
# canvas.create_rectangle(70, 170, 120, 200)
# canvas.create_rectangle(130, 170, 180, 200)
# canvas.create_rectangle(190, 170, 240, 200)
# canvas.create_rectangle(250, 170, 300, 200)
# # запускаем графический интерфейс
# window.mainloop()

# # 2 
# from random import *
# import time
# import tkinter

# window = tkinter.Tk()
# canvas = tkinter.Canvas(window)
# canvas.pack()

# for x in range(0, 280, 60):
#     colors = choice(['blue', 'orange', 'green', 'red','yellow', 'violet'])
#     canvas.create_rectangle(10 + x, 10, 60 + x, 40, fill=colors)
#     canvas.create_rectangle(10 + x, 50, 60 + x, 80, fill=colors)
#     canvas.create_rectangle(10 + x, 90, 60 + x, 120, fill=colors)
#     canvas.create_rectangle(10 + x, 130, 60 + x, 160, fill=colors)
#     canvas.create_rectangle(10 + x, 170, 60 + x, 200, fill=colors)

# window.mainloop()

# # 3 
# from random import *
# import time
# import tkinter

# window = tkinter.Tk()
# canvas = tkinter.Canvas(window)
# canvas.pack()

# while True:
#     for x in range(0, 280, 60):    
#         colors = choice(['blue', 'orange', 'green', 'red','yellow', 'violet'])
#         canvas.create_rectangle(10 + x, 10, 60 + x, 40, fill=colors)
#         canvas.update()
#         time.sleep(0.01)
#         canvas.create_rectangle(10 + x, 50, 60 + x, 80, fill=colors)
#         canvas.update()
#         time.sleep(0.01)
#         canvas.create_rectangle(10 + x, 90, 60 + x, 120, fill=colors)
#         canvas.update()
#         time.sleep(0.01)
#         canvas.create_rectangle(10 + x, 130, 60 + x, 160, fill=colors)
#         canvas.update()
#         time.sleep(0.01)
#         canvas.create_rectangle(10 + x, 170, 60 + x, 200, fill=colors)

# window.mainloop()

# # 4 
# import tkinter
# window = tkinter.Tk()
# canvas = tkinter.Canvas(window)
# canvas.pack()
# canvas.create_rectangle(20, 40, 200, 150)
# canvas.create_rectangle(40, 60, 150, 100)
# window.mainloop()