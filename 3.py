def sum_func(num_1, num_2, num_3):
    num_list = [num_1, num_2, num_3]
    num_list.sort(reverse=True)
    return num_list[0] + num_list[1]


print(sum_func('bff', 'aa', 'zz'))
