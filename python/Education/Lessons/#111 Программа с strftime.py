# Метод strftime преобразует дату/время в строку согласно переданному в качестве аргумента формату. С помощью strftime повторить результат «неправильной» программы из прошлого урока можно гораздо проще

# import datetime
# datetime_x = datetime.datetime.now()
# datetime_str = datetime_x.strftime("%Y.%m.%d")
# print(datetime_str)

# То есть, метод strftime заменяет коды в строке формата на значения из объекта даты/времени. Например, «%Y» будет заменен на текущий год, так как datetime_x — текущая дата/время. Вместо точек могут быть любые символы — они остануться без изменения

# import datetime
# datetime_x = datetime.datetime.now()
# datetime_str = datetime_x.strftime("%Y.%m.%d")
# print(datetime_str)
# datetime_str = datetime_x.strftime("%d/%m/%Y")
# print(datetime_str)

# 27 августа 2019 года эта программа вывела две вот такие строки

# Полный список этих кодов формата можно посмотреть в нашем справочнике

# В этом уроке надо написать программу, которая в переменную my_datetime запишет текущую дату/время.

# После этого программа должна вывести эту дату/время на экран. Если бы вы запускали эту программу 28 августа в 8 утра, получиться должно было следующее

# 28 Aug
# 08:00

# То есть, программа должна вывести текущее число, трехбуквенную аббревиатуру текущего месяца, а на следующей строке текущий час и минуты, разделенные двоеточием. Переменная my_datetime должна оставаться объектом даты/времени

# # 1 
# import datetime

# my_datetime = datetime.datetime.now()
# now = my_datetime.strftime("%d %b\n%H:%M")

# print(now)

# # 2 
# import datetime

# my_datetime = datetime.datetime.now()

# print(my_datetime.strftime('%d %b\n%H:%M'))