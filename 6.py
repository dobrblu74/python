def counting_lessons(file):
    """Подсчет количества занятий по каждому предмету"""
    my_dict = {}
    with open(file, encoding='utf-8') as f:
        lines = f.readlines()
        for line in lines:
            date = line.replace('(', ' ').split()
            my_dict[date[0][:-1]] = sum(int(i) for i in date if i.isdigit())
        return my_dict


filename = 'task_6.TXT'
print(counting_lessons(filename))
