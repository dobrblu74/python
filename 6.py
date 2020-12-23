products = []
number = 1
while input('Вы хотите добавить новый товар в структуру данных "Товары"? Введите "да" или "нет": ') == 'да':
    parameters = {}
    while input(f'Вы хотите добавить новый параметр товара - {number}? Введите "да" или "нет": ') == 'да':
        print('Возможные варианты ввода параметров: название, цена, количество, ед')
        parameters_key = input(f'Введите новый параметр товара - {number}: ')
        parameters_val = input('Введите характеристики в соответствии с выбранным ранее параметром: ')
        parameters[parameters_key] = parameters_val
    products.append(tuple([number, parameters]))
    number += 1
print(products)
analytics = {}
for product in products:
    for parameters_key, parameters_val in product[1].items():
        if parameters_key in analytics:
            analytics[parameters_key].append(parameters_val)
        else:
            analytics[parameters_key] = [parameters_val]
print(analytics)
