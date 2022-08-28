
# Для работы с HTTP запросами в Питоне есть отдельный модуль requests. У этого модуля много возможностей, он постоянно дорабатывается и развивается. Полная документация и руководство по установке этого модуля находятся здесь.

# Для того чтобы вы могли попробовать работать с HTTP запросами, мы разработали свой модуль requests. Его функционал аналогичен настоящему requests. То есть все, что вы напишете с нашим модулем, будет работать и с настоящим модулем requests.

# Чтобы использовать возможности модуля в своей программе, его нужно импортировать, а для отправки HTTP запроса и получения ответа использовать функцию get. Аргументом в эту функцию нужно передать адрес, по которому необходимо сделать запрос. Результатом работы этой функции будет ответ от сервера в виде Python-объекта. В модуле requests есть и другие функции для отправки запросов, но о них немного позже.

# Попробуйте запустить вот такую программу

# import requests
# result = requests.get('https://letpy.com/simple-html-example/')
# print(result.text)

# Текст, который программа выведет на экран, — это исходный код страницы-примера с нашего сайта. Попробуйте передать функции get любой другой адрес. Чувствуете всю важность таких возможностей?