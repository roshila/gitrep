# Кортеж — это неизменяемый список. Все операции и методы, которые работают со списками, но не изменяют его, работают и с кортежами. Например, метод index есть как у списков, так и у кортежей. А метода append, который добавляет элементы списка, у кортежа нет.

# Разумеется, вместо кортежа всегда можно использовать список. Но иногда бывает необходима «защита от дурака» — то есть, чтобы какой‑то список никогда не менялся случайно или намерено. Да и памяти внутри компьютера кортеж занимает меньше. В общем, бывают случаи, когда кортежи действительно нужны.

# Кортеж обозначается с помощью запятых. Если в кортеже всего один элемент, после него нужно ставить запятую. Здесь переменные a, b и c будут кортежами, а d — строкой.
# a = (1, 2, 3)
# b = 1, 2, 3
# c = ("s", )
# d = ("s")
# Круглые скобки не обязательны, но лучше их все же ставить. Тем более, что бывают случаи, когда скобки все‑таки нужны. В первом print — это три параметра: 1, 2 и 3. А во втором — это один параметр — кортеж из трех элементов.

# print(1, 2, 3)
# print((1, 2, 3))