class Road:
    def __init__(self, _length, _width):
        self._length = _length
        self._width = _width

    def calc_mass(self, mass_one=0.25, thickness=5):
        result = self._length * self._width * thickness * mass_one
        return f'Масса дорожного покрытия составит:{result} т.'


road = Road(5000.50, 20)
print(road.calc_mass())
