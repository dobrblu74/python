while True:
    num_1 = int(input('Введите положительное число: '))
    num_2 = int(input('Введите целое отрицательно число: '))
    if num_1 >= 0 and (num_2 < 0):
        break
    else:
        print('Введите положительное число и целое отрицательно число!')


def my_func_1(x, y):
    return 1 / x ** abs(y)


print(my_func_1(5, -6))


def my_func_2(x, y):
    i = 1
    while i < abs(y):
        x *= x
        i += 1
    return 1 / x


print(f'{num_1} в степени {num_2} будет {my_func_1(num_1, num_2)}')
print(f'{num_1} в степени {num_2} будет {my_func_2(num_1, num_2)}')
