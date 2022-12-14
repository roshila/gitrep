# Как уже было сказано в прошлом уроке, объект даты/времени можно запросто вывести на экран:

# import datetime
# datetime_x = datetime.datetime.now()
# print(datetime_x)
# Попробуйте, в результате выполнения такой программы на экран будет выведена дата и время в следующем формате
# 2019-08-26 15:33:15.757999

# То есть дата будет представлена в виде строки с годом из 4-х цифр, знака «-», номера месяца с лидирующим нулем, следующего знака «-» и номера дня в месяце, опять же с лидирующим нулем. После идут часы, минуты и секунды с лидирующими нулями, разделенные знаком «:». В самом конце, после точки идут микросекунды.

# В реальных программах дату/время нужно показывать в привычном человеку виде. То есть, например месяц нужно вывести после числа, а число может быть без лидирующего нуля. Например так

# 26 сентября 2019
# 26.09.2019
# 26.09.2019 15:33

# Есть два пути преобразовать дату в нужную строку. Первый способ — преобразовывать части даты/времени в строки и склеивать с друг другом и разделяющими символами. Этот способ неправильный и так делать точно не стоит. Мы вывели только дату, без времени и без наименования месяца, а в коде получилась какая‑то каша:

# import datetime
# datetime_x = datetime.datetime.now()
# datetime_str = str(datetime_x.year).zfill(4) + '.' + str(datetime_x.month).zfill(2) + '.' + str(datetime_x.day).zfill(2)
# print(datetime_str)

# Второй, правильный способ — это использовать метод strftime, подробнее о нем вы узнаете в следующем уроке.