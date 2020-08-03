# Define a class with a generator which can iterate the numbers, which are divisible by 7, between a given range 0 and n.

class seven_Generator():
    def __init__(self, range):
        self.range = range

    def seven_Gen(self):
        for i in range(self.range):
            if i%7 == 0:
                yield i

        raise StopIteration

n = int(input("Please provide a positive number : "))
sg = seven_Generator(n)

gen = sg.seven_Gen()
for i in range(n):
    print(next(gen))
