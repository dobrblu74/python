class Car:

    def __init__(self, name, color, base_speed, max_speed, is_police):
        self.name = name
        self.color = color
        self.speed = 0
        self.base_speed = base_speed
        self.max_speed = max_speed
        self.is_police = is_police

    def go(self):
        if self.speed == 0:
            self.speed = self.base_speed
            print(f'{self.name} начал движение со скоростью {self.speed}!')
        else:
            print(f'{self.name} продолжает движение со скоростью {self.speed}!')

    def stop(self):
        if self.speed:
            print(f'{self.name} остановился.')
            self.speed = 0
        else:
            print(f'{self.name} продолжает стоять.')

    def turn(self):
        print('right - повернуть направо\n'
              'left - повернуть налево\n'
              'u-turn - развернуться')
        direction = input('Введите направление куда необходимо повернуть машине: ')
        try:
            if self.speed == 0:
                print(f'{self.name} не может повернуть, так как сейчас стоит.')
            elif direction == 'right':
                print(f'{self.name} поворачивает направо.')
            elif direction == 'left':
                print(f'{self.name} поворачивает налево.')
            elif direction == 'u-turn':
                print(f'{self.name} развернулась.')
        except ValueError:
            print('Введите одну из доступных комманд:\n'
                  'right - повернуть направо\n'
                  'left - повернуть налево\n'
                  'u-turn - развернуться')

    def show_speed(self):
        print(f'Скорость {self.name} {self.speed}')

    def speed_up(self):
        acceleration = input(
            f'Максимально возможное увеличение скорости -  {(self.max_speed - self.speed)}\n'
            'Введите значение на которое увеличиться текущая скорость: ')
        if self.speed == self.max_speed:
            print(f'Набрана максимальная скорость - {self.max_speed}')
        else:
            if self.speed + int(acceleration) > self.max_speed:
                print('Привышение максимально возможной скорости!')
            else:
                self.speed = self.speed + int(acceleration)
                print(f'Скорость движения машины стала {self.speed}')

    def speed_reduction(self):
        deceleration = input('Введите значение на которое уменьшиться текущая скорость: ')
        if self.speed == 0:
            print('Машина уже стоит.')
        elif self.speed - int(deceleration) <= 0:
            print('Машина остановилась.')
        else:
            self.speed = self.speed - int(deceleration)
            print(f'Машина снизила скорость на {deceleration}, текущая скорость {self.speed}')


class TownCar(Car):
    def __init__(self, name, color, base_speed=40, max_speed=70, is_police=False):
        super().__init__(name, color, base_speed, max_speed, is_police)

    def show_speed(self):
        print(f'Скорость {self.name} {self.speed}')
        if self.speed >= 60:
            print('Превышение скорости!')


class SportCar(Car):
    def __init__(self, name, color, base_speed=80, max_speed=120, is_police=False):
        super().__init__(name, color, base_speed, max_speed, is_police)


class WorkCar(Car):
    def __init__(self, name, color, base_speed=20, max_speed=50, is_police=False):
        super().__init__(name, color, base_speed, max_speed, is_police)

    def show_speed(self):
        print(f'Скорость {self.name} {self.speed}')
        if self.speed >= 40:
            print('Превышение скорости!')


class PoliceCar(Car):
    def __init__(self, name, color, base_speed=60, max_speed=100, is_police=True):
        super().__init__(name, color, base_speed, max_speed, is_police)


towncar = TownCar('towncar', 'green')

towncar.show_speed()
towncar.speed_up()
towncar.show_speed()
towncar.turn()
towncar.stop()
