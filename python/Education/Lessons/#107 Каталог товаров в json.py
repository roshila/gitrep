# В этом уроке нужно в очередной раз переделать программу с каталогом товаров. На этот раз вместо сохранения и чтения данных в формате csv, нужно будет сделать хранение и чтение в формате json.

# Помните, что результат работы json.dumps — это строка и ее можно сохранить в файл с помощью метода write. А строку, которую нужно будет передать в json.loads можно получить, прочитав ее из файла с помощью read.

# Учтите, что если передать в json.loads пустую строку, программа завершится с ошибкой. Это случится из‑за того, что пустая строка не соответствует формату json. Чтобы избежать этой ошибки, создайте файл с содержимым {}. Такая строка преобразуется json.loads в пустой словарь, что, в общем‑то, нам и нужно.

# # 1 
# import json

# with open("magaz.json") as f:
#     line = f.read()
#     catalog = json.loads(line)

# # заполнение каталога
# for i in range(3):
#     key = input("Ключ: ")
#     value = int(input("Значение: "))

#     if key in catalog:
#         catalog[key] += value
#     else:
#         catalog[key] = value

# with open("magaz.json", "w+") as f:
#     s = json.dumps(catalog)
#     f.write(s)

# # 2 

# import json

# with open('catalog.json', 'r') as file:
#     t = file.read()
#     catalog = json.loads(t)
# print(catalog)

# for i in range(3):
#     key = input('Введите товар: ')
#     value = int(input('Введите количество: '))
#     if key in catalog:
#         catalog[key] += value
#     else: catalog[key] = value

# with open('catalog.json', 'w') as file:
#     c = json.dumps(catalog)
#     file.write(c)
# print(catalog)

# # 3 
# import json

# with open('catalog.json', 'r') as file:
#     reading = file.read()
#     catalog = json.loads(reading)

# for name in range(3):
#         name = input('Name of product: ')
#         number = int(input('How namy: '))

#         if name in catalog:
#             catalog[name] += number
#         else:
#             catalog[name] = number

# with open('catalog.json', 'w') as file:
#     jcatalog = json.dumps(catalog)
#     file.write(jcatalog)