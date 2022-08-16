# abs(x) возвращает абсолютную величину (модуль числа)
# all(iterable) проверяет все ли указанные элементы принимают значение "истина"
# all(Iterable)  -> bool
# iterable это обьект, поддерживающий интегрирование
# он вернёт true, если все элементы интегрированное обьекта представляются истинной (True)
all([True, True, True]) # True
all([True, True, False]) #False
#
all([1, 2, 3]) #True
all([1, 2, 0]) #False
 # https://letpy.com/handbook/builtins/#abs