# В этом уроке нужно дополнить программу из предыдущего. Переменная catalog должна быть не пустой, а заполнена значениями из файла. То есть, нужно прочитать файл, разбить содержимое на строки и записать полученные данные в словарь. Текст до двоеточия должен быть ключом, а после двоеточия — количеством. Не забудьте преобразовать количество в целое число.

# Прочитать файл в текстовом формате можно не только с помощью метода read. Можно, например, использовать метод readlines — он сразу вернет содержимое файла, разбитое на строки


# with open('catalog.txt', 'r+') as f:
#     lines = f.readlines()
#     for line in lines:
#         print(line)


# А еще проще сразу «пройтись» циклом по файлу

# with open('catalog.txt', 'r+') as f:
#     for line in f:
#         print(line)

# Чтение файла сделайте так, как вам больше нравится. В остальном, программа должна оставаться прежней.

# В итоге, с каждым новым запуском, программа должна дополнять файл новой введенной информацией.

# # 1
# catalog = {}

# with open('new_catalog.txt', 'r+') as file:
#     for line in file:
#         key, value = line.split(':')
#         catalog[key] = int(value)

# for i in range(3):
#     name = input('Name of product: ')
#     amount = int(input('Amount: '))

#     if name in catalog:
#         catalog[name] += amount
#     else:
#         catalog[name] = amount

# with open('new_catalog.txt', 'a') as file_catalog:
#     for key in catalog:
#         file_catalog.write(f'{key}:{catalog[key]} \n')


# # 2 


# catalog = {}

# with open('catalog.txt', 'r+') as x:
#     for el in x:
#         key, value = el.split(':')
#         catalog[key] = int(value)

# for i in range(3):
#     key = input('Введите товар: ')
#     value = int(input('Введите количество: '))
#     if key in catalog:
#         catalog[key] += value
#     else: catalog[key] = value
# for k in catalog:
#     print(k, ':', catalog[k])

#     with open('catalog.txt', 'w') as x:
#         for el in catalog:
#             x.write(f'{el}:{catalog[el]}\n')


        