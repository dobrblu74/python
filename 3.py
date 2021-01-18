class Worker:
    def __init__(self, name, surname, position, wage=0, bonus=0):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):

    def get_full_name(self):
        return print(self.name, self.surname)

    def get_total_income(self):
        return print(sum(self._income.values()))


position_1 = Position('Sergei', 'Ivanov', 'IT', 30000, 5000)

position_1.get_full_name()
position_1.get_total_income()
