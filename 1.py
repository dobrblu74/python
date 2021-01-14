def write_text(file):
    """Запись строк в файл"""
    with open(file, 'w') as f:
        while True:
            line = f.write(input('Введите текст: '))
            if not line or line == '\n':
                break


filename = 'task_1.txt'
write_text(filename)
