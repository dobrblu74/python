a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))


def division(var_1, var_2):
    """ Return result var_1|var_2

    :param var_1: dividend (number)
    :param var_2: divider (number)
    :return: result var_1|var_2 (number)

    Handling the division by 0 situation
    """
    try:
        result = var_1 / var_2
        return result
    except ZeroDivisionError:
        print('Деление на ноль. Пожалуйста введите положительные числа!')


print(f'Результат деления число {a} на число {b} будет {division(a, b)}')
