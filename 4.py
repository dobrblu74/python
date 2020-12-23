user = input('Ввведите несколько слов через пробел: ')
user_split = user.split(' ')
for i, el in enumerate(user_split, 1):
    if len(el) > 10:
        el = el[0:10]
    print(f'{i}) - {el}')
