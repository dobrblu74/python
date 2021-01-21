class Matrix:
    def __init__(self, date):
        self.date = date

    def __str__(self):
        for row in self.date:
            for i in row:
                print(f'{i:4}', end="")
            print()
        return ''

    def __add__(self, other):
        if len(self.date) == len(other.date):
            for i in range(len(self.date)):
                for i_2 in range(len(other.date[i])):
                    self.date[i][i_2] = self.date[i][i_2] + other.date[i][i_2]
            return Matrix.__str__(self)
        else:
            return 'Матрицы разных размеров!'


m_1 = Matrix([[4, 5, 6], [-3, -2, -1], [8, 3, 4], [-5, -1, 6], [0, 1, 0], [4, -4, 1]])
m_2 = Matrix([[5, 1, -3], [-1, 2, -6], [1, 5, 3], [-1, 1, -4], [1, -1, 4], [-4, -5, 3]])
print(m_1 + m_2)
