def sum_numbers():
    result = 0
    while True:
        numbers = input('Введите несколько чисел через пробел, либо введите # чтобы выйти из программы: ').split()
        for i in numbers:
            try:
                if i == '#':
                    print(f'Сумма введённых чисел равна {result}. Выход из программы.')
                    return
                else:
                    result += int(i)
            except ValueError:
                print('Необходимо ввести число или #.')
        print(f'Сумма введённых чисел равна {result}')


print(sum_numbers())
