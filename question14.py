#Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters.
#Suppose the following input is supplied to the program:
#Hello world!
#Then, the output should be:
#UPPER CASE 1
#LOWER CASE 9

line = input("write something : ")
d = {"Upper":0, "Lower":0}

for i in line:
    if i.isupper():
        d["Upper"]+=1

    if i.islower():
        d["Lower"]+=1

print("Total Uppercase : ", d["Upper"])
print("Total Lowercase : ", d["Lower"])