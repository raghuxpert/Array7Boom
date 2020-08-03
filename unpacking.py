# l = [1,2,3,4]
# print(l)
# print(*l)

# ##########################

# t = (1,2,3,4)
# print(t)
# print(*t)


###############
def testd1(*k):
    for i in k:
        print(i)
#
# def testd2(**kv):
#     for i in kv:
#         print(i)
#
#     for j in kv.values():
#         print(j)
# #
# d1 = {1:'a', 2:'b', 3:'c', 4:'d'}
d2 = {'1a':'a', '2b':'b', '3c':'c', '4d':'d'}

# print(d2)
# print(*d2)
# print(*d2.values())
#
testd1(*d2)
testd1(d2)
# testd1(*d2)

# testd2(**d2)

############################
def test(**kv):
    for i in kv:
        print(i)

    for j in kv.values():
        print(j)

# test(a="Real", b="Python", c="Is", d="Great", e="!")
# d = {'a':"Real", 'b':"Python", 'c':"Is", 'd':"Great", 'e':"!"}
# d = {1:"Real", 2:"Python", 3:"Is", 4:"Great", 5:"!"}
# testd1({'a':"Real", 'b':"Python", 'c':"Is", 'd':"Great", 'e':"!"})
# test(**d)