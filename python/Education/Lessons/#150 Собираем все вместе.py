# В этом уроке проверок не будет, потому что полноценно сыграть даже в такую простую игру, как крестики-нолики, нашему боту пока еще сложно.

# Написанный в прошлом уроке метод get_winner должен вызываться дважды внутри метода click. Первый раз — после того, как будет поставлен крестик пользователя. Если функция вернет что‑то, кроме None, должна быть выведена соответствующая надпись о победителе или ничьей на экран с помощью метода create_text. Помните, что наш класс TicTacToe — наследник класса Canvas, поэтому метод create_text нужно вызывать через self.

# Если функция вернет None, бот должен поставить нолик. Для этого нужно вызывать метод bot_move. После этого функция get_winner должна быть вызвана второй раз с аналогичными проверками на победителя.

# Да, после того, как на экран будет выведена информация о победителе или ничьей, можно сделать паузу в несколько секунд, перезаписать состояние игры списком из девяти None и начать игру заново.

# Чтобы очистить холст, используйте метод delete с аргументом "all". Вызывать его конечно же нужно через self

# self.delete("all")

# Также можно попробовать сделать бота более умным. Например, при определении следующего хода, делать копию состояния игры и изменяя это скопированное состояние проверять, какой ход может привести к победе, а какой — к поражению. Идеи, как это сделать, вырезки из исходного кода или написанные целиком игры вполне можно публиковать в вопросах для обсуждения.
# # 1
# #
# Алгоритм игры бота взят из книги Доусона «Программируем на Python»- рекомендую.
# Вопросы :
#  — не всегда с первого клика отрабатывается меню
#  — программа некорректно работает под IDLE

# import tkinter
# import random
# import time

# class TicTacToe(tkinter.Canvas) :

#     def __init__(self,window) :
#         self.window = window
#         self.canvas = super().__init__(window, width=300, height=300)
#         self.start()

#     def start(self):
#         self.state = [None,None,None,None,None,None,None,None,None]
#         self.create_text(150, 50, text='ИГРА "КРЕСТИКИ-НОЛИКИ"', fill='red', font=('Arial', 22))
#         self.create_text(150, 150, text='Кто будет ходить первым ?', fill='blue', font=('Arial', 22))
#         self.create_rectangle(0,200,300,250,fill='Yellow')
#         self.create_rectangle(0,250,300,300,fill='Green')
#         self.create_text(150, 225, text='Человек', fill='black', font=('Arial', 22))
#         self.create_text(150, 275, text='Компьютер', fill='black', font=('Arial', 22))
#         self.bind('<Button-1>',self.click_menu)
#         self.pack()


#     def click_menu(self,event):
#         if event.y > 250 :
#             self.delete('all')
#             game.draw_lines()
#             self.bot_move()
#             self.bind('<Button-1>',self.click_game)
#         elif event.y > 200 :
#             self.delete('all')
#             game.draw_lines()
#             self.bind('<Button-1>',self.click_game)
#         else :
#             pass


#     def draw_lines(self):
#         self.create_line(100, 0, 100, 300, fill='grey')
#         self.create_line(200, 0, 200, 300, fill='grey')
#         self.create_line(0, 100, 300, 100, fill='grey')
#         self.create_line(0, 200, 300, 200, fill='grey')

#     def add_o(self,column,row):
#         self.create_oval(20+column*100, 20+row*100, 80+column*100, 80+row*100, width=5, outline='red')

#     def add_x(self,column,row):
#         self.create_line(20+column*100, 20+row*100, 80+column*100, 80+row*100, width=5, fill='blue')
#         self.create_line(20+column*100, 80+row*100, 80+column*100, 20+row*100, width=5, fill='blue')

#     def bot_move(self):
#         # список доступных ходов
#         moves = []
#         for i in range(9):
#             if self.state[i] == None : moves.append(i)
#         # если следующим ходом компьютер может победить, выберем этот ход   
#         for n in moves:
#             self.state[n] = 'o'
#             if self.get_winner() == 'o_win':
#                 self.add_o(n%3,n//3)
#                 return
#         # выполнив проверку, отменим изменения
#             self.state[n] = None
#         # если следующим ходом может победить человек, выберем этот ход
#         for n in moves:
#             self.state[n] = 'x'
#             if self.get_winner() == 'x_win':
#                 self.state[n] = 'o'
#                 self.add_o(n%3,n//3)
#                 return
#         # выполнив проверку, отменим изменения
#             self.state[n] = None
#         # поскольку следующим ходом ни одна из сторон не побеждает, 
#         # выберем лучшее из доступных полей
#         for n in (4,0,2,6,8,1,3,5,7):
#             if n in moves:
#                 self.state[n] = 'o'
#                 self.add_o(n%3,n//3)
#                 return

#     def get_winner(self):
#         win = ((0, 1, 2),
#                    (3, 4, 5),
#                    (6, 7, 8),
#                    (0, 3, 6),
#                    (1, 4, 7),
#                    (2, 5, 8),
#                    (0, 4, 8),
#                    (2, 4, 6))
#         for row in win: 
#             if self.state[row[0]] == 'x' and self.state[row[1]] == 'x' and self.state[row[2]] == 'x':
#                 return 'x_win'
#         for row in win:
#             if self.state[row[0]] == 'o' and self.state[row[1]] == 'o' and self.state[row[2]] == 'o':
#                 return 'o_win'
#         if None in self.state :
#             return None
#         else :
#             return 'draw'

#     def game_over(self,t):
#         time.sleep(0.5)
#         self.delete('all')
#         self.create_text(150, 150, text=t, fill='red', font=('Arial', 24))
#         time.sleep(2)
#         self.delete('all')
#         self.start()


#     def click_game(self,event):
#         column = event.x // 100
#         row = event.y // 100
#         i = 3 * row + column
#         if self.state[i] == None :
#             self.state[i] = 'x'
#             self.add_x(column,row)
#             st = self.get_winner()
#             if st == 'x_win' :
#                 self.game_over('Победа игрока')
#             elif st == 'o_win' :
#                 self.game_over('Победа компьютера')
#             elif st == 'draw' :
#                 self.game_over('Ничья')
#             else :
#                 self.bot_move()
#                 st = self.get_winner()
#                 if st == 'x_win' :
#                     self.game_over('Победа игрока')
#                 elif st == 'o_win' :
#                     self.game_over('Победа компьютера')
#                 elif st == 'draw' :
#                     self.game_over('Ничья')
#                 else :
#                     pass

# window = tkinter.Tk()
# window.title("Крестики-нолики")
# game =  TicTacToe(window)

# window.mainloop()
# 0
# Сергей Котов — 9 дней назад
# не всегда с первого клика отрабатывается меню

# Если кликать на тексте, я полагаю? Это детали реализации под браузер к сожалению. В данных момент от них не избавиться.

# программа некорректно работает под IDLE

# Именно под IDLE? Или просто если в консоле запустить? И что именно работает не так как надо?

# P.S. Круто получилось! 


# # 2 
# Улучшил бота, протестите пожалуйста

# import tkinter
# import random
# import time


# class TicTacToe(tkinter.Canvas):
#     def __init__(self, window):
#         self.window = window
#         super().__init__(window, width=300, height=300, bg='grey')
#         self.pack()
#         self.state = [None, None, None, None, None, None, None, None, None]
#         self.winner = None
#         self.bind('<Button-1>', self.click)

#     def add_x(self, column, row):
#         self.create_line(column * 100 + 15, row * 100 + 15, column * 100 + 85, row * 100 + 85, width=5, fill='blue')
#         self.create_line(column * 100 + 85, row * 100 + 15, column * 100 + 15, row * 100 + 85, width=5, fill='blue')

#     def add_o(self, column, row):
#         self.create_oval(column * 100 + 15, row * 100 + 15, column * 100 + 85, row * 100 + 85, width=5, outline='red')

#     def draw_lines(self):
#         self.create_line(100, 0, 100, 300, fill='black')
#         self.create_line(200, 0, 200, 300, fill='black')
#         self.create_line(0, 100, 300, 100, fill='black')
#         self.create_line(0, 200, 300, 200, fill='black')

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
#             self.get_winner()
#             if self.winner == None:
#                 self.bot_move()
#             self.get_winner()
#             if self.winner != None:

#                 if self.winner == 'x_win':
#                     self.create_text(150, 150, text='Победа крестиков', fill='yellow', font=('Arial', '20', 'bold'))
#                 elif self.winner == 'o_win':
#                     self.create_text(150, 150, text='Победа ноликов', fill='yellow', font=('Arial', '20', 'bold'))
#                 elif self.winner == 'draw':
#                     self.create_text(150, 150, text='Ничья', fill='yellow', font=('Arial', '20', 'bold'))

#                 self.update()
#                 time.sleep(0.2)
#                 self.delete("all")
#                 self.state = [None] * 9
#                 self.draw_lines()
#                 self.winner = None
#                 time.sleep(0.25)
#     def bot_move(self):
#         o_is_None = [o for o, el in enumerate(self.state) if el is None]
#         win =  (['o','o'], ['x','x'])

#         for i in win:

#             if self.state[:2] == i and self.state[2] is None :
#                  o = 2
#                  break
#             elif self.state[2:7:4] == i and self.state[3] is None and self.state[4:7:2] != i:
#                 o = 3
#                 break
#             elif self.state[0:9:8] == i and self.state[3] is None:
#                 o = 3
#                 break
#             elif self.state[5:7] == i and self.state[2] is None:
#                 o = 2
#             elif self.state[3:5] == i and self.state[5] is None:
#                 o = 5
#                 break
#             elif self.state[6:8] == i and self.state[8] is None:
#                 o = 8
#                 break
#             elif self.state[0:4:3] == i and self.state[6] is None:
#                 o = 6
#                 break
#             elif self.state[1:5:3] == i and self.state[7] is None:
#                 o = 7
#                 break
#             elif self.state[2:6:3] == i and self.state[8] is None:
#                 o = 8
#                 break
#             elif self.state[0:5:4] == i and self.state[8] is None:
#                 o = 8
#                 break
#             elif self.state[2:5:2] == i and self.state[6] is None:
#                 o = 6
#                 break
#             elif self.state[4:9:4] == i and self.state[0] is None:
#                 o =0
#                 break
#             elif self.state[4:7:2] == i and self.state[2] is None:
#                 o = 2
#                 break
#             elif self.state[0:9:8] == i and self.state[4] is None or self.state[2:7:4] == i  and self.state[4] is None or self.state[1:8:6] == i and self. state[4] is None or self.state[3:6:2] == i and self.state[4] is None:
#                 o = 4
#                 break
#             elif self.state[1:3] == i and self.state[0] is None:
#                 o = 0
#                 break

#             elif self.state[7:9] == i and self.state[6] is None:
#                 o = 6
#                 break
#             elif self.state[0:7:6] == i and self.state[3] is None:
#                 o = 3
#                 break
#             elif self.state[2:9:6] == i and self.state[5] is None:
#                 o = 5
#                 break
#             elif self.state[4:8:3] == i and self.state[1] is None:
#                 o = 1
#                 break
#             elif self.state[0:3:2] == i and self.state[1] is None:
#                 o = 1
#                 break
#             elif self.state[6:9:2] == i and self.state[7] is None:
#                 o = 7
#                 break
#             elif self.state[3:7:3] == i and self.state[0] is None:
#                 o = 0
#                 break
#             elif self.state[5:9:3] == i and self.state[2] is None:
#                 o =2
#                 break
#             elif self.state[4] is None:
#                 o =4

#             elif self.state[0] is None:
#                 o = 0

#             elif self.state[2] is None:
#                 o = 2

#             elif self.state[6] is None:
#                 o = 6

#             elif self.state[8] is None:
#                 o = 8

#             else:
#                 o = random.choice(o_is_None)

#         row = o // 3
#         column = o % 3
#         self.state[o] = 'o'
#         self.add_o(column, row)

#     def get_winner(self):

#         symbols = ['x', 'x', 'x'], ['o', 'o', 'o']
#         combination = [
#             self.state[:3], self.state[2:9:3],
#             self.state[6:9], self.state[0:7:3],
#             self.state[3:6], self.state[0:9:4],
#             self.state[2:7:2], self.state[1:8:3]
#         ]
#         for symbol in symbols:
#             if symbol in combination:
#                 self.winner = f'{symbol[0]}_win'
#                 break

#             elif None not in self.state:
#                 self.winner = 'draw'


#         return self.winner


# window = tkinter.Tk()
# game = TicTacToe(window)
# game.draw_lines()

# window.mainloop()

# Это последний урок базового курса LETPY. Но это далеко не конец вашего пути в программировании. Если вас зацепило, то это только начало. Однако дальше двигаться придётся самостоятельно и лучше всего начать с книжек Марка Саммерфилд «Программирование на Python 3. Подробное руководство» и Марка Лутца — «Изучаем Python».

# Этот курс — базовый и его основная цель — дать общие представления о языке Python, переменных, типах данных, структурах и управляющих конструкциях языка. А еще этот курс сделан для того, чтобы зацепить и убедить вас, что программировать не так сложно, как кажется.

# Для раскрытия более глубоких и сложных тем мы будем добавлять новые крутые задачи и уроки, в которых расскажем о более сложных понятиях, таких как: функции высших порядков, рекурсии, классы, декораторы и т. д. О таких обновлениях мы обязательно сообщим в нашей рассылке.

# А еще, если конечно вам понравилось, можете оставить отзыв на нашей странице Facebook, ВКонтакте или же просто в блоке ниже :-)

# Если же есть вопросы — тоже смело пишите.
# 🤝 Классно, что понравилось!

# По поводу направления — обязательно поработайте с базами данных. Для начала можно и с sqlite даже, поддержка есть в Python «из коробки». Попробовать начать можно вот тут https://younglinux.info/sqlite/db

# Для закрепления можно прочитать еще Укус Питона. А чтобы потренироваться можно попробовать написать какое‑нибудь приложение для себя. Можно тот же список дел, но с сохранением в базу данных, отметками о выполнении, времени выполнения и так далее. На том же tkinter. Вот тут можно найти начальную информацию

# https://younglinux.info/tkinter/tkinter

# Здравствуйте. К сожалению аналогичных не знаю. Единственное что на ум приходит по SQL — это этот курс https://shultais.education/courses/sql но сам я его не проходил, поэтому подробностей не знаю. Кстати, у них же есть и по django что‑то.
