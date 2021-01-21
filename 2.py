from abc import ABC, abstractmethod


class Clothes(ABC):
    @property
    @abstractmethod
    def expenditure(self):
        pass

    @property
    @abstractmethod
    def name(self):
        pass

    def __str__(self):
        return f"{self.name} - {round(self.expenditure, 2)} п.м. ткани"


class Coat(Clothes):
    def __init__(self, size: float):
        self.size = size

    @property
    def expenditure(self):
        return self.size / 6.5 + 0.5

    @property
    def name(self):
        return 'Пальто'


class Costume(Clothes):
    def __init__(self, height: float):
        self.height = height

    @property
    def expenditure(self):
        return 2 * self.height + 0.3

    @property
    def name(self):
        return 'Костюм'


coat = Coat(52)
costume = Costume(1.73)
my_list = [coat, costume]
print(costume)
print(coat.expenditure)


def count_all_cloth():
    print(f'Общее количество необходимой ткани - {sum(el.expenditure for el in my_list)} п.м.')


count_all_cloth()
