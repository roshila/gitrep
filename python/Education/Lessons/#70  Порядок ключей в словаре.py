# Начиная с Python 3.6, ключи словаря перебираются в том порядке, в котором они были созданы. То есть, если вы создадите словарь и сделаете цикл по его ключам, их очередность сохранится
# foo = {"test": 1, "test_second": 1, 2: 1}
# for k, v in foo.items():
#     print(k, v)
    

# Это поведение, однако, может отличаться в более ранних версиях Python.

# В Python 2.7, например, словари неупорядоченны, то есть создав и перебрав словарь

# foo = {'color': 'red', 'foo_key': 2, 1: 'no'}
# for k, v in foo.items():
#     print k, v 

# вы получите такой результат

# color red
# 1 no
# foo_key 2
# Обратите внимание на порядок последнего и предпоследнего ключа.

# Об этой особенности словарей стоит помнить, если вы пишите программы на Python 3.5 или ниже.