# В этом уроке нужно написать программу, которая получает строку от пользователя с помощью input. Программа должна разделить строку на слова по символу пробела, точке или запятой и подсчитать, сколько раз каждое из слов встречается в строке. Разбить на слова будет проще, если предварительно заменить точки и запятые на символы пробела. Слова должны считаться одинаковыми без учёта регистра. То есть «Питон» и «питон» — одно и то же слово. Пустые слова, которые могут появиться из‑за двух и более пробелов подряд, не должны участвовать в подсчёте.

# Программа должна вывести слово, знак двоеточия и число раз, которое это слово встречается. Выглядеть это должно примерно так:

# программировали : 2
# да : 1
# не : 1
# выпрограммировали : 1
# В этом уроке не будет конкретных указаний для выполнения. Думать придется самостоятельно. Однако, можно с уверенностью сказать, что знания о словарях вам пригодятся.
# # 1 
# user = input("Sentence: ")
# list_ = user.lower().replace(".", " ").replace(",", " ").split()
# catalog = {}

# for el in list_:
#     if el in catalog:
#          catalog[el] += 1
#     else:
#         catalog[el] = 1

# for i in catalog:
#     print(i, ":", catalog[i])

# # 2 
# my_list = input().lower().replace('.', ' ').replace(',', ' ').rsplit()
# my_dict = {}
# for i in my_list:
#     if i in my_dict:
#         continue
#     kolvo = my_list.count(i)
#     my_dict[i] = kolvo
# for k in my_dict:
#     print(k, ':', my_dict[k])