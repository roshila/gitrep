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
