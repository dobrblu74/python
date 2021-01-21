class Cell:
    def __init__(self, quantity: int):
        self.quantity = quantity

    def __add__(self, other):
        return f'При сложении клеток получилась новая клетка с размером - {self.quantity + other.quantity}'

    def __sub__(self, other):
        cell = self.quantity - other.quantity
        return f'Клетка уменьшилась, теперь её размер - {cell}' if cell >= 0 else 'Клетки не стало.'

    def __mul__(self, other):
        return self.quantity * other.quantity

    def __truediv__(self, other):
        return self.quantity // other.quantity

    def make_order(self, count):
        result = ''
        for i in range(int(self.quantity / count)):
            result += '*' * count + '\n'
        result += '*' * (self.quantity % count) + '\n'
        return result


cell_1 = Cell(10)
cell_2 = Cell(6)
print(cell_1 + cell_2)
print(cell_1 - cell_2)
print(cell_1 * cell_2)
print(cell_1 / cell_2)
print(cell_1.make_order(6))
