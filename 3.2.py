month = int(input('Введите номер месяца - '))
month_py = month - 1
if 0 < month < 13:
    season = ['winter', 'winter', 'spring', 'spring','spring', 'summer', 'summer', 'summer', 'autumn', 'autumn', 'autumn', 'winter']
    print(season[month_py])
else:
    print('error')