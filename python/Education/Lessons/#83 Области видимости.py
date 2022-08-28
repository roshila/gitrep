# Все переменные, созданные в функции, будут видны только в функции. Если попробовать обратиться к переменной, созданной в функции не внутри этой функции, вы получите ошибку NameError.

# То есть, переменная, созданная внутри функции, находится в локальной области видимости этой функции:

# def f():
#     a = "Локальная переменная"
#     print(a)

# f()

# Такая программа выполнится без ошибок и выведет на экран «Локальная переменная». Если же попробовать сделать вот так:

# def f():
#     a = "Локальная переменная"
#     print(a)

# f()
# print(a)

# программа завершится с ошибкой NameError.

# Если переменной a присвоить значение вне функции, то программа, разумеется, заработает без ошибок, а переменная a будет находиться в глобальной области видимости:

# a = "Глобальная переменная"

# def f():
#     a = "Локальная переменная"
#     print(a)

# f()
# print(a)

# Вывод на экран этой программы будет таким:

# Локальная переменная
# Глобальная переменная

# Обратите внимание, что переменная a внутри функции не переопределяет значение глобальной переменной а. То есть, по сути — это две разных переменных в разных областях видимости, но с одинаковым названием.

# Если внутри функции нет переменной а, но она есть глобально в файле, то при попытке обратиться к переменной a внутри функции, будет использована глобальная переменная:

# a = "Глобальная переменная"

# def f():
#     print(a)

# f()
# print(a)

# Эта программа выведет на экран:

# Глобальная переменная
# Глобальная переменная

# Если попробовать изменить глобальную переменную из функции:

# a = "Глобальная переменная"

# def f():
#     a = a + " с дополнением из функции"
#     print(a)

# print(a)
# f()

# произойдет ошибка UnboundLocalError. Все потому, что если присваивание выполняется в пределах функции, имя становится локальным по отношению к этой функции. В примере выше, создается локальная переменная a и ее же мы пытаемся использовать в конкатенации a + " с дополнением из функции"

# В общем, чтобы изменить глобальную переменную из функции, нужно использовать ключевое слово global. Так мы можем заставить Python изменить не локальную, а глобальную переменную.

# a = "Глобальная переменная"

# def f():
#     global a
#     a = a + " с дополнением из функции"
#     print(a)

# print(a, '(до вызова функции)')
# f()
# print(a, '(после вызова функции)')

# Однако, даже с учетом того, что такая возможность есть, не нужно изменять глобальные переменные внутри функции. Сообщество Python объявило такую практику нежелательной, так как из‑за этого изменение кода становится намного сложнее.

# Попробуйте позапускать эти примеры, чтобы лучше прочувствовать всю эту историю с областями видимости.