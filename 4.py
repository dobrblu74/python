filename = 'task_4.TXT'
new_file = []
rus_num = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
with open(filename, encoding='utf-8') as f:
    for line in f:
        line = line.split(' ', 1)
        new_file.append(rus_num[line[0]] + ' ' + line[1])

filename_new = 'task_4_new.TXT'
with open(filename_new, 'w') as f_2:
    f_2.writelines(new_file)
    print(new_file)
