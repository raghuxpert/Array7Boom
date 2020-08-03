# using property class
class Celsius:
    def __init__(self, temp=0, press=0):
        # print("self in init : ", self)
        self.temp = temp
        self.press = press
        # self.force = force

    def to_fahrenheit(self):
        # print("self in to_fahrenheit : ", self)
        return (self.temperature * 1.8) + 32

    @property
    def temp(self):
        print("inside temp getter")
        return self._temp

    @temp.setter
    def temp(self, value):
        print("inside temp setter")
        if value < -273.15:
            raise ValueError("Temperature below -273.15 is not possible")
        self._temp = value

    @property
    def press(self):
        print("inside press getter")
        return self._press

    @press.setter
    def press(self, value):
        print("inside press setter")
        self._press = value

    @property
    def force(self):
        print("inside force getter")
        return self._temp + self._press

    @force.setter
    def force(self, value):
        print("inside force setter")
        self._temp = value/2
        self._press = value/2

c = Celsius(1,4)
print(c.temp, c.press, c.force)

c.temp = 3
print(c.temp, c.press, c.force)

c.force = 6
print(c.temp, c.press, c.force)