class Car:
    direction_car = 'прямо'

    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self, speed):
        self.speed = speed

    def stop(self):
        self.speed = 0

    def turn(self, direction):
        self.direction_car = direction

    def show_speed(self):
        print(self.speed)


class TownCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)

    def show_speed(self):
        if self.speed > 60:
            print('Превышение скорости')
        else:
            print(self.speed)


class SportCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)


class WorkCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)

    def show_speed(self):
        if self.speed > 40:
            print('Превышение скорости')
        else:
            print(self.speed)


class PoliceCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, True)


town_car = TownCar(65, 'black', 'name1')
print(town_car.name)
town_car.show_speed()
town_car.go(40)
town_car.show_speed()
town_car.turn('лево')
print(town_car.direction_car)
print(town_car.is_police)

sport_car = SportCar(100, 'yellow', 'name2')
print(sport_car.name)
sport_car.show_speed()
print(sport_car.direction_car)
print(sport_car.is_police)

work_car = WorkCar(55, 'white', 'name3')
print(work_car.name)
work_car.show_speed()
work_car.go(40)
work_car.show_speed()

police_car = PoliceCar(58, 'grey', 'name4')
print(police_car.name)
police_car.show_speed()
print(police_car.direction_car)
print(police_car.is_police)
