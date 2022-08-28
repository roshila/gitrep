# Этот метод словаря возвращает коллекцию, похожую на список. Эта коллекция — итерируемая. То есть ее можно перебрать с помощью цикла for. Каждый элемент этой коллекции — это кортеж. С помощью этого метода можно сделать цикл по словарю более лаконичным. Эта

# my_dict = {"first": "Первый", "second": "Второй", 3: "Третий"}
# for key, value in my_dict.items():
#     print(key, ':', value)

# и эта программы

# my_dict = {"first": "Первый", "second": "Второй", 3: "Третий"}
# for key in my_dict:
#     print(key, ':', my_dict[key])

# сделают одно и тоже, но немного разными способами.

# Чтобы пройти этот урок, усовершенствуйте программу из урока «Словари и оператор in». Единственное, что нужно там изменить — это вывод результата на экран. Сделайте это с помощью метода items().

# # 1
# catalog = {}

# for i in range(3):
#     key = input('Какой товар желаете? ')
#     value = int(input('Кол-во товара: '))
#     if key in catalog:
#         catalog[key] = catalog[key] + value #оч подробно лучше +=
#     else:
#         catalog[key] = value

# for i, e in catalog.items():
#     print(i, ':', e)

# # 2 
# catalog ={}

# for i in range(1,4):
#     key = input("Введите наименование товара: ")
#     value = int(input("Введите количество: "))
#     if key in catalog:
#         value += catalog[key]
#     catalog[key] = value
# for x,v in catalog.items():
#     print(x, ':', v)

# # 3 
# catalog = {}
# for i in range(3):
#     key = input('Введите товар: ')
#     value = int(input('Введите количество: '))
#     if key in catalog:
#         value += catalog[key]
#     catalog[key] = value
# for k, v in catalog.items():
#     print(k, ':', catalog[k])