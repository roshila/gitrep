# Как уже было сказано, доступ к элементу и срезы доступны в обоих уже известных вам коллекциях — строках и списках. Чтобы немного попрактиковаться, напишите программу, которая переворачивает слова в предложении.

# Предложение должно быть получено от пользователя с помощью встроенной функции input и разбито на слова с помощью метода split.

# Полученный список слов нужно перевернуть при помощи среза с отрицательным шагом. Вы уже делали такое со строками в задаче про палиндром.

# Далее, из перевернутого списка слов нужно снова получить предложение. То есть склеить все слова в одну строку через пробел. Полученную строку нужно вывести на экран. То есть, если пользователь введет текст «Это интересная задача», программа должна вывести на экран
# задача интересная Это
# Склеить список в одну строку проще всего будет при помощи метода строк join.
# # элементы списка будут "склеены" через разделитель
# # в одну строку. В нашем случае разделитель -- это пробел
# result = ' '.join(['один', 'два', 'три']) 
# print(result)
# Запустите этот пример и вам сразу станет понятно, как этот метод работает. Описание этого метода есть в нашем справочнике метода строк.
# # 1 
# print(' '.join(input().split()[::-1]))
# # 2 
# string = input("Введите предложение: ").split()
# result = ' '.join(string[::-1]) 
# print(result)
# # 3 
# string = input('Введите текст: ')
# print(' '.join(string.split()[::-1]))