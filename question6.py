import math as mt

class formula():
    def __init__(self):
        self.C = 50
        self.H = 30
        self.input = []
        self.output = []

    def getInput(self):
        self.input = str(input("insert values comma sepearted")).split(",")
        self.input = list(map(int, self.input))

    def giveOutput(self):
        for i in self.input:
            self.output.append(str(round(mt.sqrt(2*self.C*i/self.H))))
        print(','.join(self.output))

f = formula()
f.getInput()
f.giveOutput()