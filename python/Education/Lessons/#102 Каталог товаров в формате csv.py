# В этом уроке нужно будет усовершенствовать программу из урока «Чтение данных для каталога». Чтение и запись в файл должны быть сделаны с помощью модуля csv.

# Помните, что разделитель в формате csv — это запятая. То есть старый файл, с двоеточием в качестве разделителя, не подойдет. Поэтому, создайте для этого задания новый файл с расширением .csv или подправьте старый файл так, чтобы он соответствовал формату csv.
# # 1 
# import csv

# catalog = {}
# with open("magaz.csv") as f:
#     rows = csv.reader(f)
#     for k, v in rows:
#         catalog[k] = int(v)

# for i in range(3):
#     key = input("Название товара: ")
#     value = int(input("Кол-во: "))
#     #проверяет есть ли этот ключ в каталоге
#     if catalog.get(key, 0) == 0:  # Нужно было использовать in
#         catalog[key] = value
#     else:
#         catalog[key] += value


# with open("magaz.csv", 'w') as f:
#     writer = csv.writer(f)

#     for item in catalog:
#         row = [item, catalog[item]]
#         writer.writerow(row)

# # 2 
# import csv

# catalog = {} 

# with open('csvcatalog.csv', 'r+') as file:
#     for name, number in csv.reader(file):
#         catalog[name] = int(number)

#     for i in range(3):
#         name = input('name of product: ')
#         number = int(input('How many? '))

#         if name in catalog:
#             catalog[name] += number
#         else:
#             catalog[name] = number

#     for key in catalog:
#         writer = csv.writer(file)
#         writer.writerow([key, catalog[key]])