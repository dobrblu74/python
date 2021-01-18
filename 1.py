import time


class TrafficLight:
    _color = ['красный', 'желтый', 'зеленый']

    def running(self):
        while True:
            print(f'Горит {self._color[0]}')
            time.sleep(7)
            print(f'Горит {self._color[1]}')
            time.sleep(2)
            print(f'Горит {self._color[2]}')
            time.sleep(5)


traffic = TrafficLight()
traffic.running()
