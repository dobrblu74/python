class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Метод отрисовки.')


class Pen(Stationery):

    def draw(self):
        print('Отрисовка ручкой.')


class Pencil(Stationery):

    def draw(self):
        print('Отрисовка карандашом.')


class Handle(Stationery):

    def draw(self):
        print('Отрисовка маркером.')


pen = Pen('ручка')
pen.draw()
pencil = Pencil('карандаш')
pencil.draw()
handle = Handle('маркер')
handle.draw()
