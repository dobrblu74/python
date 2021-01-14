import json


def calc_prof_aver(file):
    """Делаем аналитику по компаниям, считаем среднюю прибль"""
    profit_dict = {}
    prof = 0
    prof_aver = 0
    i = 0
    with open(file, encoding='utf-8') as f:
        for line in f:
            name, form, revenue, costs = line.split()
            profit_dict[name] = int(revenue) - int(costs)
            if profit_dict.setdefault(name) > 0:
                prof = prof + profit_dict.setdefault(name)
                i += 1
        if i > 0:
            prof_aver = prof / i
        else:
            print('Средняя прибыль отстуствует. Все фирмы работают в убыток.')
        pr = {'средняя прибыль': round(prof_aver)}
        profit_dict.update(pr)
        return profit_dict


def record_json(file, some_text):
    with open(file, "w", encoding='utf-8') as file_js:
        json.dump(some_text, file_js)


filename = 'task_7.TXT'
date = calc_prof_aver(filename)

filename_json = 'task_7.json'
record_json(filename_json, date)

print(f'Данные записаны в файл - {filename_json}\n'
      f'Содержимое файла: {calc_prof_aver(filename)}')

# with open(filename_json) as f_j:
#     date = json.load(f_j)
#     print(date)
