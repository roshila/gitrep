# Так как каждая страница в Веб — это просто текст, мы можем довольно просто получать и анализировать любую доступную информацию. С помощью программ на Python и модуля requests можно, например, получить курсы валют с сайта банка или информацию о скидках на товары с сайта магазина. В мире, где все есть в интернете, вы можете «добыть» любую нужную вам информацию. Такую «добычу» данных с сайтов еще называют «парсингом» (от англ. parse).

# Для того, чтобы пройти этот урок, надо написать программу, которая «распарсит» нашу простую, тренировочную страницу https://letpy.com/simple-html-example/

# «Добыть» нужно случайное число, которое отображается на странице. То есть из всего текста страницы нужно оставить только число и вывести его на экран. Для этого можно использовать методы строк, срезы, циклы — в общем все, что вы проходили до этого.
# # 1
# import requests

# result = requests.get('https://letpy.com/simple-html-example/')

# num = '0123456789'
# final = ''

# for i in result.text:
#     if i in num:
#         final += i

# print(final[3:])

# # 2 
# import requests
# result = requests.get('https://letpy.com/simple-html-example/')
# target_str = 'Случайное число: '
# start_index = result.text.find(target_str) + len(target_str)
# number = []
# flag = 0
# for i in range(start_index, len(result.text)):
#     if result.text[i] == '<':
#         flag = 1
#     elif flag == 0 and result.text[i].isdigit():
#         number.append(result.text[i])
#     elif result.text[i] == '>':
#         flag = flag - 1
#     i += 1
# result = ''.join(number)
# print(result)