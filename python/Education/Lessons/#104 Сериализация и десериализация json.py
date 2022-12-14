# Очень часто общая структура программы, работающей с данными выглядит так:

# Программа читает файл с данными. Например, это может быть каталог товаров;

# Программа что‑то делает с данными. Например, она может вычислить, какие из товаров заканчиваются;

# Программа записывает в файл обработанные данные. В нашем примере товары, которых осталось мало.

# Так вот, преобразование переменных программы (словарей, списков) в формат для хранения называется «сериализацией», а обратное преобразование — «десериализацией».

# В одном из предыдущих уроков вы делали такие преобразования с каталогом товаров. Сначала читали данные, потом преобразовывали их в словарь, дополняли данные в словаре вводом от пользователя и сохраняли обновленный каталог в тот же самый файл.

# Для сериализации и десериализации в формат json в Python есть модуль, который так и называется — json. JSON — текстовый формат, поэтому сериализация в него — это по сути преобразование в строку и обратно.

# Для сериализации используется функция dumps из модуля json. Для того, чтобы сериализовать данные с ее помощью, достаточно передать в нее аргументом любую переменную. Запустите программу и посмотрите, что она выведет на экран.


# import json

# fake_dict = {
#     'key_1': 1,
#     'key_2': 'any string'
# }

# s = json.dumps(fake_dict)
# print(type(s), s)

# Обратите внимание на кавычки. Попробуйте изменить словарь fake_dict и посмотрите, что из этого получится.

# Для десериализации нужно использовать функцию loads. Ее аргумент — это строка с данными в формате json.

# Запустите программу, попробуйте изменить данные в json_data.

# import json

# json_data = '{"key_1": 1, "key_2": "any string"}'
# fake_dict = json.loads(json_data)
# print(type(fake_dict), fake_dict)

# Можно даже специально сделать ошибку в json_data. Например, вставить запятую после двоеточия. Модуль json не сможет правильно прочитать такую строку и программа завершится с ошибкой.