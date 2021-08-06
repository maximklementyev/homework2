string = input('Введите несколько слов - ').split()
# for i in range(len(string)):
#     print(i+1, string[i], end = '\n')

for ind, el in enumerate(string):
    print(ind, el[:10])