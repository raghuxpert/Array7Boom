class MyString:
    def __init__(self):
        print("init executed")
        self.s = ""

    def getString(self):
        self.s = str(input("insert string data"))

    def printString(self):
        print(self.s.upper())


mys = MyString()
mys.getString()
mys.printString()

