class myword():
    def getInput(self):
        l = input("write few comma seperated words : ").split(",")
        l.sort(reverse = True)
        asendsort = sorted(l)
        print(','.join(l))
        print(','.join(asendsort))

#    def getOutput(self):

mw = myword()
mw.getInput()
#mw.getOutput()