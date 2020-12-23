products = []
number = 1
while input('Вы хотите добавить новый товар в структуру данных "Товары"? Введите "да" или "нет": ') == 'да':
    parameters = {}
    pass
    parameters['название'] = input('Введите название товара: ')
    parameters['цена'] = input('Введите стоимость товара: ')
    parameters['количество'] = input('Введите количество товара: ')
    parameters['единица'] = input('Введите единицу учета товара: ')
    products.append(tuple([number, parameters]))
    number += 1
    parameters_key = parameters.keys()
    parameters_val = parameters.values()
print(products)
analytics = {}
for product in products:
    for parameters_key, parameters_val in product[1].items():
        if parameters_key in analytics:
            analytics[parameters_key].append(parameters_val)
        else:
            analytics[parameters_key] = [parameters_val]
print(analytics)
