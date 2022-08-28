# Следующий шаг в создании игры — обработка хода пользователя. Для начала договоримся, что компьютер играет за нолики, а пользователь — за крестики.

# Для того чтобы хранить состояние игры, в методе __init__ присвойте свойству state значение списка из 9 значений None. Каждый из элементов этого списка будет соответствовать ячейке игрового поля. Значение None будет обозначать то, что ячейка свободна
# https://letpy.com/static/lessons/lesson.1300.1300.png

# Также нужно создать метод-обработчик клика по холсту. Метод-обработчик в отличие от функции должен принимать два аргумента — self и event. Называться этот метод должен click.

# Метод обработки нужно связать с событием клика. Сделать это нужно внутри метода __init__. Помните, что наш класс — наследник Canvas и все его методы мы можем вызывать через self
# self.bind('<Button-1>', self.click)
# Внутри метода-обработчика должно происходить следующее:

# По координатам клика (их можно получить из объекта события) нужно высчитать столбец и строку игрового поля, в котором произошел клик;
# С помощью получившихся значений необходимо высчитать соответствующий для них индекс в свойстве state;
# Далее, если значение свойства state в этом индексе равно None, нужно присвоить ему строковое значение "x". Если же ячейка уже занята, метод-обработчик должен завершиться;
# И в конце концов вызовите метод add_x с аргументами из первого пункта, чтобы нарисовать крестик в нужной ячейке игрового поля.
# # 1 
# import tkinter

# class TicTacToe(tkinter.Canvas):
#     def __init__(self, window):
#         a = super().__init__(window, width = 300, height = 300)
#         self.window = window
#         self.state = [None, None, None, None, None, None, None, None, None]
#         self.bind('<Button-1>', self.click)
#     def draw_lines(self):
#         c = 'grey2'
#         self.create_line(100, 0, 100, 300, fill=c)
#         self.create_line(200, 0, 200, 300, fill=c)
#         self.create_line(0, 100, 300, 100, fill=c)
#         self.create_line(0, 200, 300, 200, fill=c)
#     def add_x(self, column, row):
#         self.create_line(column*100+15, row*100+15, column*100+85, row*100+85, width=5, fill='red')
#         self.create_line(column*100+15, row*100+85, column*100+85, row*100+15, width=5, fill='red')
#     def add_o(self, column, row):
#         self.create_oval(column*100+15, row*100+15, column*100+85, row*100+85, width=5, outline='blue')
#     def click(self, event):
#         column = event.x // 100
#         row = event.y // 100
#         c = [(0, 3, 6), (1, 4, 7), (2, 5, 8)]
#         r = [(0, 1, 2), (3, 4, 5), (6, 7, 8)]
#         for el in c[column]:
#             if el in r[row]:
#                 i = el
#                 break
#         if self.state[i] == None:
#             self.state[i] = 'x'
#             self.add_x(column, row)

# window = tkinter.Tk()
# game = TicTacToe(window)
# game.pack()
# game.draw_lines()
# window.mainloop()
# 0
# ОС
# Оксана Сень — около 2 месяцев назад
# только с None вроде is

# 1
# Сергей Котов — около 2 месяцев назад
# только с None вроде is

# Да, именно is

# # 2 
# import tkinter

# class TicTacToe(tkinter.Canvas):
#     def __init__(self, window):
#         super().__init__(window, width = 300, height = 300)
#         self.state =[None, None, None, None, None, None, None, None, None]
#         self.bind('<Button-1>', self.click)

#     def add_x(self, column, row):
#         xy = [0, 100, 200]
#         self.create_line(10+xy[column], 10+xy[row], 90+xy[column], 90+xy[row], width = 5, fill='red')
#         self.create_line(90+xy[column], 10+xy[row], 10+xy[column], 90+xy[row], width = 5, fill='red')

#     def add_o(self, column, row):
#         xy = [0, 100, 200]
#         self.create_oval(10+xy[column], 10+xy[row], 90+xy[column], 90+xy[row], width = 5, outline = 'green')


#     def darw_lines(self):
#         self.create_line(100, 0, 100, 300, fill='grey')
#         self.create_line(200, 0, 200, 300, fill='grey')
#         self.create_line(0, 100, 300, 100, fill='grey')
#         self.create_line(0, 200, 300, 200, fill='grey')

#     def click(self, event):
#         x = event.x
#         y = event.y
#         new_x = x // 100
#         new_y = y // 100
#         ind = new_x + new_y*3
#         if self.state[ind] == None:
#             self.add_x(new_x,new_y)
#             self.state[ind] = "x"

# okno = tkinter.Tk()
# game = TicTacToe(okno)
# game.pack()
# game.darw_lines()

# okno.mainloop()
# Да, точно так. У вас это и сделано. Только на None все же принято проверять с помошью is