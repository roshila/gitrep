password = input('Введите пароль')
if len(password)<= 5: #если количество символов меньше или равно 5 то условие истиннно
    print('Слишком короткий пароль')

name = input('Введите имя')
if name == 'Рома':
    print('Такое имя уже занято')
