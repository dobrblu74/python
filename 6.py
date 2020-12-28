def func_1(text):
    return text.title()


print(func_1('hello world'))


def func_2(text):
    words = text.split(' ')
    words_list = []
    for i in words:
        str_element = str(i)
        first_letter = str_element[:1].upper()
        word = first_letter + str_element[1:]
        words_list.append(word)
    return ' '.join(words_list)


print(func_2("hello world"))
