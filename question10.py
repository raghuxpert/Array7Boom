class arrayWithSpce():
    def __init__(self):
        self.input = []

    def getInput(self):
        self.input = input("write few words (including duplicate) with spaces : ").split(" ")
        print(self.input)

    def printOutput(self):
        #print(" ".join(list(set(self.input)).sort()))
        #print(list(set(self.input)).sort())
        print(" ".join(sorted(list(set(self.input)))))
        #a = list(set(self.input))
        #a.sort()
        #print(a)

aws = arrayWithSpce()
aws.getInput()
aws.printOutput()

