hello = 'Привет,'
name = input()
greeting = hello + name 
print(greeting)

#Можно сделать короче
name = input('what is your name?')
greeting = 'Hello,' + name 
print(greeting)

#Можно сделать ещё короче
name = input('what is your name?')
print('hello,' + name)

#МОЖНО ЕЩЁ КОРОЧЕ, ОДНОСТРОЧНЫЙ КОД РУЛИТ
print('hello, ' + input('what is your name?'))

hello = 'Привет пользователь'
name = input('представься')
greeting = ("Привет," + name)
print(greeting)