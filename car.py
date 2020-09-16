# /usr/bin/python3
# coding=utf-8

class Car():
    '''汽车类'''

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0  # 给某一属性指定默认值

    def get_desc_name(self):
        long_name = (str(self.year) + " " + self.make + ' ' + self.model)
        return long_name.title()

    def read_odometer(self):
        print("This car has " + str(self.odometer_reading) + " miles on it")

    def update_odometer(self, mile):
        if mile >= self.odometer_reading:
            self.odometer_reading = mile
        else:
            print('禁止将公里数回滚')

    def increment_odometer(self, miles):
        self.odometer_reading += miles


my_car = Car('jili', 'binrui', '2020')

print(my_car.make)
print(my_car.model)
print(my_car.year)
'''三种修改属性方法'''
# 直接修改
my_car.odometer_reading = 10000
my_car.read_odometer()
# 通过类方法修改
my_car.update_odometer(10000)
my_car.read_odometer()
# 通过方法对属性的值进行递增
my_car.increment_odometer(100)
my_car.read_odometer()
