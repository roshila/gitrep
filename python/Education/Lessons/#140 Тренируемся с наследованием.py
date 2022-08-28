# Коты, собаки и еноты — это хорошо. Но давайте поупражняемся с какими‑то более приближенными к реальности вещами. Предположим, вы участвуете в разработке прогрессивного интернет-банкинга. Ваша работа — написать классы для пластиковых карт. Эти классы в свою очередь будут использовать другие программисты при отображении карточек в интерфейсе, выписках и т. д.

# Итак, напишите класс Card. В его метод инициализации должны передаваться следующие параметры: number, holder, valid_date и ccv. Далее должны создаваться поля с такими же названиями. Все поля (как и параметры метода инициализации) — это строки.

# Также в этом классе должен быть реализован метод get_hidden_number. Его задача — вернуть замаскированный с помощью звездочек номер карточки, то есть первые два символа из номера карточки, потом 10 звездочек и в самом конце последние 4 символа из номера карточки. Для номера

# 4200000000000001
# метод get_hidden_number должен вернуть
# 42** **** **** 0001
# Можете смело рассчитывать на то, что в номере карточки всегда будет 16 символов. Пробелы для разбивки номера на 4 части необязательны.

# Кроме класса Card должны быть написаны еще два: MasterCard и Visa. Родителем для этих двух классов должен быть класс Card. Каждый из классов MasterCard и Visa должен реализовывать свой метод __str__. Метод должен возвращать строку с наименованием карты, замаскированным номером и квадратными скобками в начале и конце.

# К примеру, для номера
# 4200000000000001
# и класса MasterCard это будет
# [mastercard 42** **** **** 0001]
# а для класса Visa
# [visa 42** **** **** 0001]
# Для получения замаскированного номера используйте вызов метода get_hidden_number внутри метода __str__.
# # 1 
# class Card:
#     def __init__(self, number, holder, valid_date, ccv):
#         self.number = number
#         self.holder = holder
#         self.valid_date = valid_date
#         self.ccv = ccv
#     def get_hidden_number(self):
#         stars = '*' * 10
#         self.number = stars.join([self.number[:2], self.number[-4:]])
#         return self.number
# class MasterCard(Card):
#     def __str__(self):
#         return '[mastercard {}]'.format(self.get_hidden_number())
# class Visa(Card):
#     def __str__(self):
#         return '[visa {}]'.format(self.get_hidden_number())

# card1 = MasterCard('4441118877340001', 'Kevin McCallister', '23.05', '335')
# card2 = Visa('4441118877340001', 'Kevin McCallister', '23.05', '335')
# print(card1)
# print(card2)

# # 2 
# class Card:
#     def __init__(self, number, holder, valid_date, ccv):
#         self.number = number
#         self.holder = holder
#         self.valid_date = valid_date
#         self.ccv = ccv
#     def get_hidden_number(self):
#         return f'{self.number[:2]}** {4*"*"} {4*"*"} {self.number[-4:]}'

# class Visa(Card):
#     def __str__(self):
#         return f'[Visa {self.get_hidden_number()}]'
# class MasterCard(Card):
#     def __str__(self):
#         return f'[MasterCard {self.get_hidden_number()}]'


# card1 = Visa('1111222233334444', 'Bobster', '07/25', '776')
# card2 = MasterCard('5555666677778888', 'Bobster', '07/25', '776')
# print(card1)
# print(card2)