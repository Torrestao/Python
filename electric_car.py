'''
一个类继承另一个类时，它将自动获得另一个类的所有属性和方法，原有的类称为父类，而新类称为子类。
子类继承了其父类的所有属性和方法，同时还可以定义自己的属性和方法
'''

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

class Battery():
    def __init__(self,battery_size=70):
        self.battery_size = battery_size

    def describe_battery(self):
        print("This car has a " + str(self.battery_size) + '-kWh battery.')

class ElectricCar(Car):
    '''电动汽车类，继承汽车类的共有属性'''
    def __init__(self,make,model,year):
        super().__init__(make,model,year)
        self.battery = Battery()  #将Battery实例当做ElectricCar类的一个属性 

my_tesla = ElectricCar('tesla','model s', 2016)

print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()

    


