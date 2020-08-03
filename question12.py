#Write a program, which will find all such numbers between 1000 and 3000 (both included) such that each digit of the number is an even number.
#The numbers obtained should be printed in a comma-separated sequence on a single line.

def evenint(a):
   a = str(a)
   for i in a:
       if int(i)%2 != 0:
           return False

   return True

a = input("insert 2 numbers : ").split(",")
x = int(a[0])
y = int(a[1])

c = list(filter(evenint, range(x, y+1)))
print(c)