# В этом уроке нужно добавить два метода в класс TicTacToe. Один должен называться add_x, а второй — add_o. У каждого из этих методов, кроме self, должны быть еще два аргумента — column и row. Это колонка и строка, в которой нужно нарисовать крестик либо нолик. Нумерация должна начинаться с нуля
# https://letpy.com/static/lessons/lesson.1300.1200.png

# То есть, вызов add_x(2, 0) должен нарисовать крестик в правом верхнем, а add_o(0, 2) — нолик в нижнем левом углу игрового поля.

# Чтобы все выглядело красивее, можете нарисовать линии, разделяющие поле на клетки. Сделать это желательно в отдельном методе, который можно назвать draw_lines. Для рисования линий используйте метод create_line. Наш класс TicTacToe — потомок класса Canvas, поэтому внутри него методы для рисования фигур можно вызывать через self
# def draw_lines(self):
#     # Первая вертикальная линия серого цвета
#     self.create_line(100, 0, 100, 300, fill='grey')

# Размеры клеток, как нетрудно догадаться из размеров холста, 100 на 100 пикселей.

# Для проверки разделяющие линии рисовать необязательно, поэтому давайте вернемся к методам add_x и add_o.

# Метод add_o должен рисовать нолик в нужной ячейке с помощью метода create_oval. Ширину линии нолика можно указать с помощью именованного аргумента width, а цвет линии с помощью outline. Вот так, к примеру, можно нарисовать круг с шириной линии 5 пикселей красным цветом
# self.create_oval(0, 0, 100, 100, width=5, outline='red')
# Метод add_x должен рисовать крестик с помощью двух пересекающихся линий. Ширину линии можно указать с помощью такого же, как и в create_oval, именованного аргумента width. За цвет линии отвечает аргумент fill.

# Цвета можно выбрать уже на знакомой вам странице.https://letpy.com/handbook/tkinter-colors/
# #1 
# import tkinter

# class TicTacToe(tkinter.Canvas):
#     def __init__(self, window):
#         a = super().__init__(window, width = 300, height = 300)
#         self.window = window
#     def draw_lines(self):
#         self.create_line(100, 0, 100, 300, fill='grey')
#         self.create_line(200, 0, 200, 300, fill='grey')
#         self.create_line(0, 100, 300, 100, fill='grey')
#         self.create_line(0, 200, 300, 200, fill='grey')
#     def add_x(self, column, row):
#         self.create_line(column*100, row*100, column*100+100, row*100+100, width=5, fill='red')
#         self.create_line(column*100, row*100+100, column*100+100, row*100, width=5, fill='red')
#     def add_o(self, column, row):
#         self.create_oval(column*100, row*100, column*100+100, row*100+100, width=5, outline='blue')

# window = tkinter.Tk()
# game = TicTacToe(window)
# game.pack()
# window.mainloop()

# # 2 
# import tkinter

# class TicTacToe(tkinter.Canvas):

#     def __init__(self, window):
#         self.window = window
#         canvas = super().__init__(window, width=300, height=300)
#         self.pack()

#     def check(self, column, row):
#         x = 20
#         y = 20
#         if column == 0:
#             if row == 1:
#                 y += 100
#             elif row == 2:
#                 y += 200
#         elif column == 1:
#             x += 100
#             if row == 1:
#                 y += 100
#             elif row == 2:
#                 y += 200
#         else:
#             x += 200
#             if row == 1:
#                 y += 100
#             elif row == 2:
#                 y += 200
#         return x, y    
#     def draw_lines(self):
#         self.create_line(100, 0, 100, 300, fill='black', width=1)
#         self.create_line(200, 0, 200, 300, fill='black', width=1)
#         self.create_line(300, 0, 300, 300, fill='black', width=1)
#         self.create_line(0, 100, 300, 100, fill='black', width=1)
#         self.create_line(0, 200, 300, 200, fill='black', width=1)
#     def add_x(self, column, row):
#         x, y = self.check(column, row)
#         self.create_line(x, y, x+60, y+60, fill='blue', width=5)
#         self.create_line(x+60, y, x, y+60, fill='blue', width=5)
#     def add_o(self, column, row):
#         x, y = self.check(column, row)
#         self.create_oval(x, y, x+60, y+60, outline='red', width=5)

# window = tkinter.Tk()
# game = TicTacToe(window)
# game.draw_lines()
# game.add_x(2, 0)
# game.add_o(0, 2)
# window.mainloop()