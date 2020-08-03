# a = {1,2,3}
# print("type : ", type(a), ",and value : ", a, ",and ID : ", id(a))

# b = {3,4,5}
# print("type : ", type(b), ",and value : ", b, ",and ID : ", id(b))
# print(b.union(a))

# c  = b.difference(a)
# print("type : ", type(a), ",and value : ", a, ",and ID : ", id(a))
# print("type : ", type(b), ",and value : ", b, ",and ID : ", id(b))
# print("type : ", type(c), ",and value : ", c, ",and ID : ", id(c))

# b.difference_update(a)
# print("type : ", type(a), ",and value : ", a, ",and ID : ", id(a))
# print("type : ", type(b), ",and value : ", b, ",and ID : ", id(b))

a = frozenset([1, 2, 3, 4])
print("type : ", type(a), ",and value : ", a, ",and ID : ", id(a))

