# В этом уроке нужно написать программу, которая выводит информацию о том, сколько осталось времени до часа «Икс».

# В переменную date_x должен быть записан объект даты/времени. Дата и время должны быть получены от пользователя в формате ДД.ММ.ГГГГ ЧЧ:ММ. Если пользователь вводит строку, несоответствующую формату, программа должна выводить на экран надпись «Ошибка».

# Если введенные дата/время меньше текущей, программа должна вывести надпись «Ошибка».

# Если дата/время соответствуют формату и date_x больше текущей даты/времени, программа должна вывести строку с сообщением о том, сколько времени осталось до часа «Икс».

# Если осталось меньше часа, то программа должна вывести количество оставшихся минут до часа «Икс»:

# До часа "Икс" 34 минуты
# Программа должна подбирать правильную форму для существительного «минута». Для этого можете смело взять свою функцию choose_plural из этой задачи.

# Если осталось больше часа, но меньше дня, строка будет такой:

# До часа "Икс" 1 час и 13 минут
# Слова «час» и «минута» должны быть правильной формы. Если количество оставшихся минут равно 0, то про минуты писать ничего не нужно и достаточно написать просто:
# До часа "Икс" 2 часа
# Если осталось больше одного дня, вывод программы должен быть таким:
# До часа "Икс" 2 дня и 1 час
# Про минуты писать ничего не нужно, а если количество оставшихся часов — 0, то достаточно будет написать просто:
# До часа "Икс" 2 дня
# Для получения количества дней используйте свойство days объекта timedelta.

# Для того, чтобы получить минуты и часы, делите количество секунд, полученное с помощью seconds, целочисленно, то есть оператором //.

# И еще, чтобы все ваши расчеты сработали верно и не вылезло ничего лишнего, уберите лишние секунды и микросекунды из текущей даты с помощью метода replace даты/времени. Его описание можно найти в справочнике.

# # 1 
# def choose_plural(num, tuptl):
#     per = num % 10
#     m = num % 100

#     if per==1 and m != 11:
#         return f'{num} {tuptl[0]}'

#     if (per <= 4 and per >= 2) and (m > 20 or m< 10):
#         return f'{num} {tuptl[1]}'

#     else:
#         return f'{num} {tuptl[-1]}'

# minutes = ("минута","минуты", "минут")
# hours = ('час', 'часа', 'часов')
# days = ('день', 'дня', 'дней')

# import datetime

# str_d = input("B формате ДД.ММ.ГГГГ ЧЧ:ММ ")
# now = datetime.datetime.now()
# now2 = now.replace(second = 0, microsecond = 0)
# many = 'До часа "Икс" '

# try:
#     date_x = datetime.datetime.strptime(str_d, '%d.%m.%Y %H:%M')
#     delta = date_x - now2

#     if now < date_x:
#         if (delta.total_seconds()// 3600) == 0 and delta.days == 0:
#             num = int(delta.total_seconds() // 60)
#             print(f'{many}{choose_plural(num, minutes)}')

#         if (delta.total_seconds() // 3600) >= 1 and delta.days < 1:
#             num = int(delta.total_seconds() // 3600)
#             nim = int(delta.total_seconds() // 60) % 60
#             print(f'{many}{choose_plural(num, hours)}', end=" ")
#             if num != 0:
#                 print(f'и {choose_plural(nim, minutes)}')

#         if delta.days > 0:
#             print(f'{many}{choose_plural(delta.days, days)}', end=" ")
#             num = (delta.total_second // 3600) % 24
#             if num != 0:
#                 print(f"и {choose_plural(num, hours)}")

#     else:
#         print("ошибка")

# except:
#     print("Ошибка")

# # 2 
# import datetime

# def choose_plural(number, list_):

#     number = str(number)

#     if int(number[-2:]) > 10 and int(number[-2:]) < 21:
#         return f'{number} {list_[2]}'

#     if number[-1] == '1':
#         return f'{number} {list_[0]}'

#     if int(number[-1]) > 1 and int(number[-1]) < 5:
#         return f'{number} {list_[1]}'

#     else:
#         return f'{number} {list_[2]}'

# try:
#     user_date = input('Введите дату и время часа X в формате ДД.ММ.ГГГГ ЧЧ:ММ ')
#     date_x = datetime.datetime.strptime(user_date, '%d.%m.%Y %H:%M')
#     now = datetime.datetime.now().replace(second=0, microsecond=0)

#     if date_x > now:
#         delta = date_x - now

#         days = delta.days
#         hours = delta.seconds // 3600
#         minutes = (delta.seconds % 3600) // 60

#         result = ''

#         if days > 0:
#             result = choose_plural(days, ['день', 'дня', 'дней'])
#             if hours > 0:
#                 result += ' и ' + choose_plural(hours, ['час', 'часа', 'часов'])

#         elif hours > 0:
#             result = choose_plural(hours, ['час', 'часа', 'часов'])
#             if minutes > 0:
#                 result += ' и ' + choose_plural(minutes, ['минута', 'минуты', 'минут'])

#         else:
#             result = choose_plural(minutes, ['минута', 'минуты', 'минут'])

#         print('До часа "Икс"', result)

#     else:
#         print('Ошибка')

# except ValueError:
#     print('Ошибка')