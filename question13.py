#Write a program that accepts a sentence and calculate the number of letters and digits.
#Suppose the following input is supplied to the program:
#hello world! 123
#Then, the output should be:
#LETTERS 10
#DIGITS 3

line = input("insert some text : ")
d = {"letters":0, "numbers":0}

for i in line:
    if i.isalpha():
        d["letters"]+=1
    if i.isnumeric():
        d["numbers"]+=1

print("Total Letters : ", d["letters"])
print("Total numbers : ", d["numbers"])