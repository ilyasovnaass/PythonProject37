class car:
    def __init__(self, wheels, color, marka):
        self.wheels = wheels
        self.color = color
        self.marka = marka

    def change_color(self, new_color = 'pink'):
        self.color = new_color


my_car = car(4, 'red', 'blue')
my_car2 = car(4, 'green', 'yellow')
print(my_car.wheels)

