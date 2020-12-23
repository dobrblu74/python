my_list = [7, 5, 3, 3, 2]
number = int(input('Введите число которое мы добавим в список: '))
q = my_list.count(number)
for el in my_list:
    if q > 0:
        i = my_list.index(number)
        my_list.insert(q + i, number)
        break
    else:
        if number > el:
            i = my_list.index(el)
            my_list.insert(i, number)
            break
        elif number < my_list[len(my_list) - 1]:
            my_list.append(number)
print(my_list)
