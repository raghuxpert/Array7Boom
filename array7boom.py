def boom(arr):
    for i in arr:
        if i==7:
            return "boom"

    return "no 7 in array"

a=[1,2,3,4,7,5]
print(boom(a))