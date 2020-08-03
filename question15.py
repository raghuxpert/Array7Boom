#Write a program that computes the value of a+aa+aaa+aaaa with a given digit as the value of a.
#Suppose the following input is supplied to the program:
#9
#Then, the output should be:
#11106

n = int(input("insert count : "))
d = {}
out = 0

for i in range(n):
    if i == 0:
       d[i] = 9
    else:
       d[i] = d[i-1]*10 + 9

for i in range(len(d)):
    out+=d[i]

print(out)