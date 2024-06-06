# def add(*args):
#     c = 0
#     for n in args:
#         c += n
#     print(type(args))
#     return c
#
#
# print(add(1, 9, 5, 6))
#
#
# def calculate(**kwargs):
#     print(kwargs)
#     print(type(kwargs))
#     for key, value in kwargs.items():
#         print(key)
#         print(value)
#
#
# calculate(add=3, multiply=5)

class Car:

    def __init__(self, **kwargs):
        self.make = kwargs.get("make")  # better than kwargs["make"]
        self.model = kwargs.get("model")


my_car = Car(make="vw", model="golf")
print(my_car.make, my_car.model)