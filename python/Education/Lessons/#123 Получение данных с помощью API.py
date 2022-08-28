# Парсинг исходного кода страниц дело хорошее. Но если нужно найти что‑то сложнее, чем случайное число, парсинг становится тоже не очень простым. Нужно найти закономерности в исходном коде страницы, найти, за что можно зацепиться, что можно взять за основу поиска. В конце концов, владельцы сайта могут поменять дизайн, HTML код изменится и все придется анализировать и переписывать заново. Например, посмотрите на исходный код вот этойhttps://www.imdb.com/страницы.
# Добыть нужную информацию из такого исходного кода кажется не такой простой задачей.

# К счастью, многие сайты и сервисы предоставляют API для работы с данными. Дословно API — это программный интерфейс приложения. В общем и целом — это способ взаимодействия разных программ между собой. В прошлом уроке, например, написанная вами программа взаимодействовала с программой, написанной нами.

# Описание способов взаимодействия обычно публикуются на сайтах, которые предоставляют возможность взаимодействия.

#  Вот, например, описание реального API для получения курсов валют.
#  https://www.exchangerate-api.com/docs/free

#  Из документации мы узнаем, что по адресу ниже можно получить курс доллара США

#  https://open.er-api.com/v6/latest/USD

#  Текст, который вы увидите, когда перейдете по ссылке, должен вам кое‑что напомнить. Это данные в формате json, о котором было рассказано в разделе про файлы. То есть, используя модуль json мы можем преобразовать данные, полученные по API в переменную Python!


# import requests
# import json

# result = requests.get('https://open.er-api.com/v6/latest/USD')
# data = json.loads(result.text)
# print(data)

# В получившемся словаре слишком много ключей. Из‑за этого трудно понять, что за данные мы получили. Чтобы было проще прочитать то, что нам пришло от API, можно использовать модуль pprint из стандартной библиотеки Python.
# import requests
# import json
# # импортируем 
# import pprint

# # и настраиваем PrettyPrinter
# pp = pprint.PrettyPrinter(indent=4)  # indent=4 -- значит отступ в 4 пробела

# result = requests.get('https://open.er-api.com/v6/latest/USD')
# data = json.loads(result.text)

# pp.pprint(data)  # "красиво" выводим на экран данные

# Помимо свойства text у ответа есть и метод json который автоматически попытается преобразовать текст ответа. То есть, вполне можно сделать вот так

# import requests

# result = requests.get('https://open.er-api.com/v6/latest/USD')

# # нет необходимости импортировать модуль json отдельно, 
# # все нужное есть в модуле requests
# data = result.json()
# print(data["rates"]['EUR'])

# Есть огромное множество таких API у разных сайтов и для различных целей. Так можно получить информации о погоде, авиарейсах, о результатах футбольных матчей и многое другое. К каждому такому API есть документация и разбираться с каждым API придется индивидуально. Мы составили таблицу из нескольких интересных на наш взгляд API, чтобы вы смогли немного потренироваться. Если, конечно, хотите.

# https://agify.io	Предсказание возраста по имени
# https://www.boredapi.com/documentation	Для тех, кому скучно
# https://genderize.io	Предсказание пола по имени
# http://numbersapi.com/	Интересные факты о числах