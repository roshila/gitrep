# Следующий шаг — создание бота, который будет играть против нас. Добавьте в класс TicTacToe метод bot_move. Этот метод должен сделать следующее

# выбрать индекс случайной свободной ячейки из свойства state;

# присвоить в этом индексе state значение "o";

# вызвать метод add_o соответствующими аргументами column и row.

# Также нужно добавить вызов bot_move в обработчике клика click. Сразу же после того, как рисуется крестик

# # 1 
# import tkinter
# import random

# class TicTacToe(tkinter.Canvas):
#     def __init__(self, window):
#         self.window = window
#         canvas = super().__init__(window, width=300, height=300)
#         self.pack()
#         self.state = [None, None, None, None, None, None, None, None, None]
#         self.bind('<Button-1>', self.click)

#     def click(self, event):
#         column = event.x // 100
#         row = event.y // 100
#         index = column + row
#         if row == 1:
#             index += 2
#         elif row == 2:
#             index += 4
#         if self.state[index] == None:
#             self.state[index] = 'x'
#             self.add_x(column, row)
#             self.bot_move()
#         else:
#             pass

#     def bot_move(self):
#         i = random.randint(0, 8)
#         while self.state[i] != None:
#             i = random.randint(0, 8)
#             if None not in self.state:
#                 break
#         else:
#             self.state[i] = 'o'
#             if i < 3:
#                 column = i
#                 row = 0
#             elif i > 5:
#                 column = i - 6
#                 row = 2
#             else:
#                 column = i - 3
#                 row = 1
#             self.add_o(column, row)

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
# window.mainloop()