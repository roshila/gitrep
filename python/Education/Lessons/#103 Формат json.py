# Этот текстовый формат данных создан на основе синтаксиса языка JavaScript (json — JavaScript Object Notation). Из‑за своей простоты, читаемости и компактности, json получил большое распространение, а чтение и запись в этом формате доступно практически во всех языках программирования.

# В отличие от csv, данные в этом формате не просто разделены запятыми, а имеют структуру ключ-значение. Это напоминает словарь Python, но в отличие от словаря, ключи в json могут быть только строками, заключенными в двойные кавычки.


# {
#   "key_1": "value",
#   "key_2": "value 2"
# }


# Значения в json могут быть не только строками. Это могут быть числа, списки значений, а также вложенные объекты

# {
#   "key_1": [1, 2, 3, "value"],
#   "key_2": {
#     "inner_key": "inner value",
#     "inner_key_2": ["a", "b", "c"],
#     "inner_key_n": [
#       {
#         "key_1": "value"
#       } 
#     ]
#   }
# }

# Списки значений, как видно из примера, напоминают списки Python. Они ограничены квадратными скобками, а значения списка пишутся через запятую.

# Вложенность данных может быть бесконечной. То есть, значением ключа может быть список, а элементом этого списка — объект. В примере значение ключа key_2 — объект, в котором есть ключ inner_key_n со значением, которое является списком. Единственный элемент этого списка — снова объект.

# Переносы строк и отступы в этом формате необязательны. Они нужны только для удобства чтения. То есть вот это

# {
#   "key_1": "value",
#   "key_2": "value 2"
# }

# и это

# {"key_1": "value","key_2": "value 2"}

# совершенно одинаковые данные с точки зрения json