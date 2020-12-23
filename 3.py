while True:
    user_answer = int(input('Введите номер месяца: '))
    if 12 >= user_answer >= 1:
        time_of_year_dict = {1: "Зима",
                             2: "Зима",
                             3: "Весна",
                             4: "Весна",
                             5: "Весна",
                             6: "Лето",
                             7: "Лето",
                             8: "Лето",
                             9: "Осень",
                             10: "Осень",
                             11: "Осень",
                             12: "Зима"}
        time_of_year_list = list(time_of_year_dict.values())
        for i, el in enumerate(time_of_year_list):
            if i == user_answer - 1:
                print(f'Месяц с использованием list получился - {time_of_year_list[i]}')
                break
        print(f'Месяц с использованием dict получился - {time_of_year_dict[user_answer]}')
        break
    else:
        print('Необходимо ввести номер месяца от 1 до 12!')
