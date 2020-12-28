def profile(name, surname, year, city, email, phone):
    """
    Returning a dictionary of parameters and values
    :param name: parameter name str
    :param surname: last name parameter str
    :param year: date of birth parameter int
    :param city: parameter city of birth str
    :param email: parameter email str
    :param phone: parameter phone number
    :return: dictionary of parameters and values specified in the function
    """
    print(
        f'Имя - {name}, фамилия - {surname}, год рождения - {year}, город - {city}, email - {email}, телефон - {phone}')


profile(name='Sergei', surname='Danilov', year=1994, city='Moscow', email='dobrblu74@mail.ru', phone=89774359876)
