def wages(file):
    """Фильтр сотрудников по окладу и подсчет средней велечины дохода"""
    with open(file, encoding='utf-8') as f:
        sal_list = []
        workers = {}
        for i in f:
            key, value = i.split()
            workers[key] = value
            if float(value) < 20000.00:
                print(f'{key} - зарплата меньше 20000')
        sal = workers.pop(key)
        sal_list.append(sal)
        result = round(sum(map(float, sal_list)) / len(sal_list), 2)
        print(f'Средняя величина дохода сотрудников составляет {result}')


filename = 'task_3.TXT'
wages(filename)
