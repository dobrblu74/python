my_list_1 = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
new_list_1 = [number for i, number in enumerate(my_list_1) if i > 0 and my_list_1[i] > my_list_1[i - 1]]
print(new_list_1)

my_list_2 = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
new_list_2 = [el for el in my_list_2 if my_list_2.index(el) > 0 and el > my_list_2[my_list_2.index(el) - 1]]
print(new_list_2)
