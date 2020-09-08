class Car():
    '''汽车类'''

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        print("This car has " + str(self.odometer_reading) + ' miles on it' + '\n')

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer")

    def increment_odometer(self, miles):
        self.odometer_reading += miles


my_car = Car('jili', 'binrui', '2019')

print(my_car.make)
print(my_car.model)
print(my_car.year)
# 直接修改属性的值
my_car.odometer_reading = 10000
print(my_car.get_descriptive_name())
my_car.read_odometer()
# 通过类方法修改属性的中
my_car.update_odometer(10000)
my_car.read_odometer()
# 通过方法对属性的值进行递增
my_car.increment_odometer(888)
my_car.read_odometer()

