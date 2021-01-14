def number_rows(file):
    """Подсчет количества строк в файле"""
    try:
        with open(file, encoding='utf-8') as f:
            file_list = f.readlines()
    except FileNotFoundError:
        print(f'К сожалению файла с названием {file} не найдено.')
    else:
        print(f'Количество строк в файле - {len(file_list)}')


def number_words(file):
    """Подсчет количества слов в строке"""
    try:
        with open(file, encoding='utf-8') as f:
            contents = f.readlines()
    except FileNotFoundError:
        print(f'К сожалению файла с названием {file} не найдено.')
    else:
        for line in contents:
            print(f'В строке "{line}" количество слов - {len(line.split())}')


filename = 'task_2.TXT'
number_rows(filename)

number_words(filename)
