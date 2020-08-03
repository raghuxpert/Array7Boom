import numpy as np

class my2Darray():
    def __init__(self):
        self.x = 0
        self.y = 0

    def getInput(self):
        a = input("insert value of x,y : " ).split(",")
        self.x = int(a[0])
        self.y = int(a[1])

    def printOutput(self):
        #out = np.ones((self.x, self.y))
        out = [[0 for i in range(self.y)] for j in range(self.x)]
        for k in range(self.x):
            for l in range(self.y):
                out[k][l] = k*l
        print(out)

ma = my2Darray()
ma.getInput()
ma.printOutput()