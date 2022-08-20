t = int(input('температура'))
if t < -4:
    print('морозно')
elif t < 0 and t >= -4:
    print('холодно')
elif t >= 0 and t < 12:
    print('Прохладно')
elif t >= 12 and t < 27:
    print('Тепло')
else:
    print('жарко')