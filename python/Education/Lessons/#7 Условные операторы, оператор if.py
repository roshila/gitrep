a = int(input('Введите число а')) # Разберёмся чё и почём, для начала вводим переменную а с числовым значением , которое вводит пользователь
if a > 10: # затем условный оператор сравнивает значение переменной а с каким то значением и в случае если условие if выполняется то
    print('Число больше 10') # выполняется программа "под" if 

#Программа "под" if буквально означает что if создаёт мини программу в коде, которая выполняется при определённом условии 
# также эта программа пишется в контейнере if, для создания этого контейнера нужно сделать 4 отступа от границы поля ввода либо одну табуляцию

#a = int(input('Введите число'))
#if a > 10:
#print('Число больше 10') # Всё бы ничего но программа видит ошибку на этой строке, потому что не соблюдена табуляция

#a = int(input('Введите текст'))
#if a > 10 #В этом примере компилятор видит ошибку в этой срочке, всему виной отсутствие : которое натурально означает
          #Если условие if выполняется ТО делать что-то дальше
#    print('Оно больше 10') 

a = int(input('ВВВедите число a'))
if a > 10:
    print('Число больше 10') # если результатом if является True то будет выполнена эта строчка 
print('Число действительно больше 10') # эта функция находится вне оператора if и будет выполнена в любом случае , даже если a < 10 

a = int(input('ВВЕДИ УЖЕ ЭТО ЧИСЛО А '))
if a > 10: 
    print('Число больше 10')
    print('Число действительно больше 10') #если нам важно соблюсти условие то функцию нужно прописать именно в операторе if


# а позже оказалось что есть ещё другие операторы
a = 3 + 2 #например оператор сложения +
b = a + 1
if b > a: #или оператор сравнения > 
    print('Умница')
else:
    print('Не, не катит')

# короче мир полон неизвестного , ты уже запомнил что ты можешь обьявить любую какую хошь переменную и задать ей какое хошь
# значение и если соблюдены условия Строгой типизации и ты не складываешь строку с числом то ты гений , не задерживайся тут 
# и иди дальше  
# оператор else может использоваться только в связке с оператором if
# программа под else будет выполняться только когда if возвращает false

from ast import If


a = int(input("Введите число"))
if a >= 10:                         # если условие if истинно то запускается программа внутри if
    print('Поздравляю, ваше число больше 10') # и мы видим этот текст
else:           # иначе (иначе = если условие ложно False ) мы видим этот текст 
    print('Не повезло, не фартануло, чило меньше 10')

# логика такова что по сути "если 2 + 2 равно 4 то ты учился в школе, если нет то ты не учился в школе "
a = 2 + 2
if a >= 4:
    print('Поздравляю, ты учился в школе')
else: 
    print('неуч')
    a = int(input('введи число')) #Условные оператор elif работает в связке с if else
if a > 10:                     #буквально можно сказать что код читается так :
    print('число больше 10')   #если a>10 делай так, иначе
elif a == 10:
    print('это десять')        # если a == 10 делай так
else:
    print('Число меньше 10')   #Иначе делай что-то ещё

# операторов elif в коде программы может быть сколько угодно

a = int(input('Введите число'))
if a > 10:
    print('Число больше 10')
elif a == 10:
    print('это десять')
elif a == 5:
    print('это пять')
elif a == 15:
    print('это пятнадцать')
else:
    print('число меньше десяти')
    # если при срабатывании условия необходимо выполнить только одну операцию то её можно записать в одну строку с условием
a = int(input('введите число'))
if a > 10: print('Число больше 10')
elif a < 10: print('Число меньше 10')
else: print('Это 10!')
# условные операторы могут быть вложены друг в друга и вместо использования and можно сделать вот так:
a = int(input('Введите число'))
if a > 10:
    if a < 20: # Второе условие будет проверяться только если истинно первое
        print('Число больше 10 , но меньше 20')
# способ с and никто не отменял, возможно в некоторых ситуациях он будет актуальнее 
a = int(input('Введите число'))
if a > 10 and a < 20:
    print('Число больше 10 и меньше 20')