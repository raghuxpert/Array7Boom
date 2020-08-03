# list = [i for i in range(5)]
# print(list) #[0, 1, 2, 3, 4]
#
# list = [i for i in range(1,5)]
# print(list) #[1, 2, 3, 4]
#
# list = [i for i in range(1,5,2)]
# print(list) #[1, 3]
#
# list = [i for i in range(5,1,-1)]
# print(list) #[5, 4, 3, 2]
#
# list = [i for i in range(5,1,-2)]
# print(list) #[5, 3]
# #
# # ##################################################

# list = [1,2,3,4,5]
#
# l = [i for i in list]
# print(l) #[1, 2, 3, 4, 5]
#
# l = [i*2 for i in list]
# print(l) #[2, 4, 6, 8, 10]
#
# l = [i for i in list if i%2 == 0]
# print(l) #[2, 4]
#
# l = [i*i for i in list if i%2 == 0]
# print(l) #[4, 16]
#
# l = [i*i for i in list if i%2 != 0]
# print(l) #[1, 9, 25]

##################################################
#
# list = [1,2,3,4,5]
#
# l = (i for i in list)
# print(next(l)) #[1, 2, 3, 4, 5]
#
# l = (i*2 for i in list)
# print(next(l)) #[2, 4, 6, 8, 10]
#
# l = (i for i in list if i%2 == 0)
# print(next(l))
#
# l = (i*i for i in list if i%2 == 0)
# print(next(l)) #[4, 16]
#
# l = (i*i for i in list if i%2 != 0)
# print(next(l)) #[1, 9, 25]

###########################################
list = (i for i in range(5))
print(next(list)) #[0, 1, 2, 3, 4]

list = (i for i in range(1,5) if i%2 == 0)
for i in list:
    print(i)

list = (i for i in range(1,5,2))
for i in list:
    print(i)

list = (i for i in range(5,1,-1))
for i in list:
    print(i)

list = (i for i in range(5,1,-2))
for i in list:
    print(i)

