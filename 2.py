my_list = []

while input('Вы хотите добавить новый элемент в список? Пожалуйста введите да или нет: ') == 'да':
    el = input('Введите любой элемент который хотите добавить в список: ')
    my_list.append(el)

print(my_list)

if len(my_list) % 2 == 0:
    i = 0
    while i < len(my_list):
        el = my_list[i]
        my_list[i] = my_list[i + 1]
        my_list[i + 1] = el
        i += 2
else:
    i = 0
    while i < len(my_list) - 1:
        el = my_list[i]
        my_list[i] = my_list[i + 1]
        my_list[i + 1] = el
        i += 2

print(my_list)
