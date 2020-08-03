# def i_am_decorator(func):
#     def dec():
#         print("i am decorated")
#         func()
#     return dec
#
# @i_am_decorator
# def i_am_ordinary():
#     print("i am ordinary")
#
# i_am_ordinary()

###############################################

# def smart_devide(func):
#     def inner(a, b):
#         if b == 0:
#             print("opps wrong input")
#             return
#         return func(a, b)
#     return inner
#
# @smart_devide
# def devide(a, b):
#     return a/b
#
# print(devide(2,5))
# print(devide(2,0))

#########################

def universal_decorator(func):
    def inner(*args, **kwargs):
        print("i am decorator")
        return func(*args, **kwargs)
    return inner

@universal_decorator
def func(*a, **b):
    sum = 0
    for i in a:
        sum+=i

    for j in b.values():
        sum+=j

    return sum

t = (1,2,3)
d = {1:1, 2:2, 3:3}

print(func(*d, *t))
