# For bool types (immutable)
print("Booleans:")
a = True
print("before change: value of a = ", a, ", and type of a = ", type(a), ", and ID of a = ", id(a))
a = False
print("after change: value of a = ", a, ", and type of a = ", type(a), ", and ID of a = ", id(a))
print("_____________________________________________________________________________________________")

# For int types (immutable)
print("int:")
a = 1
print("before change: value of a = ", a, ", and type of a = ", type(a), ", and ID of a = ", id(a))
a = 2
print("after change: value of a = ", a, ", and type of a = ", type(a), ", and ID of a = ", id(a))
print("_____________________________________________________________________________________________")

# For float types (immutable)
print("float:")
a = 1.5
print("before change: value of a = ", a, ", and type of a = ", type(a), ", and ID of a = ", id(a))
a = 2.5
print("after change: value of a = ", a, ", and type of a = ", type(a), ", and ID of a = ", id(a))
print("_____________________________________________________________________________________________")

# For string types (immutable)
print("string:")
a = "Raghav"
print("before change: value of a = ", a, ", and type of a = ", type(a), ", and ID of a = ", id(a))
a = "Mathur"
print("after change: value of a = ", a, ", and type of a = ", type(a), ", and ID of a = ", id(a))
print("_____________________________________________________________________________________________")

# For tuple types (immutable)
print("Tuple:")
a = (1,2,3)
print("before change: value of a = ", a, ", and type of a = ", type(a), ", and ID of a = ", id(a))
a = (1,4,5)
print("after change: value of a = ", a, ", and type of a = ", type(a), ", and ID of a = ", id(a))
print("_____________________________________________________________________________________________")

# For list types (mutable)
print("list:")
a = [1,2,3,4]
print("before change: value of a = ", a, ", and type of a = ", type(a), ", and ID of a = ", id(a))
a[1] = 5
print("after change: value of a = ", a, ", and type of a = ", type(a), ", and ID of a = ", id(a))
print("_____________________________________________________________________________________________")

# For set types (mutable)
print("set:")
a = {1,2,3,4}
print("before change: value of a = ", a, ", and type of a = ", type(a), ", and ID of a = ", id(a))
a.add(5)
print("after change: value of a = ", a, ", and type of a = ", type(a), ", and ID of a = ", id(a))
print("_____________________________________________________________________________________________")
