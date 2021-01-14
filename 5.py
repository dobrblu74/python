def number_sum(file):
    """Записываем введенные пользователем числа в отдельный файл.
    Выводим на экран сумму чисел"""
    try:
        with open(file, 'w') as f:
            line = input('Введите цифры через пробел: ')
            f.writelines(line)
            numbers = line.split()
            print(sum(map(int, numbers)))
    except ValueError:
        print('Вы неправильно ввели цифры.\nНаберите цифры через пробел.')


filename = 'task_5.txt'
number_sum(filename)
