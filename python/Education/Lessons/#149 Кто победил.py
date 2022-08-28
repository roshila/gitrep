# Есть три варианта завершения игры в крестики-нолики: победа ноликов, победа крестиков или ничья, если все клетки игрового поля заполнены, но нет ни трех крестиков, ни трех ноликов, расположенных в одну линию.

# Для определения состояния игры нужно написать метод get_winner. В зависимости от состояния игрового поля state, get_winner должен возвращать следующие значения:

# строку 'x_win', если на поле есть три крестика в одну линию или по диагоналям;
# строку 'o_win', если на поле есть три нолика в одну линию или по диагоналям;
# строку 'draw', если все клетки заполнены, но победителя нет:
# None, если победителя нет и остались свободные клетки.
# # 1 
# Сначало в методе get_winner() я использовал кучу elif-ов, но потом увидел что можно проще сделать со срезами и так и сделал, я изначально хотел похожим образом сделать но я не знал что в срезах можно указывать шаг, в общем, вот решение:

# import tkinter
# import random

# class TicTacToe(tkinter.Canvas):

#     def __init__(self, window):
#         self.window = window
#         canvas = super().__init__(window, width=300, height=300)
#         self.pack()
#         self.state = [None, None, None, None, None, None, None, None, None]
#         self.winner = None
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
#             self.get_winner()
#         else:
#             pass

#     def bot_move(self):
#         i = random.randint(0, 8)
#         while self.state[i] != None or self.winner != None:
#             i = random.randint(0, 8)
#             if None not in self.state or self.winner != None:
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

#     def get_winner(self):
#         winner_x = ['x', 'x', 'x']
#         winner_o = ['o', 'o', 'o']
#         combination = [
#             self.state[0:3], self.state[3:6], self.state[6:9], 
#             self.state[0:7:3], self.state[1:8:3], self.state[2:9:3], 
#             self.state[0:9:4], self.state[2:7:2]
#         ]
#         if winner_x in combination: self.winner = 'x_win'
#         elif winner_o in combination: self.winner = 'o_win'
#         else:
#             if None not in self.state:
#                 self.winner = 'draw'
#         print(self.winner)
#         return(self.winner)

# window = tkinter.Tk()
# game = TicTacToe(window)
# game.draw_lines()
# window.mainloop()