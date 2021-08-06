goods = []
features = {'name': '', 'price': '', 'number': '', 'ei': '', 'машина': ''}
analytics = {'name': [], 'price': [], 'number': [], 'ei': [], 'машина': []}
n = 0
while True:
    if input().upper() == 'esc':
        break
    for i in features.keys():
        property = input('Введите значение свойства - ')
        features[i] = int(property) if (i == 'price' or i == 'number') else property
        analytics[i].append(features[i])
    goods.append((number, features.copy()))
    print(f'\nСтруктура товаров\n{goods}')
    print(f"\nАналитика по товарам\n{'*' * 30}")
    for key, value in analytics.items():
        print(f'{key[:25]:>30}: {value}')
    print('*' * 30)

# это задание скопировал, признаюсь, но остальные сделал своими силами =)