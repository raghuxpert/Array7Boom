# import os
# with open("test2.txt",'w',encoding = 'utf-8') as f:
#    f.write("my first file2\n")
#    f.write("This file2\n")
#    f.write("contains three lines2\n")

# with open("test.txt",'r',encoding = 'utf-8') as f:
#    print(f.read(4))
#
# print(os.getcwd())

def file_reader1(file):
   f = open(file, 'r', encoding = 'utf-8')
   return f.read().split("\n")

def file_reader2(file):
   for row in open(file, 'r', encoding = 'utf-8'):
      yield row

f1 = file_reader1("test1.txt")
print("type : ", type(f1), ",and value : ", f1, ",and ID : ", id(f1))

f2 = file_reader2("test2.txt")
print("type : ", type(f2), ",and value : ", f2, ",and ID : ", id(f2))

f3 = (row for row in open("test1.txt"))
print("type : ", type(f3), ",and value : ", f3, ",and ID : ", id(f3))

