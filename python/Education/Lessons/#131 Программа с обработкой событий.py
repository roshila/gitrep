# В этом уроке надо написать программу, которая по клику мышкой будет рисовать круг с любым радиусом, можно случайным. Центром круга должны быть координаты клика.

# Также можно сделать так, чтобы цвет круга при каждом клике выбирался случайно.

# Функция обработки клика должна называться my_click. У функции обязательно должен быть один аргумент. Назвать его можно так, как хотите.
# # 1 
# import tkinter
# import random

# window = tkinter.Tk()
# canvas = tkinter.Canvas(window)
# canvas.pack()


# def my_click(event):
#     x, y = event.x, event.y
#     R = random.randint(5, 26)

#     x0, y0 = x - R, y - R
#     x1, y1 = x + R, y + R

#     canvas.create_oval(x0, y0, x1, y1, outline = 'red') if R % 2 == 0 else canvas.create_oval(x0, y0, x1, y1, outline = 'grey')


# canvas.bind('<Button-1>', my_click)
# window.mainloop()

# # 2 
# import tkinter
# import random

# window = tkinter.Tk()
# canvas = tkinter.Canvas(window, width=750, height=750)
# canvas.pack()

# colors = [
#     'AliceBlue', 
#     'CornflowerBlue', 
#     'chartreuse3', 
#     'DarkGoldenrod1', 
#     'purple',
#     'SeaGreen1',
#     'MidnightBlue',
#     'medium spring green',
#     'grey1',
#     'black'
#     ]

# def my_click(event):
#     size = random.randint(5, 75)
#     canvas.create_oval(
#         event.x - size, 
#         event.y - size, 
#         event.x + size, 
#         event.y +size, 
#         outline = random.choice(colors),
#         fill = random.choice(colors))

# canvas.bind('<Button-1>', my_click)
# window.mainloop()