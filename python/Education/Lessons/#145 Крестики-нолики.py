# Первый финальный проект (и на данный момент последний) — это игра крестики-нолики. Написать ее надо с помощью объектно-ориентированного подхода. Поэтому первым делом создайте класс с названием TicTacToe. Да, именно так на английском называется эта игра. Класс TicTacToe должен быть потомком класса Canvas из модуля tkinter.

# У этого класса должен быть переопределен метод __init__. Принимать он должен единственный аргумент, кроме self. Этот аргумент должен называться window. Подразумевается, что это будет объект окна Tk, все как в обычном Canvas.

# Внутри переопределенного метода должен быть вызов родительского метода __init__. В него надо передать аргумент window, а также ширину и высоту, равную 300 пикселям.

# Далее нужно создать окно tkinter.Tk и объект класса TicTacToe. Объект класса TicTacToe назовите game. Не забудьте передать окно в качестве аргумента при его создании. Также нужно вызывать метод размещения в окне pack, а в самом конце вызвать метод окна mainloop.

# Уловили? Мы основываем свою игру на классе Canvas, получаем все его возможности через наследование и дополняем функциональность.
# # 1
# import tkinter
# from tkinter import Canvas

# window = tkinter.Tk()
# canvas = tkinter.Canvas(window)
# canvas.pack()

# class TicTacToe(Canvas):
#     def __init__(self, window):
#         super().__init__(window, width=300, height=300) 
#         self.window = window

# game = TicTacToe(window)
# game.window.mainloop()