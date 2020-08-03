# t = (1,2,3,[1,2,3])
# print("type : ", type(t), ",and value : ", t, ",and ID : ", id(t))
#
# t[3][1] = 5
# print("type : ", type(t), ",and value : ", t, ",and ID : ", id(t))
from operator import itemgetter

l = [(1,3,3),(1,2,4),(2,4,3),(2,4,1)]

print(sorted(l, key=itemgetter(0,1,2)))