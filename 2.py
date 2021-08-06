
list_1 = [(input('Введите элементы списка: ')) for i in range(int(input('Введите кол-во элементов списка: ')))]

for elements in range(1, len(list_1), 2):
    elem_1 = list_1.pop(elements)
    list_1.insert(elements-1, elem_1)


print(list_1)