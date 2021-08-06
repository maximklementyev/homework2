my_list = [7, 5, 3, 3, 2]
rating = int(input('Введите новый элемент рейтинга - '))
n = 0
for i in my_list:
    if i >= rating:
        n += 1
    else:
        break
my_list.insert(n, rating)
print(my_list)