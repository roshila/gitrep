# Кроме начала и конца, в срезе можно задать шаг. 
# Следующая программа выведет на экран каждый второй символ исходной строки.
foo = "Привет, мир!"
print(foo[::2])
# В этом примере мы не указываем начало и конец среза и берём каждый второй символ исходной строки целиком.
# Если же указать в качестве начала второй символ
foo = "Привет, мир!"
print(foo[1::2])
# то результатом будет каждый второй символ, начиная со второго
# Если указать отрицательный шаг, символы будут идти в обратном порядке. Вот так, например, можно перевернуть исходную строку
foo = "Привет, мир!"
print(foo[::-1])
# Проверка
# В этом уроке вам надо будет написать программу, которая определяет, является ли введённый пользователем текст палиндромом.
# Палиндром — это слово или предложение, которое одинаково читается слева направо и справа налево. Такие слова или предложения еще называют перевертышами.
# Четких указаний для выполнения в этом уроке не будет — придумать решение вы должны самостоятельно. Единственное, чего нет в предыдущих уроках, 
# но понадобится для решения — описание метода строк replace, который заменяет символы, переданные первым аргументом, на символы, переданные вторым аргументом.
# Эта программа, например, заменит все символы пробела в строке string на пустые строки
string = "А роза упала на лапу Азора"
string = string.replace(" ", "")
print(string)
# и выведет на экран следующий текст
#АрозаупаланалапуАзора
# Стоит запомнить, что пробел " " — это такой же символ, как и все остальные, а пустая строка "" — это не символ, а отсутствие каких‑либо символов.
# Это задание может потребовать больше времени на выполнение, чем обычно. Не переживайте, если что‑то не получается,
# лучше попробуйте вывести введённую и перевернутую строку функцией print и сравнить их. Это поможет понять, что именно пошло не так.
# Программа должна вывести на экран «да», если введённый текст — палиндром и «нет» — если нет.
string = input("введите текст:")
string=string.replace(" ","")
string=string.upper()
if string == string[::-1]:
    print("да")
else:
    print("нет")