class Racer:
    def drive(self):
        print('f')

class Car:
    def drive(self):
        print('dri')

class RacingCar(Car, Racer):
    pass

car = RacingCar()
car.drive()























