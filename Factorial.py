#############################################################



###############################################################

import math as m

class PowTwo:
    def __init__(self, max=0):
        self.max = max

    def __iter__(self):
        self.n = 0
        return self

    def __next__(self):
        if self.n <= self.max:
            r =  m.pow(self.n,2)
            self.n+=2
            return r
        else:
            raise StopIteration

# create an object
#numbers = list(PowTwo(5))
#print(numbers)


################################################################

#indata = str(input(print("insert data requested")))

#a = map(int, indata.split(","))
#print(id(a))
#print(a)

#b = list(a)
#b = list(a)
#print(id(b))
#print(b)

#print(id(a))
#print(id(b))
#print(b)

##################################################################

def dictionary(n):
    d = dict()
    for i in range(1,n+1):
        d[i] = i**2
    return d

#print(dictionary(5))

#####################################################################

def func(start, end):
    r = end-start
    result = []
    for i in range(r):
        if start%7 == 0 and start%5 != 0:
            result.append(start)
        start+=1
    return result

def func1(start, end):
    result = []
    for i in range(start,end+1):
        if (i%7 == 0 and i%5 != 0):
            result.append(str(i))
    return result

#r = (func1(1,100))
#print(r)
#print(',and,'.join(r))

########################################################################

def factorial(n):
    if n>1:
        return n*factorial(n-1)
    else:
        return 1

#print(factorial(5.4))
