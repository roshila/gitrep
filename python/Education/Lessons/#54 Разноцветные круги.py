# from email.mime import image


# Напишите программу, которая рисует концентрические круги с центром в любой точке и радиусами от 5 до 95. Шаг изменения радиуса должен быть равен 5.

# Результатом работы программы должен быть такой вот рисунок

# lesson.700.1201

# Для рисования круга нужно использовать метод create_oval из модуля tkinter. Разумеется, перед использованием этого метода нужно импортировать модуль tkinter, создать холст и разместить его в окне.
# # импортируем tkinter
# import tkinter
# # создаем окно
# window = tkinter.Tk()
# # создаем холст и размещаем его в окне
# canvas = tkinter.Canvas(window)
# canvas.pack()

# # координаты левого верхнего 
# # угла прямоугольника, в который должен быть вписан круг
# x0 = 50
# y0 = 50

# # координаты правого нижнего 
# # угла прямоугольника
# x1 = 150
# y1 = 150

# canvas.create_oval(x0, y0, x1, y1)
# window.mainloop()
# Координаты верхнего левого угла прямоугольника для круга с центром в точке x, y и радиусом R будут равны x - R, y - R, а координаты правого нижнего — x + R, y + R

# Так вот, если радиус делится на 2 без остатка — цвет круга должен быть красным, иначе — серым.

# Чтобы изменить цвет, в create_oval нужно передать именованный аргумент outline. К примеру круг красного цвета с центром в точке 100, 100 и радиусом 100 можно создать вот так
# canvas.create_oval(0, 0, 200, 200, outline="red")
# а круг серого цвета с центром в точке 100, 100 и радиусом 50 — так
# canvas.create_oval(50, 50, 150, 150, outline="grey") 
# В программе обязательно используйте цикл for и функцию range. В самом конце программы не забудьте вызывать window.mainloop(), чтобы окно с рисунком не закрывалось.

# # 1 
# import tkinter
# window = tkinter.Tk()
# canvas = tkinter.Canvas(window)
# canvas.pack()
# for i in range(5,100,5):
#     if i % 2 == 0: canvas.create_oval(0 + i, 0 + i, 200 - i, 200 - i, outline="red")
#     else: canvas.create_oval(0 + i, 0 + i, 200 - i, 200 - i, outline="grey")
# window.mainloop()

# # 2 
# import tkinter
# import time
# import random

# window = tkinter.Tk()
# canvas = tkinter.Canvas(window)
# canvas.pack()

# colors = ['red', 'blue', 'purple', 'orange', 'black' ]

# def abcd_random():
#     global a, b, c ,d
#     a = random.randint(1, 300)
#     b = random.randint(1, 200) 
#     c = random.randint(1, 300)
#     d = random.randint(1, 200)

# def update():
#     canvas.update()
#     time.sleep(0.05)

# i = 0
# while i != 25:

#     abcd_random()

#     canvas.create_rectangle(a, b, c, d, outline = random.choice(colors))
#     update()

#     if i%2 == 0:

#         abcd_random()

#         canvas.create_line(a, b, c, d, outline = random.choice(colors))
#         update()

#         abcd_random()

#         canvas.create_oval(a, b, c, d, outline = random.choice(colors))
#         update()
#     i += 1

# print('Работа завершена')
# window.mainloop()