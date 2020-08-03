import numpy as np
#Write a program which accepts a sequence of comma separated 4 digit binary numbers as its input and then check whether they are divisible by 5 or not. The numbers that are divisible by 5 are to be printed in a comma separated sequence.
#Example:
#0100,0011,1010,1001
#Then the output should be:
#1010

def bintoint(a):
    output = []
    for i in a:
        x = int(i,2)
        if x%5 == 0:
            output.append(i)
    return output

a = input("insert comma seperated binary numbers : ").split(",")
b = bintoint(a)
print(b)


