#Переменные хранят данные, функции взаимодействуют с данными, хранящимися в переменной 
#Чтобы функция запустилась её нужно вызвать, в Python функция вызывается по скобкам после её названия ()
#Всё, что находится внутри скобок, называется аргументами или параметрами функции
a = 1
b = 2
c = 3
print(a,b,c) #a,b,c - это аргументы функции print
#При вызове функции код основной программы останавливается и начинает выполняться код функции
#После того как выполнение закончено, управление возвращается в основную программу вместе с результатом выполнения функции

a = 23
b = 13
c = b % a 
print(c) # print не возвращает результат функции, она лишь выводит текст на экран

m = abs(-10) # функция abs возвращает в переменную модуль числа -10 , то есть возвращает 10 
print(m)