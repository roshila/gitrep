# Напишите программу, которая будет выводить текущее время на экран вот таким образом:
# https://letpy.com/static/lessons/lesson.1100.401.gif

# Как вы догадались, в этой программе, кроме модуля datetime, нужно использовать Canvas из модуля tkinter.

# Для того чтобы добавить текст на холст, нужно использовать метод create_text. Первые два аргумента этого метода — координаты текста. Именованным аргументом text можно установить отображаемый текст. Однако, этот текст у нас будет постоянно меняться, так как это часы. Поэтому при создании можно передать его значением пустую строку. А вот шрифт и цвет вполне можно задать. Цвет — задается уже знакомым нам именованным аргументом fill, а шрифт — font. Значением font должен быть кортеж из имени шрифта и его размера. Следующий код создаст на холсте текст «Привет, мир!» синего цвета в точке с координатами100, 100. Также будет использован шрифт «Arial» с размером 30 пикселей.
# canvas.create_text(100, 100, text='Привет, мир!', fill='blue', font=('Arial', 30))

# Как и любой метод создания фигур на холсте, create_text возвращает числовой идентификатор. Как вы уже знаете, его можно использовать для изменения координат и передвижения фигур с помощью метода move. Так вот, изменить свойства любой фигуры, в том числе и текста, можно с помощью метода itemconfig

# text_object = canvas.create_text(100, 100, text='Привет, мир!')
# canvas.itemconfig(text_object, text='Пока, мир.')

# Первый аргумент этого метода — числовой идентификатор. Далее нужно указать изменяемое свойство. Разумеется, можно изменять несколько свойств за один вызов itemconfig

# text_object = canvas.create_text(100, 100, text='Привет, мир!')
# canvas.itemconfig(text_object, text='Пока, мир.', fill='red')

# В общем, после создания текста на холсте в программе должен начинаться бесконечный цикл, в котором и должна происходить «магия» отображения текущего времени.

# P.S. Не забывайте вызывать метод холста update в каждой итерации бесконечного цикла.

# # 1 
# import tkinter
# import datetime

# window = tkinter.Tk()
# canvas = tkinter.Canvas(window)
# canvas.pack()

# clr = 'orange'
# fnt = ('Arial', 50)
# txt = ''

# obj = canvas.create_text(150, 75, text=txt, fill=clr, font=fnt)

# while True:
#     now = datetime.datetime.now()
#     hour = now.strftime("%H:%M:%S")
#     canvas.itemconfig(obj, text=hour)
#     canvas.update()

# window.mainloop()

# # 2 
# import tkinter
# import datetime

# window = tkinter.Tk()
# canvas = tkinter.Canvas(window)
# canvas.pack()

# text_object = canvas.create_text(150, 100, text='', fill='blue', font=('Arial', 30))

# while True:
#     canvas.itemconfig(text_object, text=datetime.datetime.now().strftime('%H:%M:%S'))
#     canvas.update()

# window.mainloop()