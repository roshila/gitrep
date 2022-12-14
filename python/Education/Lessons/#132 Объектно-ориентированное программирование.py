# До этого урока код в наших программах состоял из блоков, выражений и максимум, как мы организовывали его, это писали функции. Такой подход к программированию называется процедурно-ориентированным. В этом подходе нет ничего плохого и его вполне можно использовать. Однако, когда сложность и объем программы растет, становится трудно удержать все детали в голове.

# Собственно, чтобы улучшить организацию и восприятие кода, был придуман объектно-ориентированный подход к программированию.

# Основополагающие понятия объектно-ориентированного программирования — это класс и объект. Когда программист создает класс, он по сути создает свой собственный тип данных. А вот объект — это конкретный экземпляр класса.

# Чтобы лучше разобраться в этом, приведу пример с уже знакомым вам встроенным типом данных

# string = "Любая строка"
# print(type(string))
# В этой программе переменная string — это объект класса str
# <class 'str'>
# Создать класс можно с помощью ключевого слова class
# class ExampleClass:
#     pass

# То есть, мы пишем ключевое слово class, название класса и двоеточие. Как и при создании функции, тело класса мы пишем с отступом. Про то, что может быть телом класса вы узнаете в следующем уроке. Пока оставим его пустым и в этом нам поможет оператор pass.

# Обратите внимание на то, как написано название класса. Такой стиль именования называется CamelCase и именно этот стиль предпочтителен для названий классов. CamelCase переводится с английского как ВерблюжийРегистр. Слова при таком стиле пишутся без пробелов, каждое слово с заглавной буквы. Эти заглавные буквы напоминают горбы верблюда. Отсюда и такое название.